#HW1 產生灰階漸漸圖
from readbmp import GetBMPData

'''
file_header = bytes.fromhex('42 4D FA 4E 00 00 00 00 00 00 36 00 00 00')
'''

info_header = bytes.fromhex('28 00 \
                             00 00 ff 00 00 00 64 00 00 00 01 00 18 00 00 00 \
                             00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 \
                             00 00 00 00 00 00')


def image_create():
    f = open("output/gray_level.bmp", "wb")
    f.write(file_header)
    f.write(info_header)
    f.write(image_rgb)
    width = 255
    pad_width = width * 3
    height = 100
    padding_num = 1

    while pad_width % 4 != 0:
        pad_width += padding_num
        padding_num += 1

    for i in range(height):
        for j in range(width):
            f.write(bytes([j]))
            f.write(bytes([j]))
            f.write(bytes([j]))
        for k in range(padding_num):
            f.write(bytes([0]))

if __name__ == "__main__":
    ori_bmp = GetBMPData('testgray.bmp')
    file_header = ori_bmp.file_header
    
    #info_header = ori_bmp.fileinfo()
    #print(info_header.hex())
    image_rgb = ori_bmp.rgb_quad
    #ori_file_data = ori_bmp.filedata()
    image_create()
