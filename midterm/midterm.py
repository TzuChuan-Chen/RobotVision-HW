import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks




if __name__ == '__main__':
    #cv2.namedWindow('windows', cv2.WINDOW_NORMAL)

    img = cv2.imread('HW_Image/20070907_170041_Cell_114.png', cv2.IMREAD_GRAYSCALE)
    gray_img = np.copy(img)
    dst = cv2.medianBlur(gray_img, 7)
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
    # dst = cv2.convertScaleAbs(y)

    # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))
    # closing = cv2.morphologyEx(dst, cv2.MORPH_CLOSE, kernel, iterations=5)
    # image_copy = closing.copy()
    # diff = np.diff(vt_sp)
    # print(diff)
    # print(np.where(diff > 50))
    vt_ref = dst[:, 500]
    vt_head = dst[:, 500]
    plt.plot(vt_ref, color="red")
    plt.imshow(np.rot90(dst), cmap='gray')
    # plt.imshow(closing, cmap='gray')
    plt.show()

    myl_top = np.zeros(1000, dtype=int)
    for i in range(1000):
        ls = vt_head[i:i+5]
        myl_top[i] = np.min(ls)

    # print(np.where(myl < 60)[0][0])
    start_idx = np.where(myl_top < 60)[0][0]

    myl_botton = np.zeros(5000, dtype=int)
    for i in range(5000):
        ls2 = vt_head[start_idx+i:start_idx+i+5]
        myl_botton[i] = np.min(ls2)
        #print(ls2)
    print(myl_botton[2900:3000])
    print(np.where(myl_botton < 20)[0][0])
    end_idx = np.where(myl_botton < 20)[0][0]

    # print(vt_ref)
    # # print(np.where(vt_tail < 20))
    # start_idx = np.where(vt_head > 200)[0][0]
    # print(start_idx)
    # vt_tail = dst[start_idx:, 500]
    # end = np.where(vt_tail < 10)[0][0]
    # print(end)
    # # end = np.where(vt_tail < 35)[0][-1]
    roi_img = dst[start_idx:start_idx+end_idx+50, :]
    vt_1 = roi_img[:, 50]
    vt_2 = roi_img[:, 200]
    vt_3 = roi_img[:, 500]
    vt_4 = roi_img[:, 800]
    vt_5 = roi_img[:, 950]
    plt.imshow(roi_img, cmap='gray')
    plt.show()
    # cv2.imshow("windows", closing)
    # cv2.waitKey(0)
    cv2.imwrite('output.png', roi_img)
    # cv2.destroyAllWindows()

    peaks1, _ = find_peaks(vt_1, height=40, width=5)
    peaks2, _ = find_peaks(vt_2, height=40, width=5)
    peaks3, _ = find_peaks(vt_3, height=40, width=5)
    peaks4, _ = find_peaks(vt_4, height=40, width=5)
    peaks5, _ = find_peaks(vt_5, height=40, width=5)
    peak_list = [len(peaks1), len(peaks2), len(peaks3), len(peaks4), len(peaks5)]

    print(peak_list)

    print(np.argmax(np.bincount(peak_list)))

    plt.plot(peaks1, vt_1[peaks1], "x")
    plt.plot(np.zeros_like(vt_1), "--", color="gray")
    pimg = plt.imread('output.png')

    plt.imshow(np.rot90(pimg), cmap='gray')
    plt.plot(vt_1)

    plt.show()
