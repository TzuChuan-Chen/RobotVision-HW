#HW1 產生灰階漸漸圖

file_header = bytes.fromhex('42 4D 00 00 00 00 00 00 00 00 36 00 00 00')

info_header = bytes.fromhex('28 00 \
                             00 00 ff 00 00 00 64 00 00 00 01 00 18 00 00 00 \
                             00 00 00 00 00 00 ff 00 00 00 64 00 00 00 00 00 \
                             00 00 00 00 00 00')

def image_create():
    f = open("myImage.bmp", "wb")
    f.write(file_header)
    f.close()

    f = open("myImage.bmp", "ab")
    f.write(info_header)
    f.close()

    f = open("myImage.bmp", "ab")
    for i in range(100):
        for j in range(255):
            for k in range(3):
                f.write(bytes([j]))
        for r in range(3):
            f.write(bytes([0]))
    f.close()

if __name__ == "__main__":
    image_create()



