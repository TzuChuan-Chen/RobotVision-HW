#  HW2 BMP格式圖檔做Power law transformation
from bmp_reader import GetBMPData # 自己寫的bmp reader

def normalization(data, max_range):
    # 對image_data做normalization
    norm_data = []
    max_sum = max(data) # 另外寫能加快速度
    min_sum = min(data)

    for i in range(len(data)):
        norm_data.append((data[i] - min_sum) * max_range / (max_sum - min_sum))

    return norm_data

def image_create(transformation = 'error', bmp_name = 'output/test.bmp', constant = 1, gamma = 1):
    if transformation == 'power law':
        f = open(bmp_name, 'wb')
        f.write(file_header)
        f.write(info_header)
        f.write(image_rgb)

        #  Power law transformation 𝑠=𝑐(𝑟+𝜀)^Υ 不考慮𝜀
        trans_data = []
        for i in range(len(image_data)):
            trans_data.append(constant * ((image_data[i])**gamma))

        norm_data = normalization(trans_data, 255)
        for j in range(len(norm_data)):
            f.write(round(norm_data[j]).to_bytes(1, byteorder='big'))

        f.close()

    else:
        print('error')
        
if __name__ == "__main__":
    # 取得power_law.bmp的資料
    power_law_bmp = GetBMPData('power_law.bmp')
    file_header = power_law_bmp.file_header
    info_header = power_law_bmp.info_header
    image_rgb = power_law_bmp.rgb_quad
    image_data = power_law_bmp.image_data
    image_create("power law","output/powerlaw.bmp", 1, 5)
