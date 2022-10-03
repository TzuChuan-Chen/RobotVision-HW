# HW2 

from math import log
from bmp_reader import GetBMPData # 自己寫的reader

def normalization(data):

    # 將image_data做normalization到0~255
    sum = []
    norm_sum = []
    for i in range(len(data)):
        sum.append(log(data[i] + 1))

    max_sum = max(sum) # 另外寫能加快速度
    min_sum = min(sum)
    #print(max_sum, ',', min_sum)

    for i in range(len(sum)):
        norm_sum.append(round((sum[i] - min_sum) * 255 // (max_sum - min_sum)))
        #print(len(norm_sum))
        #f.write(round((sum[i] - min_sum) * 255 // (max_sum - min_sum)).to_bytes(1, byteorder='big'))

    return norm_sum

def image_create(transformation = 'error', scaling_factor = 1, bmp_name = 'output/test.bmp',):
    
    # Log transformation
    if transformation == 'Log':
        f = open(bmp_name, 'wb')
        f.write(file_header)
        f.write(info_header)
        f.write(image_rgb)
        #f.write(image_data)

        norm_sum = normalization(image_data)
        for k in range(len(norm_sum)):
            f.write(norm_sum[k].to_bytes(1, byteorder='big'))

        f.close()
        
    else:
        print('error')
        
if __name__ == "__main__":
    newbmp = GetBMPData('logarithm.bmp')
    file_header = newbmp.file_header
    info_header = newbmp.info_header
    image_rgb = newbmp.rgb_quad
    image_data = newbmp.image_data

    image_create("Log", 5, "output/log.bmp")
