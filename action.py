# Do actions on the screen

import numpy as np
import pyautogui
import time

class ActionException(Exception):
    pass
class Action:
    def __init__(self, model):
        self.model = model
    # click on the screen with the given coordinates
    def _click(x, y):
        pyautogui.click(x, y)

    def dump_inventory():
        """
        Dump the inventory to the ground
        """ 
        # open inventory, press f1 key
        pyautogui.press("f1")
        time.sleep(0.5)

        # get the number of items in the inventory from the display
        items_in_inventory = 0
        
        while items_in_inventory > 0:
            # drop the item
            pyautogui.dragTo(x, y, duration=0.5)
            time.sleep(0.5)




