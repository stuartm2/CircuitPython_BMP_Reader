"""
This example uses a Pimoroni Unicorn Hat with the input pin (GPIO18) attached to
digital pin 6 of an Adafruit Feather board running CircuitPython.  It reads in a
8x8 pixel 24 bit colour BMP image.
"""

import board
import neopixel

from bmp_reader import BMPReader

img = BMPReader('image.bmp')

pixels = neopixel.NeoPixel(board.D6,
                           img.width * img.height,
                           brightness=0.025,
                           auto_write=False)

pixel_grid = img.get_pixels()
i = 0

for row in range(img.height):
    for col in range(img.width):
        # The Unicorn Hat arranges its pixels starting top-right and alternates
        # back and forth with each row so we need to reverse the even rows
        if row % 2 == 0:
            col = img.width - 1 - col

        pixels[i] = pixel_grid[row][col]
        i += 1

pixels.show()
