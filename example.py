"""
This example uses a Pimoroni Unicorn Hat with the input pin (GPIO18) attached to
digital pin 6 of an Adafruit Feather board running CircuitPython.  It reads in a
8x8 pixel 24 bit colour BMP image.
"""

import board
import neopixel
from bmp_reader import BMPReader

def get_index(i):
    """ In the bitmap image, we're reading the pixel data out in the same order
        for each row but in the Unicorn board, the rows 'snake', starting in the
        top right and going right-to-left then left-to-right with each
        subsequent row.  So we need to reverse the even rows to ensure the
        display matches the bitmap image.
    """
    if int(i / 8) % 2: # Even line so reverse the index
        return (int(i / 8) * 8) + (7 - int(i % 8))
    else: # Odd line
        return i

imdata = BMPReader('image.bmp').get_pixels(64)
pixels = neopixel.NeoPixel(board.D6, 64, brightness=0.025, auto_write=False)

for i in range(64):
    pixels[get_index(i)] = imdata.pop()

pixels.show()
