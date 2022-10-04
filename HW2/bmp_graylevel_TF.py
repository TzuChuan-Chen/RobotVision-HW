#  HW2 BMP格式圖檔調整亮度與直方圖等化

from cProfile import label
from math import log
import matplotlib.pyplot as plt
from bmp_reader import GetBMPData # 自己寫的bmp reader

def normalization(data, max_range):

    # 對image_data做normalization
    norm_data = []
    max_sum = max(data) # 另外寫能加快速度
    min_sum = min(data)

    for i in range(len(data)):
        norm_data.append((data[i] - min_sum) * max_range / (max_sum - min_sum))
    # print(max(norm_data), min(norm_data))
    return norm_data

def image_create(transformation = 'error', bmp_name = 'output/test.bmp', constant = 1, gamma = 1):
    
    #  Log transformation 𝑠=𝑐log(1+𝑟)
    if transformation == 'log':
        f = open(bmp_name, 'wb')
        f.write(file_header)
        f.write(info_header)
        f.write(image_rgb)

        trans_data = []
        for i in range(len(image_data)):
            trans_data.append(constant * log(image_data[i] + 1))

        norm_data = normalization(trans_data, 255)
        for j in range(len(norm_data)):
            f.write(round(norm_data[j]).to_bytes(1, byteorder='big'))

        f.close()

    #  Power law transformation 𝑠=𝑐(𝑟+𝜀)^Υ 不考慮𝜀
    elif transformation == 'power law':
        f = open(bmp_name, 'wb')
        f.write(file_header)
        f.write(info_header)
        f.write(image_rgb)

        trans_data = []
        for i in range(len(image_data)):
            trans_data.append(constant * ((image_data[i])**gamma))

        norm_data = normalization(trans_data, 255)
        for j in range(len(norm_data)):
            f.write(round(norm_data[j]).to_bytes(1, byteorder='big'))

        f.close()
        
    elif transformation == 'histogram equalization':
        f = open(bmp_name, 'wb')
        f.write(file_header)
        f.write(info_header)
        f.write(image_rgb)
        
        # Histogram 計算
        histogram = [0] * 255
        for pixel in image_data:
            histogram[pixel] += 1

        # Histogram Equalization 計算cumulative sum
        a = iter(histogram)
        cum_sum = [next(a)]
        for i in a:
            cum_sum.append(cum_sum[-1] + i)

        cum_sum = normalization(cum_sum, 255)

        # 將image_data[j]當作cum_sum的index(都需四捨五入)
        for j in range(len(image_data)):
            f.write(round(cum_sum[round(image_data[j])]).to_bytes(1, byteorder='big'))

        f.close()

    #  (additional) negatives transformation s=L−1−r
    elif transformation == 'negatives':
        f = open(bmp_name, 'wb')
        f.write(file_header)
        f.write(info_header)
        f.write(image_rgb)

        trans_data = []
        for i in range(len(image_data)):
            trans_data.append(255 - image_data[i])

        norm_data = normalization(trans_data, 255)
        for j in range(len(norm_data)):
            f.write(round(norm_data[j]).to_bytes(1, byteorder='big'))

        f.close()

    else:
        print('error')
        
if __name__ == "__main__":

    # 要使用不同原圖檔都要宣告不同的file_header info_header image_rgb image_data
    log_bmp = GetBMPData('logarithm.bmp')
    file_header = log_bmp.file_header
    info_header = log_bmp.info_header
    image_rgb = log_bmp.rgb_quad
    image_data = log_bmp.image_data
    image_create("log", "output/log.bmp", 1)
    # image_create("negatives","output/negatives.bmp", 1) 

    power_law_bmp = GetBMPData('power_law.bmp')
    file_header = power_law_bmp.file_header
    info_header = power_law_bmp.info_header
    image_rgb = power_law_bmp.rgb_quad
    image_data = power_law_bmp.image_data
    image_create("power law","output/powerlaw.bmp", 1, 5)

    hist_eq_bmp = GetBMPData('HistogramEQ.bmp')
    file_header = hist_eq_bmp.file_header
    info_header = hist_eq_bmp.info_header
    image_rgb = hist_eq_bmp.rgb_quad
    image_data = hist_eq_bmp.image_data
    image_create("histogram equalization","output/histogram_equalization.bmp") 




    dict = {}
    for k in image_data:
        dict[k] = dict.get(k, 0) + 1
    plt.xlim([0, 255])
    plt.bar(list(dict.keys()), list(dict.values()), 0.9, label='Origin')
    

    hist2_eq_bmp = GetBMPData('output/histogram_equalization.bmp')
    image_data = hist2_eq_bmp.image_data

    dict = {}
    for k in image_data:
        dict[k] = dict.get(k, 0) + 1

    plt.bar(list(dict.keys()), list(dict.values()), 0.9, label='Equalization')

    plt.title('Histogram of image')
    plt.xlabel('Gray Level')
    plt.legend(loc='upper left')
    plt.show()
