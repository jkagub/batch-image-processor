# image-manipulation
A simple script for manipulating images using PIL on python

The images received are in the wrong format:

.tiff format
Image resolution 192x192 pixel (too large)
Rotated 90° anti-clockwise

The output will be in format:
.jpeg
Image resolution 128x128 pixel

Iterate through each file in the /images folder
For each file:
Rotate the image 90° clockwise
Resize the image from 192x192 to 128x128
Save the image to a new folder in .jpeg format
