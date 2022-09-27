#HW1 read bitmap image data

class GetBMPData:
    def __init__(self, file_name):
        
        self.file_header = b''
        self.info_header = b''
        self.image_data = b''
        self.file_name = file_name
        self.offbytes = int(0x0436)
        f = open(self.file_name, "rb")
        self.bmp_data = f.read()
        f.close()

    def fileheader(self):
        self.file_header = self.bmp_data[:14]
        return self.file_header

    def fileinfo(self):
        self.file_info = self.bmp_data[14:54]
        return self.file_info

    def rgbquad(self):
        self.rgb_quad = self.bmp_data[54:self.offbytes]
        return self.rgb_quad

    def imagedata(self):
        self.image_data = self.bmp_data[self.offbytes:]
        return self.image_data


if __name__ == "__main__":
    header = GetBMPData('testgray.bmp').fileheader()
    #print(header.hex(' '))
    info = GetBMPData('testgray.bmp').fileinfo()
    #print(info.hex(' '))
    rgb = GetBMPData('testgray.bmp').rgbquad()
    #print(rgb.hex(' '))
    data = GetBMPData('testgray.bmp').imagedata()
    #print(data.hex(' '))

