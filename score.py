import numpy as np
import pyautogui
import imutils
import cv2
import keyboard
import time
from matplotlib import pyplot as plt
import pytesseract
from pytesseract import image_to_string
import os
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
DATA_PATH = "data"
def locate_score_bar():
    #Start the game
    play_button = pyautogui.locateCenterOnScreen("play.png")
    pyautogui.moveTo(play_button)
    pyautogui.click(play_button)
    
    time.sleep(3)
    #Move forward and backward, starting the game so the scoreboard is displayed
    pyautogui.press("w")
    pyautogui.press("s")

    #See the location of the score
    time.sleep(2)
    left,top,width,height = pyautogui.locateOnScreen("zero.png",confidence=0.7)
    return left,top,width,height


def create_training_data(left,top,width,height):
    """Given the top left corner of the scorebar, the width and its height, return a screenshot of the scorebar"""
    print("Do your moves!")
    score_tlbr = (left-width*2,top,width*6,height) #road to 20kws
    time.sleep(30)
    for i in range(500,2000):
        filepath = fr"c:\Users\yw347\Downloads\Project +1\data\score{i}.png"
        image = pyautogui.screenshot(filepath,region=score_tlbr)
        print(f"image with filepath {filepath} saved!")
        if keyboard.is_pressed("q"):
            break


    
    
    image = cv2.cvtColor(np.array(image),cv2.COLOR_BGR2GRAY)
    return image

def calculate_score(img):
    """
    Given an image, calculate the current score. 
    """
    thr = cv2.threshold(img,0,255,cv2.THRESH_BINARY_INV)[1]
    print(thr)
    txt = image_to_string(thr,config="--psm 7 -c tessedit_char_whitelist=0123456789")
    return txt



if __name__ == "__main__":
    #Test run
    time.sleep(5)
    print("starting!")
    l,t,w,h = locate_score_bar()
    time.sleep(5)
    print("tracking score!")
    create_training_data(l,t,w,h)
    print(calculate_score(image))