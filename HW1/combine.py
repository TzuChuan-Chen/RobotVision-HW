#HW1 merge bk.bmp and testgray.bmp * weight
from readbmp import GetBMPData

def image_merge(weight = 1, bmp_name = 'output/test.bmp',):

    f = open(bmp_name, 'wb')
    f.write(file_header)
    f.write(info_header)
    f.write(image_rgb)

    sum = []
    for i in range(len(ori_file_data)):
        sum.append(int(ori_file_data[i]*weight) + int(bk_file_data[i]))
    
    max_sum = max(sum)
    min_sum = min(sum)
    #print(max_sum, ',', min_sum)

    for i in range(len(sum)):
        norm_sum = (sum[i] - min_sum) * 255 // (max_sum - min_sum)
        f.write(norm_sum.to_bytes(1, byteorder='big'))
    f.close()


if __name__ == "__main__":
    ori_bmp = GetBMPData('testgray.bmp')
    file_header = ori_bmp.fileheader()
    info_header = ori_bmp.fileinfo()
    image_rgb = ori_bmp.rgbquad()
    ori_file_data = ori_bmp.imagedata()

    bk_bmp = GetBMPData('bk.bmp')
    bk_file_data = bk_bmp.imagedata()
    image_merge(1, "output/merge.bmp")
    