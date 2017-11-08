# Simple BMP image reader for CircuitPython

This class reads in a simple BMP image returning an array of RGB values ideal
for displaying with an array of Neopixels.

## Installation

Copy lib/bmp_reader.py to the /lib directory on your CircuitPython device.

## Usage

    >>> from bmp_reader import BMPReader
    >>> BMPReader('image.bmp').get_pixels(5)
    [(0, 255, 255), (0, 255, 0), (255, 255, 0), (127, 0, 0), (127, 0, 127)]

For a more complete example displaying the image on an 8x8 Neopixel display, see
example.py.

## Image format
