# main access point for the application
from display import Display
import action
import argparse
import inventory
import cv2
import time

def arg_parser() -> argparse.Namespace:
    """Parse the command line arguments

    Returns:
        parsed_args ['list']: Arguments parsed from the command line
    """
    parser = argparse.ArgumentParser(prog= "python main.py", description="Just for fun OSRS bot")
    parser.add_argument("-m", "--mode", help="Mode of the bot", required=True)
    parser.add_argument("-t", "--target", help="Target to interact/attack")
    parser.add_argument("-d", "--debug", help="Set to debug mode", action="store_true")
    parsed_args = parser.parse_args()
    return parsed_args


def __init__(self, model, display):
    self.model = model
    self.display = display

def main(args):
    timeout = time.time() + 30
    while time.time() < timeout:
        img, window_position = Display.capture()
        if args.debug:
            cv2.imshow('RuneLite Capture', img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                    cv2.destroyAllWindows()
                    return

        if args.mode == "attack":
            target_coord = Display.FindTarget(args.target)
            action.attack()

        if args.mode == "chop_trees":
            while inventory.is_full() == False:
                target_coord = Display.FindTarget(args.target)
                action.chop_trees()

if __name__ == "__main__":
    args = arg_parser()
    main(args)