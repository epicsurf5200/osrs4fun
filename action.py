# Do actions on the screen

import numpy as np
import pyautogui
import time
from inventory import Inventory

class ActionException(Exception):
    pass
class Action:
    def __init__(self, model):
        self.model = model
    def _coord_randomizer(coord):
        """
        Randomize the coordinates with a random +- 5 pixel offset
        """
        x = coord[0]
        y = coord[1]
        coord[0] = x + np.random.randint(-5, 5)
        coord[1] = y + np.random.randint(-5, 5)
        return (coord)
        
    def _click(coord= None):
        if coord:
            Action._coord_randomizer(coord)
            x = coord[0]
            y = coord[1]
            pyautogui.click(x, y)
        else:
            pyautogui.click()
        time.sleep(0.25)

    def _right_click(coord= None):
        if coord:
            Action._coord_randomizer(coord)
            x = coord[0]
            y = coord[1]
            pyautogui.rightClick(x, y)
        else:
            pyautogui.click
        time.sleep(0.25)

    def _move_to(coord):
        Action._coord_randomizer(coord)
        x = coord[0]
        y = coord[1]
        pyautogui.moveTo(x, y)
        time.sleep(0.25)

    def drop_item(self, item=None, coord=None):
        """
        Drop the item from the inventory
        """
        # open inventory
        Inventory.open_inventory()

        if coord:
            # drop the item
            pyautogui.dragTo(x, y, duration=0.5)
            time.sleep(0.5)
            Inventory.determine_inventory(self)

        elif item:
            # locate the item
            for item in self.inventory:
                if item == item:
                    # locate the center to click
                    x, y = self.inventory[item]["cnter"]  
                    # drop the item
                    Action.right_click(x, y)
                    # locate the drop button
                    Action._move_to(coord=drop_coord)
                    Action._click(x, y)
                    Inventory.determine_inventory(self)
                    return
        else:
            raise ActionException(f"Item {item} not found in the inventory")
        
    def dump_inventory(self):
        """
        Dump the inventory to the ground
        """ 
        Inventory.open_inventory()
        for item in self.inventory:
            if self.inventory[item]["item"]: # only drop known items
                Action.drop_item(coord=self.inventory[item]["center"])
        Inventory.determine_inventory


    def attack(self, target_coord):
        # TODO
        pass

    def light_logs(self, target_coord):

        # determine which invnetory spot has the tinderbox
        for item in self.inventory:
            if self.inventory[item]["item"] and self.inventory[item]["name"] == "tinderbox":
                tinderbox = self.inventory[item]["center"]
                break
        else:
            raise ActionException("Tinderbox not found in the inventory")

        # Light the logs        
        for item in self.inventory:
            if self.inventory[item]["item"] and self.inventory[item]["name"] == "logs":
                timeout = time.time() + 60 # timeout after 30 seconds of trying to light the log
                max_timeout = time.time() + 60 # timeout after 30 seconds of trying to light the log
                while self.inventory[item]["item"] == "logs":
                    Action._click(tinderbox)
                    Action._click(self.inventory[item]["center"])
                    Inventory.determine_inventory(self)
                    if time.time() > timeout:
                        # reorient the player to the logs
                        # TODO
                        pass
                    if time.time() > max_timeout:
                        raise ActionException("Unable to light the logs")


