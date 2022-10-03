#HW1 產生灰階漸漸圖
from bmp_reader import GetBMPData

def image_create(width, height):
    #依序寫入file_header info_header image_rgb
    f = open("output/gray_level.bmp", "wb")
    f.write(file_header)
    f.write(info_header)
    f.write(image_rgb)

    #製作灰階漸進圖，長度不能整除4時做zero padding
    pad_width = width * 3
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
    
    f.close()

if __name__ == "__main__":
    ori_bmp = GetBMPData('testgray.bmp')
    file_header = ori_bmp.file_header
    info_header = bytes.fromhex('28 00 \
                             00 00 ff 00 00 00 64 00 00 00 01 00 18 00 00 00 \
                             00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 \
                             00 00 00 00 00 00')

    image_rgb = ori_bmp.rgb_quad

    image_create(255, 100)
