#HW1 read bitmap image data

class GetBMPData:
    def __init__(self, file_name):

        #讀取整個bmp file的raw data存到self.bmp_data
        self.file_name = file_name
        f = open(self.file_name, "rb")
        self.bmp_data = f.read()
        f.close()

        #讀取header的offbytes當作image data的開始index
        self.offbytes = int.from_bytes(self.bmp_data[11:9:-1], 'big')
        
        #依序存取fileheader infoheader rgbquad imagedata
        self.file_header = self.bmp_data[:14]
        self.info_header = self.bmp_data[14:54]
        self.rgb_quad = self.bmp_data[54:self.offbytes]
        self.image_data = self.bmp_data[self.offbytes:]
        
    #   依照header格式讀取fileheader的資料並存入對應的struct tag利用dictionary方法取值
    def fileheader(self, tag):
        """
        tag dict: bfType, bfSize, bfOffbytes, fileheaderlen
        """
        
        #用.hex()方便閱讀
        bfType = self.file_header.hex()[0:4]
        bfSize = self.file_header.hex()[4:12]
        bfReserved1 = self.file_header.hex()[12:16]
        bfReserved2 = self.file_header.hex()[16:20]
        bfOffbytes = self.file_header.hex()[20:28]
        fileheaderlen = len(self.file_header)
        
        tagdict = {'bfType' : bfType, 'bfSize' : bfSize, 'bfOffbytes' : bfOffbytes, 'fileheaderlen' : fileheaderlen}

        #print(tag, 'bytes:', tagdict[tag], '\n')
        return tagdict[tag]
    
    #   依照header格式讀取infoheader的資料並存入對應的struct tag利用dictionary方法取值
    def infoheader(self, tag):
        """
        tag dict: biSize, biWidth, biHeight, biPlanes, biBitCount, biCompression,
                  biSizeImage, biXPelsPerMeter, biYPelsPerMeter, biClrUsed,
                  biClrImportant, infoheaderlen
        """

        #用.hex()方便閱讀
        biSize = self.info_header.hex()[0:8]
        biWidth = self.info_header.hex()[8:16]
        biHeight = self.info_header.hex()[16:24]
        biPlanes = self.info_header.hex()[24:28]
        biBitCount = self.info_header.hex()[28:32]
        biCompression = self.info_header.hex()[32:40]
        biSizeImage = self.info_header.hex()[40:48]
        biXPelsPerMeter = self.info_header.hex()[48:56]
        biYPelsPerMeter = self.info_header.hex()[56:64]
        biClrUsed = self.info_header.hex()[64:72]
        biClrImportant = self.info_header.hex()[72:80]
        infoheaderlen = len(self.info_header)
        
        tagdict = {'biSize' : biSize, 'biWidth' : biWidth, 'biHeight' : biHeight, 'biPlanes' : biPlanes, 
                   'biBitCount' : biBitCount, 'biCompression' : biCompression, 'biSizeImage' : biSizeImage,
                   'biXPelsPerMeter' : biXPelsPerMeter, 'biYPelsPerMeter' : biYPelsPerMeter, 'biClrUsed' : biClrUsed, 
                   'biClrImportant' : biClrImportant, 'infoheaderlen' : infoheaderlen}

        #print(tag, 'bytes: ', tagdict[tag])
        return tagdict[tag]


if __name__ == "__main__":

    print('')
    print('>>>BITMAPFILEHEADER<<<')
    fileheader_taglist = ['bfType', 'bfSize', 'bfOffbytes']
    for i in fileheader_taglist:
        print(i + 'bytes: ' + GetBMPData('testgray.bmp').fileheader(i))



    print('')
    print('>>>BITMAPINFO<<<')
    infoheader_taglist = ['biSize', 'biWidth', 'biHeight', 'biPlanes', 'biBitCount', 'biCompression',
                  'biSizeImage', 'biXPelsPerMeter', 'biYPelsPerMeter', 'biClrUsed',
                  'biClrImportant']
    for i in infoheader_taglist:
        print(i + 'bytes: ' + GetBMPData('testgray.bmp').infoheader(i))

    print('File Size:', len(GetBMPData('testgray.bmp').bmp_data))
    #print(GetBMPData("output/combine.bmp").image_data.hex(' '))