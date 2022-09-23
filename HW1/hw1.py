#HW1 create a bitmap image 

file_header = bytes.fromhex('42 4D 50 00 00 00 00 00 00 00 36 00 00 00')

info_header = bytes.fromhex('28 00 \
                             00 00 02 00 00 00 03 00 00 00 01 00 18 00 00 00 \
                             00 00 1A 00 00 00 12 0B 00 00 12 0B 00 00 00 00 \
                             00 00 00 00 00 00')

image_data = bytes.fromhex('72 C6 F0 CC 33 66 00 00 66 00 FF FF CC FF 00 00 66 CC 99 CC CC CC 00 00 00 00')

f = open("myImage.bmp", "wb")
f.write(file_header)
f.close()

f = open("myImage.bmp", "ab")
f.write(info_header)
f.close()

f = open("myImage.bmp", "ab")
f.write(image_data)
f.close()
