#include <iostream>
#include <cstdlib>
#include <string>

#define STBI_IMAGE_IMPLEMENTATION
#include "stb_image.h"


int
main(int argc, char **argv)
{
    if (argc != 5) {
        std::cerr << "usage: carve.py <h/w> <scale> <image_in> <image_out>" << std::endl;
        return -1;
    }
    int which_axis = argv[1];
    double scale = atof(argv[2]);
    const char *in_filename = argv[3];
    const char *out_filename = argv[4];

    int x, y, n;
    unsigned char *img = stbi_load(in_filename, &x, &y, &n, 0);

	img = imread(in_filename)

	if which_axis == 'h':
		out = vertical_carving(img, scale)
	elif which_axis == 'w':
		out = horizontal_carving(img, scale)
	else:
		print('usage: carve.py <h/w> <scale> <image_in> <image_out>', file=sys.stderr)
		sys.exit(1)
 
    const int comp = 3;
    const int quality = 1;
    stbi_write_jpg(out_filename, w, h, comp, out, quality):
     int stbi_write_jpg(char const *filename, int w, int h, int comp, const void *data, int quality) != 0;
	imwrite(out_filename, out)
    stbi_image_free(img);
    return 0;
}
