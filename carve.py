import sys
from tqdm import trange
import numpy as np
from imageio import imread, imwrite
from scipy.ndimage.filters import convolve
import numba


def calc_energy(img):
    """
    calculate image energy based on gradient using sobel operator

    Args:
        img:  numpy.ndarray of shape [H, W, C]

    Returns:
        energy_map:  numpy.ndarray of shape [H, W]
    """

    kern_du = np.asarray([[1., 2., 1.],
                       [0. , 0. , 0.,],
                       [-1., -2., -1.]])
    kern_dv = kern_du.T
    filter_du = np.stack([kern_du] * 3, axis = 2)
    filter_dv = np.stack([kern_dv] * 3, axis = 2)
    img = img.astype(np.float32)
    convolved = np.absolute(convolve(img, filter_du)) + np.absolute(convolve(img, filter_dv))
    energy_map = np.sum(convolved , axis = 2)
    return energy_map

@numba.jit
def minimal_seam(energy_map):
    """
    get M and seam route index based on energy map

    Args:
        energy_map:  numpy.ndarray of shape [H, W]

    Returns:
        M:  stores seam energy w.r.t each line(row)
        track: stroes which(index of) element used by *Next* row
    """

    H, W = energy_map.shape

    M = energy_map.copy()
    track = np.zeros_like(M, dtype = np.int32)

    # compute seam
    for i in range(1,H):
        track[i, 1] = np.argmin(M[i-1, :2])
        M[i, 0] += M[i - 1, track[i, 0]]

        for j in range(1, W):
            track[i, j] = np.argmin(M[i - 1, j - 1:j + 2]) + (j - 1)
            M[i, j] += M[i - 1, track[i, j]]

    return M, track

def process_seam(original, removed):
    """
    Process seam from progressively removed list

    Args:
        original:  same as image, [H, W, C]
        removed:   list of list, (# of removedseams, Width/Height)

    Returns:
        image_sesam:
                image_seam: original image with removed seam highlighted,
                same shape as original
    """

    H, W, C = np.shape(original)
    image_seam = original
    removed = np.asarray(removed, np.int32)

    for i in range(1, np.shape(removed)[0]):
        for k in range(i-1):
            removed[i, removed[i] >= removed[k]] += 1

    ind_h = np.asarray(range(H))[::-1] # flip!
    ind_h = np.stack([ind_h] * np.shape(removed)[0], axis = 0)
    ind_seam = np.stack([ind_h, removed], axis = 2) # [num_seam, H, 2]
    ind_seam = np.reshape(ind_seam, [-1,2])

    image_seam[ind_seam[:,0], ind_seam[:,1]] = [255, 0, 0] # Red channel

    return image_seam

def horizontal_carving(image, scale_w):
    """
    Carve image by removing minimal_seam repetitively until meet width scale

    Args:
        image:  image input, ndarray shape [H, W, C]
        scale_w:  expected final scale of width

    Returns:
        image_carved: carved image of shape [H, W * scale_w, C]
        image_seam: original image with removed seam highlighted
    """

    @numba.jit
    def _carve_one_column(img):
        H, W, C = img.shape
        # Get energy map
        energy_map = calc_energy(img)
        # Get minimal_seam
        M, track = minimal_seam(energy_map)
        pick = np.argmin(M[-1,:])
        mask = np.ones_like(energy_map, dtype = np.bool)
        mask[-1, pick] = False

        pick_list = [pick]
        # from -2 to -H(included)
        # 即从倒二行到第一行
        for i in range(-2, - H - 1, -1):
            pick = track[i, pick]
            mask[i, pick] = False
            pick_list += [pick]

        img = np.reshape(img[mask], [H, W - 1, 3])
        return img, pick_list

    removed = []
    original = image.copy()

    H, W, C = image.shape
    W_finish = int(np.round(W * scale_w))

    # Real carve
    for i in trange(W - W_finish):
        image, pick_list = _carve_one_column(image)
        removed += [pick_list]
    image_seam = process_seam(original, removed)

    return image, image_seam

def vertical_carving(image, scale_h):
    """
    Carve image horizontally
    Args & Returns:
    	See horizontal_carving()
    """

    image = np.rot90(image, 1, (0, 1))
    image, image_seam = horizontal_carving(image, scale_h)
    image = np.rot90(image, 3, (0, 1))
    image_seam = np.rot90(image_seam, 3, (0, 1))
    return image, image_seam

def main():
    if len(sys.argv) != 5:
    	print('usage: carve.py <h/w> <scale> <image_in> <image_out>', file=sys.stderr)
    	sys.exit(1)

    which_axis = sys.argv[1]
    scale = float(sys.argv[2])
    in_filename = sys.argv[3]
    out_filename = sys.argv[4]

    img = imread(in_filename)

    if which_axis == 'h':
    	out, seam = vertical_carving(img, scale)
    elif which_axis == 'w':
    	out, seam  = horizontal_carving(img, scale)
    else:
    	print('usage: carve.py <h/w> <scale> <image_in> <image_out>', file=sys.stderr)
    	sys.exit(1)
    imwrite(out_filename, out)
    imwrite(out_filename.split('.')[0] + "_seam.jpg", seam)

if __name__ == '__main__':
    main()
