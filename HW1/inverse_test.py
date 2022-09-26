#HW1 inverse bitmap image
from readbmp import GetBMPData


def image_create():
    f = open('new.bmp', 'wb')
    f.write(file_header)
    f.close()

    f = open('new.bmp', 'ab')
    f.write(info_header)
    f.close()

    f = open('new.bmp', 'ab')
    rgb = image_rgb.hex()
    new_rgb = rgb[-8:]
    for i in range(8, len(rgb), 8):
        new_rgb += (rgb[(-8-i):(-i)])
    f.write(bytes.fromhex(new_rgb))
    f.close()

    f = open('new.bmp', 'ab')
    f.write(file_data)
    f.close()


if __name__ == "__main__":
    newbmp = GetBMPData('testgray.bmp')
    file_header = newbmp.fileheader()
    info_header = newbmp.fileinfo()
    image_rgb = newbmp.rgbquad()
    file_data = newbmp.filedata()

    image_create()

