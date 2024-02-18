# use the display to click on the screen when an object is detected

import cv2
import numpy as np
import pyautogui
import time


# click on the screen with the given coordinates
def click(x, y):
    pyautogui.click(x, y)

