#HW1 create a bitmap image 

'''
42 4D 4E FA 00 00 00 00 00 00 36 04 00 00 28 00 00 00 FA 00 00 00 FA 00 00 00 01 00 08 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
'''

f = open("testgray_origin.bmp", "rb")
data = f.read()
print(data[:14])

a = bytes.fromhex('42 4D 50 00 00 00 00 00 00 00 36 00 00 00 28 00 00 00 02 00 00 00 03 00 00 00 01 00 18 00 00 00 00 00 1A 00 00 00 12 0B 00 00 12 0B 00 00 00 00 00 00 00 00 00 00 72 C6 F0 CC 33 66 00 00 66 00 FF FF CC FF 00 00 66 CC 99 CC CC CC 00 00 00 00')
print(a)

f.close()




f = open("myImage.bmp", "wb")
f.write(a)
f.close()

