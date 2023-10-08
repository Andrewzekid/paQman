import cv2 as cv
import numpy as np
import math
threshold = 0.75

def find_window_coordinates(haystack,*corners):
    """
    Finds the location of the game window by fetching the height and width of it.
    Corners: top right, bottom right, top left corner
    tr br tl
    """
    haystack_img = cv.imread(haystack,cv.IMREAD_UNCHANGED)
    corner_paths = list(corners)
    
    corner_imgs = [cv.imread(corner,cv.IMREAD_UNCHANGED) for corner in corner_paths]
    # print(corner_imgs)
    matches = [cv.matchTemplate(haystack_img,corner_img,cv.TM_CCOEFF_NORMED) for corner_img in corner_imgs]
    print(matches)
    #Get coordinates of corners of game window
    locations = [cv.minMaxLoc(result) for result in matches]

    print(locations)
    for i in range(len(locations)):
        current = locations[i]
        needle_img = corner_imgs[i]

        if current[1] >= threshold:

            print(f"Needle {i} found")
            # top_left = current[3]
            # needle_w = needle_img.shape[1]
            # needle_h = needle_img.shape[0]
            # bottom_right = (top_left[0]+needle_w,top_left[1]+needle_h)

            # cv.rectangle(haystack_img,top_left,bottom_right,color=(0,255,0),thickness=2,lineType=cv.LINE_4)
            # cv.imshow("Result",haystack_img)
            # cv.waitKey()
        else:
            print("Needle not found.")
            raise ValueError("Needle wasnt found!")
        
    tr = locations[1][3]
    br = locations[2][3]
    tl = locations[0][3]
    print(tl)
    print(br)
    window_top = (tl[0],tl[1]+corner_imgs[0].shape[0])
    window_bottom = (br[0],br[1] + corner_imgs[2].shape[0])

    cv.rectangle(haystack_img,window_top,window_bottom,color=(0,255,0),thickness=2,lineType=cv.LINE_4)
    # cv.imshow("Result",haystack_img)
    # cv.waitKey()
    cv.imwrite("result.jpg",haystack_img)

    window = (tl,br)

# def get_window_properties(window):
#     window_height = abs(window[0][1] - br[1])
#     window_width = abs(tl[0] - tr[0])
#     return window_width,window_height

find_window_coordinates("test2.png","headerpartial.png","collapse.png","homeduplicate.png")
import pyautogui, sys
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')