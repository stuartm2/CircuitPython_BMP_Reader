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

This reader doesn't really understand the BMP format, it just pulls the raw binary pixel data from the end of the file and converts it to a Python list of RGB values, primarily for use with a Neopixel array.  The example image.bmp file was created in GIMP as an 8x8 pixel image, exported as a plain BMP with 24 bit colour (R8 G8 B8).  If you use any other method, your mileage will probably vary so keep it simple, get the colour mode right and apply plenty of hope.
