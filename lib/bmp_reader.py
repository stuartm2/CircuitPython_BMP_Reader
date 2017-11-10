
class BMPReader(object):
    def __init__(self, filename):
        self._filename = filename
        self._read_img_data()

    def get_pixels(self):
        """
        Returns a multi-dimensional array of the RGB values of each pixel in the
        image, arranged by rows and columns from the top-left.  Access any pixel
        by its location, eg:

        pixels = BMPReader(filename).get_pixels()
        top_left_px = pixels[0][0] # [255, 0, 0]
        bottom_right_px = pixels[8][8] # [0, 255, 255]
        """
        pixel_grid = []
        pixel_data = list(self._pixel_data) # So we're working on a copy

        for x in range(self.width):
            col = []
            for y in range(self.height):
                r = pixel_data.pop()
                g = pixel_data.pop()
                b = pixel_data.pop()
                col.append((r, g, b))
            col.reverse()
            pixel_grid.append(col)

        return pixel_grid

    def _read_img_data(self):
        def lebytes_to_int(bytes):
            n = 0x00
            while len(bytes) > 0:
                n <<= 8
                n |= bytes.pop()
            return int(n)

        with open(self._filename, 'rb') as f:
            img_bytes = list(bytearray(f.read()))

        # Before we proceed, we need to ensure certain conditions are met
        assert img_bytes[0:2] == [66, 77], "Not a valid BMP file"
        assert lebytes_to_int(img_bytes[30:34]) == 0, \
            "Compression is not supported"
        assert lebytes_to_int(img_bytes[28:30]) == 24, \
            "Only 24-bit colour depth is supported"

        start_pos = lebytes_to_int(img_bytes[10:14])
        end_pos = start_pos + lebytes_to_int(img_bytes[34:38])

        self.width = lebytes_to_int(img_bytes[18:22])
        self.height = lebytes_to_int(img_bytes[22:26])

        self._pixel_data = img_bytes[start_pos:end_pos]
