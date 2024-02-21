# find the cv target in the image captuered by the display

import cv2
import numpy as np
import pyautogui
import time
import mss
im
#using my custom model, find the target in the image

class DisplayException(Exception):
    pass

class Display:

    def __init__(self, model):
        self.model = model

    def capture(self, debug=False):
        """
        Capture the window
        """

        with mss.mss() as sct:
            monitor = sct.monitors[1]  # Index 1 is usually the primary monitor
            screenshot = sct.grab(monitor)
            img = np.array(screenshot)  # Convert the screenshot to a numpy array

            # Convert the image from BGR (Blue, Green, Red) to RGB
            img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

            # Display the image in a window named 'Screen Capture'
            cv2.imshow('Screen Capture', img)

            # Wait for a key press to close the window
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        return img

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
            raise DisplayException("Target not found")

        return target