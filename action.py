# Do actions on the screen

import cv2
import numpy as np
import pyautogui
import time

class ActionException(Exception):
class Action:

    # click on the screen with the given coordinates
    def _click(x, y):
        pyautogui.click(x, y)

    def dump_inventory():
        """
        Dump the inventory to the ground
        """    




