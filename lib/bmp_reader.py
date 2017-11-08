
class BMPReader(object):
    def __init__(self, filename):
        self._filename = filename

    def get_pixels(self, pixel_size):
        img_data = []
        raw_data = self._read_img_data()
        raw_data = raw_data[::-1][0:pixel_size * 3]

        for i in range(pixel_size):
            B = raw_data.pop()
            G = raw_data.pop()
            R = raw_data.pop()
            img_data.append((R, G, B))

        return img_data

    def _read_img_data(self):
        raw_data = []
        img_file = open(self._filename, 'rb')

        try:
            byte = ord(img_file.read(1))

            while byte != "":
                raw_data.append(byte)
                byte = ord(img_file.read(1))
        except:
            pass
        finally:
            img_file.close()

        return raw_data
