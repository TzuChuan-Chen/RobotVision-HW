import cv2
from matplotlib import pyplot as plt
import time
import glob

def template_matching(img, target):
    # convert to grayscale image
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    target = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)
    img = cv2.medianBlur(img, 15)
    # copy image in order to compare with different method
    img2 = img.copy()
    
    w, h = target.shape[::-1]

    # All the 6 methods for comparison in a list
    methods = eval('cv2.TM_CCOEFF_NORMED')

    # do template matching with different method
    img = img2.copy()

    # Apply template Matching
    res = cv2.matchTemplate(img,target,methods)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    # draw the match region
    cv2.rectangle(img, top_left, bottom_right, (255, 0, 0), 2)
    return img


# -------------------------- main -------------------------- #
if __name__ == '__main__':
    # Read image and target(template)
    circle_path = glob.glob(r'./circle/*')
    cross_path = glob.glob(r'./cross/*')

    pattern_path = glob.glob(r'./pattern/*') 
    '''
    ['./pattern/Template_circle.bmp', './pattern/Template_BorderCross.bmp', 
     './pattern/Template_BorderCircle.bmp', './pattern/Template_cross.bmp']
    '''

    ### Image = circle, Template = Template_BorderCross.bmp
    for i in circle_path:
        image = cv2.imread(i)
        target = cv2.imread(pattern_path[1])
        start = time.time()
        img = template_matching(image, target)
        end = time.time()
        print("執行時間：%f 秒" % (end - start))
        cv2.imshow('Template_circle Matching', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    for i in cross_path:
        image = cv2.imread(i)
        target = cv2.imread(pattern_path[2])
        start = time.time()
        img = template_matching(image, target)
        end = time.time()
        print("執行時間：%f 秒" % (end - start))
        cv2.imshow('Template_cross Matching', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    for i in circle_path:
        image = cv2.imread(i)
        target = cv2.imread(pattern_path[0])
        start = time.time()
        img = template_matching(image, target)
        end = time.time()
        print("執行時間：%f 秒" % (end - start))
        cv2.imshow('Template_cross Matching', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    for i in cross_path:
        image = cv2.imread(i)
        target = cv2.imread(pattern_path[3])
        start = time.time()
        img = template_matching(image, target)
        end = time.time()
        print("執行時間：%f 秒" % (end - start))
        cv2.imshow('Template_cross Matching', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # # show the result
    # plt.subplot(121),plt.imshow(res,cmap = 'gray')
    # plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    # plt.subplot(122),plt.imshow(img,cmap = 'gray')
    # plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    # plt.suptitle(methods)

    # plt.show()
    