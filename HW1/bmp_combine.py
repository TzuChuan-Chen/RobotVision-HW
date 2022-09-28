#HW1 merge bk.bmp and testgray.bmp * weight
from bmp_reader import GetBMPData

def image_merge(weight = 1, bmp_name = 'output/test.bmp',):

    f = open(bmp_name, 'wb')
    f.write(file_header)
    f.write(info_header)
    f.write(image_rgb)

    sum = []
    norm_sum = []
    for i in range(len(ori_file_data)):
        sum.append(ori_file_data[i]*weight + bk_file_data[i])
    
    max_sum = max(sum)
    min_sum = min(sum)
    #print(max_sum, ',', min_sum)

    for i in range(len(sum)):
        norm_sum.append(round((sum[i] - min_sum) * 255 // (max_sum - min_sum)))
        f.write(norm_sum[i].to_bytes(1, byteorder='big'))
    #print(norm_sum[-10].to_bytes(1, byteorder='big').hex())
    #print(list(map(hex, norm_sum)))
    f.close()


if __name__ == "__main__":
    ori_bmp = GetBMPData('testgray.bmp')
    file_header = ori_bmp.file_header
    info_header = ori_bmp.info_header
    image_rgb = ori_bmp.rgb_quad
    ori_file_data = ori_bmp.image_data
    #print(ori_file_data[0])
    bk_bmp = GetBMPData('bk.bmp')
    bk_file_data = bk_bmp.image_data
    image_merge(0.95, "output/combine.bmp")
    