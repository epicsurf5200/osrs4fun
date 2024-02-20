# Do actions on the screen

import cv2
import numpy as np
import pyautogui
import time


# click on the screen with the given coordinates
def _click(x, y):
    pyautogui.click(x, y)

