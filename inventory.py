import pyautogui
import time
import cv2 as cv

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
        self.open_inventory()

        # get the number of items in the inventory from the display
        items_in_inventory = 0

        if items_in_inventory == 28:
            return True
        else:
            return False
    def draw_inventory(self, img, inventory_slots):
        """
        Draw the inventory on the screen
        """
        # open inventory
        self.open_inventory()

        for inventory_slot in inventory_slots:
            cv.rectangle(img, inventory_slot["coordinates"], inventory_slot["coordinates"]+10, color, thickness)

            cv.draw_rectangle(img, inventory_slot, (0, 255, 0))
            pyautogui.moveTo(x, y)
            pyautogui.dragTo(x, y, duration=0.5)
            time.sleep(0.5)

        # draw the inventory
        for x in range(4):
            for y in range(7):
                pyautogui.moveTo(x, y)
                pyautogui.dragTo(x, y, duration=0.5)
                time.sleep(0.5)
    def determine_inventory(self):
        """Determine the items in the inventory"""
        # open inventory
        inventory.open_inventory()
        print("detecting items in the inventory")
        items_in_inventory = {}
        for x in range(4):
            for y in range(7):
                items_in_inventory[item]
            # get the item
            item = pyautogui.locateOnScreen("item.png")
            if item is not None:
                items_in_inventory[f"item_{i}"] = item

        return items_in_inventory
    
    def drop_item(item):
        """
        Drop the item from the inventory
        """
        # open inventory
        inventory.open_inventory()

        # drop the item
        pyautogui.rightClick(x, y)
        time.sleep(0.5)

    def drop_all_items():
        """
        Dump the inventory to the ground
        """ 
        # open inventory, press f1 key
        inventory.open_inventory()

        # get the number of items in the inventory from the display
        items_in_inventory = 0

        while items_in_inventory > 0:
            # drop the item
            pyautogui.dragTo(x, y, duration=0.5)
            time.sleep(0.5)