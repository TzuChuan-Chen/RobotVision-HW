#HW1 red bitmap image
from readbmp import GetBMPData


def image_create(bmp_name = 'test.bmp'):
    f = open(bmp_name, 'wb')
    f.write(file_header)
    f.close()

    f = open(bmp_name, 'ab')
    f.write(info_header)
    f.close()

    f = open(bmp_name, "ab")

    for j in range(256):
        f.write(bytes([0]))
        f.write(bytes([0]))
        f.write(bytes([j]))
        f.write(bytes([0]))

    f.close()

    f = open(bmp_name, 'ab')
    f.write(file_data)
    f.close()


if __name__ == "__main__":
    newbmp = GetBMPData('testgray.bmp')
    file_header = newbmp.fileheader()
    info_header = newbmp.fileinfo()
    image_rgb = newbmp.rgbquad()
    file_data = newbmp.filedata()

    image_create()
    test = GetBMPData('test.bmp')
    print(test.rgbquad().hex(' '))

