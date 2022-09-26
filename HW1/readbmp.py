#HW1 read bitmap image data

class GetBMPData:
    def __init__(self, file_name):
        
        self.file_header = ''
        self.info_header = ''
        self.image_data = ''
        self.file_name = file_name
        f = open(self.file_name, "rb")
        self.bmp_data = f.read()
        f.close()

    def fileheader(self):
        file_header = self.bmp_data[:14]
        return file_header

    def fileinfo(self):
        file_info = self.bmp_data[14:54]
        return file_info

    def rgbquad(self):
        rgb_quad = self.bmp_data[54:int(0x0436)]
        return rgb_quad

    def filedata(self):
        file_data = self.bmp_data[int(0x0436):]
        return file_data



if __name__ == "__main__":

    header = GetBMPData('testgray.bmp').fileheader()
    print(header.hex(' '))

    info = GetBMPData('testgray.bmp').fileinfo()
    print(info.hex(' '))

    rgb = GetBMPData('testgray.bmp').rgbquad()
    print(rgb.hex(' '))

    data = GetBMPData('testgray.bmp').filedata()
    print(data.hex(' '))
    print(data)

    #data = GetBMPData('testgray.bmp').filedata()
    #print(data.hex(' '))

