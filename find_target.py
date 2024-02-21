# find the cv target in the image captuered by the display

import cv2
import numpy as np
import pyautogui
import time
import pill
#using my custom model, find the target in the image

class FindTargetException(Exception):
    pass

class FindTarget:

    def __init__(self, model):
        self.model = model

    def find_target(self):
        """
        Find the target in the image
        """
        # Capture the screen
        screenshot = pyautogui.screenshot()
        screenshot = np.array(screenshot)
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2RGB)

        # Find the target in the screenshot
        target = self.model.predict(screenshot)

        if target is None:
            raise FindTargetException("Target not found")

        return target