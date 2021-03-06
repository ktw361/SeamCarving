# SeamCarving
Seam Carving implementation based on *[Seam Carving for Content-Aware Image Resizing](https://inst.eecs.berkeley.edu/~cs194-26/fa16/hw/proj4-seamcarving/imret.pdf)* paper. 

## Run 
`
python carve.py <h/w> <scale> </path/to/input> </path/to/output>
`

## Result
#### `Original - Seam = Carved`

| Original | Seam | Carved |
| --- | --- | --- |
| ![original](https://raw.githubusercontent.com/ktw361/SeamCarving/master/imgs/Broadway_tower.jpg) | ![shrunk](https://raw.githubusercontent.com/ktw361/SeamCarving/master/output_imgs/Broadway_tower_shrunk_seam.jpg)| ![shrunk](https://raw.githubusercontent.com/ktw361/SeamCarving/master/output_imgs/Broadway_tower_shrunk.jpg)|


### Width carving
| Original | Carved |
| ---  | --- |
| ![original](https://raw.githubusercontent.com/ktw361/SeamCarving/master/imgs/home_2.jpg)|  ![shrunk](https://raw.githubusercontent.com/ktw361/SeamCarving/master/output_imgs/home_2_shrunk.jpg) |

### Height carving

| Original | Carved |
| ---  | --- |
| ![original](https://raw.githubusercontent.com/ktw361/SeamCarving/master/imgs/home_1.jpg)|  ![shrunk](https://raw.githubusercontent.com/ktw361/SeamCarving/master/output_imgs/home_1_shrunk.jpg) |
| ![original](https://raw.githubusercontent.com/ktw361/SeamCarving/master/imgs/night.jpg) | ![shrunk](https://raw.githubusercontent.com/ktw361/SeamCarving/master/output_imgs/night_shrunk.jpg)|

## Acknowledgements

Many thanks to the great post: https://karthikkaranth.me/blog/implementing-seam-carving-with-python/
