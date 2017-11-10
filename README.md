# Simple BMP image reader for Circuit/MicroPython

This class reads in a simple BMP image returning a multi-dimensional array of
RGB values ideal for displaying with an array of Neopixels.

## Installation

Copy lib/bmp_reader.py to the /lib directory on your Circuit/MicroPython device.

## Usage

    >>> from bmp_reader import BMPReader
    >>> img = BMPReader('image.bmp')
    >>> img.width
    8
    >>> img.height
    8
    >>> pixels = img.get_pixels()
    >>> pixels[0][0] # top-left
    (255, 0, 0)
    >>> pixels[7][7] # bottom-right
    (0, 255, 255)

For a more complete example displaying the image on an 8x8 Neopixel display, see
example.py.

## Image format

This reader only understands very basic aspects of the BMP format.  The library
supports images with 24-bit colour depth and no compression.  The example
image.bmp file was created in GIMP.
