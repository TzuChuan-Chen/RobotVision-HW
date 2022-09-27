#HW1 更改testgray.bmp的 rgbquad 產生bitmap image

from readbmp import GetBMPData

def image_create(color = 'error', bmp_name = 'output/test.bmp',):
    
    if color == 'blue':
        f = open(bmp_name, 'wb')
        f.write(file_header)
        f.write(info_header)

        for j in range(256):
            f.write(bytes([j]))
            f.write(bytes([0]))
            f.write(bytes([0]))
            f.write(bytes([0]))
        f.write(file_data)
        f.close()
        
    elif color == 'green':
        f = open(bmp_name, 'wb')
        f.write(file_header)
        f.write(info_header)

        for j in range(256):
            f.write(bytes([0]))
            f.write(bytes([j]))
            f.write(bytes([0]))
            f.write(bytes([0]))
        f.write(file_data)
        f.close()
        
    elif color == 'red':
        f = open(bmp_name, 'wb')
        f.write(file_header)
        f.write(info_header)

        for j in range(256):
            f.write(bytes([0]))
            f.write(bytes([0]))
            f.write(bytes([j]))
            f.write(bytes([0]))
        f.write(file_data)
        f.close()
        
    elif color == 'gray':
        f = open(bmp_name, 'wb')
        f.write(file_header)
        f.write(info_header)

        for j in range(256):
            f.write(bytes([j]))
            f.write(bytes([j]))
            f.write(bytes([j]))
            f.write(bytes([0]))
        f.write(file_data)
        f.close()

    elif color == 'inverse_gray':
        f = open(bmp_name, 'wb')
        f.write(file_header)
        f.write(info_header)

        for j in range(256):
            f.write(bytes([255-j]))
            f.write(bytes([255-j]))
            f.write(bytes([255-j]))
            f.write(bytes([0]))
        f.write(file_data)
        f.close()

    else:
        print('error')
        
if __name__ == "__main__":
    newbmp = GetBMPData('testgray.bmp')
    file_header = newbmp.file_header
    info_header = newbmp.info_header
    image_rgb = newbmp.rgb_quad
    file_data = newbmp.image_data
    #GetBMPData('testgray.bmp').file_header
    image_create("blue", "output/blue.bmp")
    image_create("green", "output/green.bmp")
    image_create("red", "output/red.bmp")
    image_create("gray", "output/gray.bmp")
    image_create("inverse_gray", "output/inverse_gray.bmp")
