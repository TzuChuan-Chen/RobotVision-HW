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
        file_info = self.bmp_data[14:55]
        return file_info

    def filedata(self):
        file_data = self.bmp_data[55:]
        return file_data

if __name__ == "__main__":
    header = GetBMPData('testgray.bmp').fileheader()
    print(header.hex(' '))

    info = GetBMPData('testgray.bmp').fileinfo()
    print(info.hex(' '))

    data = GetBMPData('testgray.bmp').filedata()
    print(data.hex(' '))
     



    