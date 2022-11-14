import cv2
import numpy as np
import matplotlib.pyplot as plt
import glob
from scipy.signal import find_peaks


if __name__ == '__main__':
    cv2.namedWindow('windows', cv2.WINDOW_NORMAL)

    list_images = glob.iglob("HW_Image/*")
    my_img = []
    for title in list_images:
        my_img.append(cv2.imread(title, cv2.IMREAD_GRAYSCALE))
    # print(my_img)

    img = my_img[8]
    gray_img = np.copy(img)

    # 使用 sobel 算子
    # 第一個參數是要作用的影像
    # 第二個參數是影像深度 使用 16 可避免 overflow 問題
    # 第三 & 四個參數是控制是否使用兩種面罩的參數
    # 第五個參數是 mask size
    kernel_size = 3
    # x = cv2.Sobel(gray_img, cv2.CV_16S, 1, 0, ksize=kernel_size)
    y = cv2.Sobel(gray_img, cv2.CV_16S, 0, 1, ksize=kernel_size)

    # 轉換為影像原本儲存的格式 uint8
    # absX = cv2.convertScaleAbs(x)
    dst = cv2.convertScaleAbs(y)

    image_copy = img.copy()

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))
    closing = cv2.morphologyEx(dst, cv2.MORPH_CLOSE, kernel, iterations=10)
    # diff = np.diff(vt_sp)
    # print(diff)
    # print(np.where(diff > 50))
    vt_ref = closing[:, 700]
    vt_head = vt_ref[:1000]
    vt_tail = vt_ref[1200:]
    print(len(vt_tail))
    # print(np.where(vt_tail < 20))
    start_idx = np.where(vt_head > 100)[0][0]

    end = np.where(vt_tail < 40)[0][0]
    print(np.where(vt_tail < 50))
    # end = np.where(vt_tail < 35)[0][-1]
    roi_img = image_copy[start_idx:end+1200, :]
    vt_1 = roi_img[:, 50]
    vt_2 = roi_img[:, 200]
    vt_3 = roi_img[:, 500]
    vt_4 = roi_img[:, 800]
    vt_5 = roi_img[:, 950]

    cv2.imshow("windows", closing)
    cv2.waitKey(0)
    cv2.imwrite('output.png', roi_img)
    cv2.destroyAllWindows()

    peaks1, _ = find_peaks(vt_1, distance=25, height=20)
    peaks2, _ = find_peaks(vt_2, distance=25, height=20)
    peaks3, _ = find_peaks(vt_3, distance=25, height=20)
    peaks4, _ = find_peaks(vt_4, distance=25, height=20)
    peaks5, _ = find_peaks(vt_5, distance=25, height=20)
    peak_list = [len(peaks1), len(peaks2), len(peaks3), len(peaks4), len(peaks5)]

    print(peak_list)

    print(np.argmax(np.bincount(peak_list)))
    plt.plot(peaks1, vt_1[peaks1], "x")
    plt.plot(np.zeros_like(vt_1), "--", color="gray")
    pimg = plt.imread('output.png')

    plt.imshow(np.rot90(pimg), cmap='gray')
    plt.plot(vt_1)

    plt.show()
