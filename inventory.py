import pyautogui
import time
import cv2 as cv
import numpy as np
from display import Display

class Inventory:
    def __init__(self, model, display):
        self.model = model

    def close_inventory():
        """
        Open the inventory
        """
        print("Closing inventory...")
        try:
            pyautogui.locateOnScreen("images/inventory.png")
        except:
            print("Inventory is already closed")
        else:
            print("Inventory is open")
            pyautogui.press("f1")
            print("Inventory closed")
        time.sleep(0.5)

    def open_inventory():
        """
        Open the inventory
        """
        # raise the window to the top
        Display.raise_window("RuneLite")
        print("Opening inventory...")
        try:
            pyautogui.locateOnScreen("images/inventory.png")
        except:
            print("Inventory is closed")
            pyautogui.press("f1")
            print("Inventory opened")
        else:
            print("Inventory is already open")
        time.sleep(0.5)

    def is_full(self):
        """
        Check if the inventory is full
        """
        # open inventory, press f1 key
        Inventory.open_inventory()

        # get the number of items in the inventory from the display
        items_in_inventory = 0

        if items_in_inventory == 28:
            return True
        else:
            return False
    def draw_inventory(self):
        """
        Draw the inventory on the screen
        """
        # open inventory
        Inventory.open_inventory()
        for inventory in self.inventory:
            cv.rectangle(self.debug_img, self.inventory[inventory]["coord_1"], self.inventory[inventory]["coord_2"], self.color, self.thickness)
        return self.img

    def determine_inventory(self):
        """Determine the items in the inventory"""
        threshold = 0.5
        # open inventory
        Inventory.open_inventory()
        template = cv.imread('images/empty_inventory.png')

        print("Detecting items in the inventory")
        # iterate through the inventory slots and determine if there is an item, or if it is empty
        for slot in self.inventory:
            #crop the image to the inventory slot
            x1, y1 = self.inventory[slot]["coord_1"]
            x2, y2 = self.inventory[slot]["coord_2"]
            cropped_img = self.img[y1:y2, x1:x2]

            if self.debug["INVENTORY"]:
                cv.imshow('Inventory Slot', cropped_img)
                cv.imshow('Template', template)
                cv.waitKey(0)

            result = cv.matchTemplate(cropped_img, template, cv.TM_CCOEFF_NORMED)
            if np.any(result >= threshold):
                self.inventory[slot]["item"] = False
                print(f"Slot {slot} is empty")
            else:
                self.inventory[slot]["item"] = True
                print(f"Slot {slot} contains an item")

    def drop_item(item):
        """
        Drop the item from the inventory
        """
        # open inventory
        Inventory.open_inventory()

        # drop the item
        pyautogui.rightClick(x, y)
        time.sleep(0.5)

    def drop_all_items():
        """
        Dump the inventory to the ground
        """ 
        # open inventory, press f1 key
        Inventory.open_inventory()

        # get the number of items in the inventory from the display
        items_in_inventory = 0

        while items_in_inventory > 0:
            # drop the item
            pyautogui.dragTo(x, y, duration=0.5)
            time.sleep(0.5)