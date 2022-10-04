#  HW2 BMP格式圖檔做Log transformation
from math import log
from bmp_reader import GetBMPData # 自己寫的bmp reader

def normalization(data, max_range):
    # 對image_data做normalization
    norm_data = []
    max_sum = max(data) # 另外寫能加快速度
    min_sum = min(data)

    for i in range(len(data)):
        norm_data.append((data[i] - min_sum) * max_range / (max_sum - min_sum))

    return norm_data

def image_create(transformation = 'error', bmp_name = 'output/test.bmp', constant = 1):
    if transformation == 'log':
        f = open(bmp_name, 'wb')
        f.write(file_header)
        f.write(info_header)
        f.write(image_rgb)

        #  Log transformation 𝑠=𝑐log(1+𝑟)
        trans_data = []
        for i in range(len(image_data)):
            trans_data.append(constant * log(image_data[i] + 1))

        norm_data = normalization(trans_data, 255)
        for j in range(len(norm_data)):
            f.write(round(norm_data[j]).to_bytes(1, byteorder='big'))
            
        f.close()

    else:
        print('error')
        
if __name__ == "__main__":
    # 取得logarithm.bmp的資料
    log_bmp = GetBMPData('logarithm.bmp')
    file_header = log_bmp.file_header
    info_header = log_bmp.info_header
    image_rgb = log_bmp.rgb_quad
    image_data = log_bmp.image_data
    image_create("log", "output/log.bmp", 1)
