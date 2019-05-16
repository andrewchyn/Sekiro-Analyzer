
from skimage.measure import compare_ssim as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2
import scipy
import pyautogui
import time
from tkinter import *
from PIL import Image
from pyfirmata import Arduino, util

TASE_TIME = 0.05 #0.05 is highest ive tolerated
TASER_PIN = 12
LED = 13
TASED = 0
TOLERANCE = 0.93
TIME = 0.1

#initializing arduino
board = Arduino("COM3")

#initializing the image we are comparing to
ori = cv2.imread("original.png")
ori = cv2.cvtColor(ori, cv2.COLOR_BGR2GRAY)

def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err
0
def compare_images(imageA, imageB):
    # compute the mean squared error and structural similarity
    # index for the images
    m = mse(imageA, imageB)
    s = ssim(imageA, imageB)

    return(s)

def stopShocking():
    print("Program has started")
    print("___________________\n\n")
    root.destroy()

def compare(imageA, imageB):
    sift = cv2.xfeatures2d.SIFT_create()
    kp_1, desc_1 = sift.detectAndCompute(imageA, None)
    kp_2, desc_2 = sift.detectAndCompute(imageB, None)

    index_params = dict(algorithm=0, trees=5)
    search_params = dict()
    flann = cv2.FlannBasedMatcher(index_params, search_params)

    matches = flann.knnMatch(desc_1, desc_2, k=2)
    print(len(matches))

    result = cv2.drawMatchesKnn(imageA, kp_1, imageB, kp_2, matches, None)
    cv2.imshow("result", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def taser():
    board.digital[LED].write(1)
    board.digital[taser_pin].write(1)

    print("shocking")

    time.sleep(tase_time)

    board.digital[LED].write(0)
    board.digital[taser_pin].write(0)

#start button
root = Tk()
start_button = Button(root, text="START", fg="cyan", bg="grey",command = stopShocking, height = 10, width = 20,)
start_button.pack()
root.mainloop()

while(1):
    #gets screenshots and saves it as current image
    screenshot = pyautogui.screenshot("screenshot.png", region=(981,430,14,174))

    compare = cv2.imread("screenshot.png")
    compare = cv2.cvtColor(compare, cv2.COLOR_BGR2GRAY)

    s = compare_images(ori, compare)
    print("\n%.4f" % s)

    if s > tolerance:
        print("you died")

        if tased == 0:
            taser()
            tased = 1
    else:
        tased = 0

    time.sleep(time_interval)






