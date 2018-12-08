# SeamCarving
Seam Carving implementation based on *[Seam Carving for Content-Aware Image Resizing](https://inst.eecs.berkeley.edu/~cs194-26/fa16/hw/proj4-seamcarving/imret.pdf)* paper. 

## run 
`
python carve.py <h/w> <scale> </path/to/input> </path/to/output>
`

## Result
#### `Original - Seam = Carved`
#### Width carving
| Original | Seam | Carved |
| --- | --- | --- |
| ![original](https://raw.githubusercontent.com/ktw361/SeamCarving/master/imgs/Broadway_tower.jpg)| ![Seam](https://raw.githubusercontent.com/ktw361/SeamCarving/master/output_imgs/Broadway_tower_shrunk_seam.jpg) | ![shrunk](https://raw.githubusercontent.com/ktw361/SeamCarving/master/output_imgs/Broadway_tower_shrunk.jpg) |

#### Height carving
| Original | Seam | Carved |
| --- | --- | --- |
| ![original](https://raw.githubusercontent.com/ktw361/SeamCarving/master/imgs/night.jpg) | ![shrunk](https://raw.githubusercontent.com/ktw361/SeamCarving/master/output_imgs/night_shrunk_seam.jpg)| ![shrunk](https://raw.githubusercontent.com/ktw361/SeamCarving/master/output_imgs/night_shrunk.jpg)|
