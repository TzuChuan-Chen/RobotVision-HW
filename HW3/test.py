import glob
import numpy as np
import cv2
import pylab as pl

# ------------------ Normalised Cross Correlation ------------------ #
def Normalised_Cross_Correlation(roi, target):
    # Normalised Cross Correlation Equation
    cor = np.sum(roi * target)
    nor = np.sqrt( (np.sum(roi ** 2))) * np.sqrt(np.sum(target ** 2))

    return cor / nor

# ----------------------- template matching ----------------------- #
def template_matching(img, target):
    # initial parameter
    height, width, _ = img.shape
    tar_height, tar_width, _ = target.shape
    print(tar_height, tar_width)
    print(height, width)
    (max_Y, max_X) = (0, 0)
    MaxValue = 0

    # Set image, target and result value matrix
    img = np.array(img, dtype="int")
    target = np.array(target, dtype="int")
    NccValue = np.zeros((height-tar_height, width-tar_width))

    # calculate value using filter-kind operation from top-left to bottom-right
    for y in range(0, height-tar_height):
        for x in range(0, width-tar_width):
            # image roi
            roi = img[y : y+tar_height, x : x+tar_width]
            # calculate ncc value
            NccValue[y, x] = Normalised_Cross_Correlation(roi, target)
            # find the most match area
            if NccValue[y, x] > MaxValue:
                MaxValue = NccValue[y, x]
                (max_Y, max_X) = (y, x)

    return (max_X, max_Y)


# -------------------------- main -------------------------- #
if __name__ == '__main__':
    # Read image and target(template)
    circle_path = glob.glob(r'./circle/*')
    cross_path = glob.glob(r'./cross/*')

    pattern_path = glob.glob(r'./pattern/*') 
    image = cv2.imread(circle_path[0])
    target = cv2.imread(pattern_path[1])
    
    height, width, _ = target.shape

    # function
    top_left = template_matching(image, target)
    # draw rectangle on the result region
    cv2.rectangle(image, top_left, (top_left[0] + width, top_left[1] + height), 0, 3)

    # show result
    pl.subplot(111)
    pl.imshow(image)
    pl.title('result')
    pl.show()