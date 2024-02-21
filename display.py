# find the cv target in the image captuered by the display

import cv2
import numpy as np
import pyautogui
import time
import mss
import pygetwindow as gw
import Quartz
from Quartz.CoreGraphics import CGWindowListCopyWindowInfo, kCGNullWindowID, kCGWindowListOptionOnScreenOnly, kCGWindowImageDefault
from AppKit import NSWorkspace, NSScreen

#using my custom model, find the target in the image

class DisplayException(Exception):
    pass

class Display:

    #def __init__(model):
    #    self.model = model

    def capture(debug=False):
        """
        Capture the window
        """

        # Get the list of all windows
        windowList = CGWindowListCopyWindowInfo(kCGWindowListOptionOnScreenOnly, kCGNullWindowID)
        # Find the RuneLite window
        for window in windowList:
            if 'RuneLite - Slotstick' in window.get('kCGWindowName', ''):
                windowID = window['kCGWindowNumber']
                image = Quartz.CGWindowListCreateImage(Quartz.CGRectNull, Quartz.kCGWindowListOptionIncludingWindow, windowID, kCGWindowImageDefault)

                width = Quartz.CGImageGetWidth(image)
                height = Quartz.CGImageGetHeight(image)
                provider = Quartz.CGImageGetDataProvider(image)
                data = Quartz.CGDataProviderCopyData(provider)
                length = Quartz.CFDataGetLength(data)
                buf = bytearray(length)
                Quartz.CFDataGetBytes(data, (0, length), buf)
                bytes_per_row = Quartz.CGImageGetBytesPerRow(image)
                img = np.frombuffer(buf, dtype=np.uint8).reshape((height, bytes_per_row // 4, 4))

                img = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)

                break
        cv2.imshow('RuneLite Capture', img)
        cv2.waitKey(0)
        breakpoint()
        cv2.destroyAllWindows()

    def find_target():
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