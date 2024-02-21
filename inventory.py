import pyautogui
import time

class inventory:
    def __init__(self, model, display):
        self.model = model

    def open_inventory():
        """
        Open the inventory
        """
        if pyautogui.locateOnScreen("inventory.png") is not None:
            pyautogui.press("f1")
            time.sleep(0.5)

    def is_full():
        """
        Check if the inventory is full
        """
        # open inventory, press f1 key
        inventory.open_inventory()

        # get the number of items in the inventory from the display
        items_in_inventory = 0

        if items_in_inventory == 28:
            return True
        else:
            return False
    
    def determine_inventory():
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