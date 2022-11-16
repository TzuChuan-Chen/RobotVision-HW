import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from scipy.signal import argrelextrema
if __name__ == '__main__':
    # cv2.namedWindow('windows', cv2.WINDOW_NORMAL)

    img = cv2.imread('HW_Image/20070907_164013_Cell_79.png', cv2.IMREAD_GRAYSCALE)
    gray_img = np.copy(img)

    # 使用 sobel 算子
    # 第一個參數是要作用的影像
    # 第二個參數是影像深度 使用 16 可避免 overflow 問題
    # 第三 & 四個參數是控制是否使用兩種面罩的參數
    # 第五個參數是 mask size
    kernel_size = 3
    # x = cv2.Sobel(gray_img, cv2.CV_16S, 1, 0, ksize=kernel_size)
    #y = cv2.Sobel(gray_img, cv2.CV_16S, 0, 1, ksize=kernel_size)

    # 轉換為影像原本儲存的格式 uint8
    # absX = cv2.convertScaleAbs(x)
    #dst = cv2.convertScaleAbs(y)
    dst = cv2.medianBlur(img, 9)
    dst = cv2.equalizeHist(dst)

    # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))
    # dst = cv2.morphologyEx(dst, cv2.MORPH_CLOSE, kernel, iterations=10)
    # image_copy = closing.copy()
    # diff = np.diff(vt_sp)
    # print(diff)
    # print(np.where(diff > 50))
    vt_ref = dst[:, 500]
    vt_head = dst[:, 500]
    print(np.where(vt_ref < 90)[0][0])
    start_idx = np.where(vt_ref < 90)[0][0]
    print(np.where(vt_ref[start_idx+4000:] < 30))
    end_idx = np.where(vt_ref[start_idx+4000:] < 30)[0][0]
    myl_top = np.zeros(1000, dtype=int)
    diff_top = np.zeros(1000, dtype=int)
    tmp = 0
    myl_botton = np.zeros(6000, dtype=int)
    mean_bot = np.zeros(10001, dtype=int)
    for i in range(10000, start_idx, -1):
        ls2 = vt_head[i:i-5:-1]
        # myl_botton[i] = np.min(ls2)
        mean_bot[i] = np.sum(ls2)
        if mean_bot[i] < 250:
            if abs(tmp-i) > 20:
                print(mean_bot[i], i)
            tmp = i

        # print(ls2)
    # print(mean_bot[4870:4890])
    # print(np.where(diff_bot<90))
    # print(myl_botton[2900:3000])
    # print(np.where(myl_botton < 20)[0][0])


    # print(vt_ref)
    # # print(np.where(vt_tail < 20))
    # start_idx = np.where(vt_head > 200)[0][0]
    # print(start_idx)
    # vt_tail = dst[start_idx:, 500]
    # end = np.where(vt_tail < 10)[0][0]
    # print(end)
    # # end = np.where(vt_tail < 35)[0][-1]

    roi_img = dst[start_idx-50:end_idx+start_idx+100]
    vt_1 = roi_img[:, 50]
    vt_2 = roi_img[:, 200]
    vt_3 = roi_img[:, 500]
    vt_4 = roi_img[:, 800]
    vt_5 = roi_img[:, 950]
    # cv2.imshow("windows", closing)
    # cv2.waitKey(0)
    cv2.imwrite('output.png', roi_img)
    # cv2.destroyAllWindows()

    peaks1, _ = find_peaks(vt_1, height=20, width=5, distance=5)
    peaks2, _ = find_peaks(vt_2, height=20, width=5, distance=5)
    peaks3, _ = find_peaks(vt_3, height=20, width=5, distance=5)
    peaks4, _ = find_peaks(vt_4, height=20, width=5, distance=5)
    peaks5, _ = find_peaks(vt_5, height=20, width=5, distance=5)
    peak_list = [len(peaks1), len(peaks2), len(peaks3), len(peaks4), len(peaks5)]

    print(peak_list)
    print(round(np.mean(peak_list)))
    # print(np.argmax(np.bincount(peak_list)))
    plt.imshow(dst, cmap='gray')
    plt.show()
    plt.plot(peaks3, vt_3[peaks3], "x")
    plt.plot(np.zeros_like(vt_3), "--", color="gray")
    pimg = plt.imread('output.png')

    plt.imshow(np.rot90(pimg), cmap='gray')
    plt.plot(vt_3)

    plt.show()
