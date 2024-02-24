import argparse
import cv2
import time
from display import Display
import action
from inventory import Inventory
import yaml

class Main:
    def __init__(self):
        # read the config file
        with open("config.yaml", "r") as file:
            config = yaml.load(file, Loader=yaml.FullLoader)
            self.inventory = config["inventory"]
        # setup the coordinates for the inventory
        for inventory in self.inventory:
            self.inventory[inventory]["coord_2"] = (
                [self.inventory[inventory]["coord_1"][0]+ self.inventory[inventory]["width"], 
                 self.inventory[inventory]["coord_1"][1]+ self.inventory[inventory]["height"]]
            )
        self.color = (0, 255, 0)
        self.thickness = 2
        self.debug = False
        self.debug_img = None
        # self.model = model
        # self.display = display
        self.img = None
        self.window_position = None

    @staticmethod
    def arg_parser() -> argparse.Namespace:
        """Parse the command line arguments

        Returns:
            argparse.Namespace: Arguments parsed from the command line
        """
        parser = argparse.ArgumentParser(prog="python main.py", description="Just for fun OSRS bot")
        parser.add_argument("-m", "--mode", help="Mode of the bot", required=True)
        parser.add_argument("-t", "--target", help="Target to interact/attack")
        parser.add_argument("-d", "--debug", help="Set to debug mode", action="store_true")
        return parser.parse_args()

    def run(self, args):
        """Run the bot"""

        timeout = time.time() + 60
        self.img, self.window = Display.capture()
        self.debug = args.debug

        if args.debug:
            self.debug_img = Inventory.draw_inventory(self)
            Inventory.determine_inventory(self)
            #cv2.imshow('RuneLite Capture', self.img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                return

        while time.time() < timeout:
            #self.img, self.window = Display.capture()
            #Inventory.open_inventory()
            #time.sleep(5)
            #Inventory.close_inventory()


            if args.mode == "attack":
                target_coord = Display.FindTarget(args.target)
                action.attack()

            if args.mode == "chop_trees":
                while not Inventory.is_full():
                    target_coord = Display.FindTarget(args.target)
                    action.chop_trees()

# Main access point for the application
if __name__ == "__main__":
    args = Main.arg_parser()  # Call the static method to parse arguments
    app = Main()  # Create an instance of Main
    app.run(args)  # Call the run method with the parsed arguments
