import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import glob
from scipy.signal import find_peaks


def find_range(f, x):
    """
    Find range between nearest local minima from peak at index x
    """
    for i in range(x+1, len(f)):
        if f[i+1] >= f[i]:
            uppermin = i
            break
    for i in range(x-1, 0, -1):
        if f[i] <= f[i-1]:
            lowermin = i + 1
            break
    return (lowermin, uppermin)


if __name__ == '__main__':
    cv2.namedWindow('windows', cv2.WINDOW_NORMAL)

    list_images = glob.iglob("HW_Image/*")
    my_img = []
    for title in list_images:
        my_img.append(cv2.imread(title, cv2.IMREAD_GRAYSCALE))
    # print(my_img)

    img = my_img[9]

    # np.set_printoptions(threshold=np.inf)

    # img = img[800:, :]

    # print(img.shape)

    img = cv2.medianBlur(img, 9)

    contrast = 1
    brightness = 0

    image_copy = img.copy()
    vt_ref = img[:, 500]

    # kernel = np.ones((15, 15), np.uint8)
    # img = cv2.dilate(img, kernel, iterations=10)
    #img = img * (img / 127 + 1) - img + brightness  # 轉換公式
    #img = ((img-np.min(img)) * 255) / (np.max(img)-np.min(img))
    print(img[:500])
    # img = np.where(img < 200, img, 255)
    # img = np.where(img < 100, img, 0)
    #img = img.astype(np.uint8)
    #print(vt_ref)

    # diff = np.diff(vt_sp)
    # print(diff)
    # print(np.where(diff > 50))

    vt_head = vt_ref[:1000]
    vt_tail = vt_ref[700:-1]

    # print(np.where(vt_tail < 20))
    start_idx = np.where(vt_head < 255)
    #print(start_idx)
    # end = np.where(vt_tail > 50)
    end = np.where(vt_tail < 35)[0][-1]
    roi_img = image_copy[:, :]
    vt_1 = roi_img[:, 200]
    vt_2 = roi_img[:, 500]
    vt_3 = roi_img[:, 800]
    # print(vt)

    # vt = np.clip(vt, 30, 100)

    cv2.imshow("windows", img)
    cv2.waitKey(0)
    cv2.imwrite('output.png', roi_img)
    cv2.destroyAllWindows()

    peaks1, _ = find_peaks(vt_1, distance=20)
    peaks2, _ = find_peaks(vt_2, distance=20)
    peaks3, _ = find_peaks(vt_3, distance=20)
    print(len(peaks1))
    print(len(peaks2))
    print(len(peaks3))
    plt.plot(peaks1, vt_1[peaks1], "x")
    plt.plot(np.zeros_like(vt_1), "--", color="gray")
    pimg = plt.imread('output.png')

    plt.imshow(np.rot90(pimg), cmap='gray')
    plt.plot(vt_1)

    plt.show()






