#  HW2 BMP格式圖檔做Histogram Equalization
import matplotlib.pyplot as plt # plot直方圖
from bmp_reader import GetBMPData # 自己寫的bmp reader

def normalization(data, max_range):
    # 對image_data做normalization
    norm_data = []
    max_sum = max(data) # 另外寫能加快速度
    min_sum = min(data)

    for i in range(len(data)):
        norm_data.append((data[i] - min_sum) * max_range / (max_sum - min_sum))

    return norm_data

def image_create(transformation = 'error', bmp_name = 'output/test.bmp'):
    if transformation == 'histogram equalization':
        f = open(bmp_name, 'wb')
        f.write(file_header)
        f.write(info_header)
        f.write(image_rgb)
        
        # Gray Level 0-255 Histogram 計算每個灰階的出現次數
        histogram = [0]*256 
        for element in image_data:
            histogram[element] +=  1

        # Histogram Equalization 計算cumulative sum
        cum_sum = []
        cdf = 0
        for n in histogram:
            cdf += n / len(image_data) # 累積分布cdf
            cum_sum.append(round(cdf * 255)) 
        # plt.plot(cum_sum) # plot cdf
        # plt.show()

        # 將image_data[j]當作cum_sum的index mapping回去原圖
        output_image_data = []
        for j in range(len(image_data)):
            output_image_data.append(cum_sum[image_data[j]])
            f.write(output_image_data[j].to_bytes(1, byteorder='big'))

        f.close()
        return output_image_data

    else:
        print('error')
        
if __name__ == "__main__":
    # 取得power_law.bmp的資料
    hist_eq_bmp = GetBMPData('HistogramEQ.bmp')
    file_header = hist_eq_bmp.file_header
    info_header = hist_eq_bmp.info_header
    image_rgb = hist_eq_bmp.rgb_quad
    image_data = hist_eq_bmp.image_data
    output_image_data = image_create("histogram equalization","output/hist_eqliz.bmp") 

    # # plot出原圖的直方圖跟Equalization後的直方圖
    # ori_dict = {}
    # for key in image_data:
    #     ori_dict[key] = ori_dict.get(key, 0) + 1
    # plt.bar(list(ori_dict.keys()), list(ori_dict.values()), label='Origin_Hist', color = 'blue')
    # eqliz_dict = {}
    # for key in output_image_data:
    #     eqliz_dict[key] = eqliz_dict.get(key, 0) + 1
    # plt.bar(list(eqliz_dict.keys()), list(eqliz_dict.values()), label='Equalization_Hist', color = 'red')
    # plt.xlim([0,256])
    # plt.title('Histogram of image')
    # plt.xlabel('Gray Level')
    # plt.legend(loc='upper left')
    # plt.show()
