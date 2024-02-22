# find the cv target in the image captuered by the display

import cv2
import numpy as np
import pyautogui
import pygetwindow as gw
import Quartz
from Quartz.CoreGraphics import CGWindowListCopyWindowInfo, kCGNullWindowID, kCGWindowListOptionOnScreenOnly, kCGWindowImageDefault
from AppKit import NSWorkspace, NSScreen
import subprocess
import time

#using my custom model, find the target in the image

class DisplayException(Exception):
    pass

class Display:

    #def __init__(model):
    #    self.model = model
    def raise_window(window_title):
        """
        Raise the window to the top using AppleScript
        """
        script = f'''
        tell application "System Events"
            set frontmost of the first process whose name is "{window_title}" to true
        end tell
        '''
        subprocess.run(["osascript", "-e", script])
        time.sleep(1)

    def capture(debug=False):
        """
        Capture the window
        """
        border_offset_x = 65
        border_offset_y = 80

        # Get the list of all windows
        windowList = CGWindowListCopyWindowInfo(kCGWindowListOptionOnScreenOnly, kCGNullWindowID)
        # Find the RuneLite window
        for window in windowList:
            if 'RuneLite - Slotstick' in window.get('kCGWindowName', ''):

                # capture the window
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
                img = img[border_offset_y:-border_offset_y, border_offset_x:-border_offset_x, :]

                img = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)
                # get the window position
                window_position = window['kCGWindowBounds']
                break
        return img, window

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