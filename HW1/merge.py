#HW1 merge bk.bmp and testgray.bmp * weight

from readbmp import GetBMPData


def image_merge(weight = 1, bmp_name = 'output/test.bmp',):

    f = open(bmp_name, 'wb')
    f.write(file_header)
    f.write(info_header)
    f.write(image_rgb)

    ori = ori_file_data.hex()
    bk = bk_file_data.hex()

    for i in range(0, len(ori), 2):
        sum = int((int(ori[i:i+2], 16)*weight + int(bk[i:i+2], 16))*255//510 )
        f.write(sum.to_bytes(1, byteorder='big'))
    
    f.close()


if __name__ == "__main__":
    ori_bmp = GetBMPData('testgray.bmp')
    file_header = ori_bmp.fileheader()
    info_header = ori_bmp.fileinfo()
    image_rgb = ori_bmp.rgbquad()
    ori_file_data = ori_bmp.filedata()

    bk_bmp = GetBMPData('bk.bmp')
    bk_file_data = bk_bmp.filedata()

    image_merge(0.95, "output/merge.bmp")


