# main access point for the application
import action
import argparse
import inventory

def arg_parser() -> argparse.Namespace:
    """_summary_

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

def main(mode: str, target: str = None):
    display.Display.capture()
    breakpoint()
    if mode == "attack":
        target_coord = find_target.FindTarget(target)
        action.attack()

    if mode == "chop_trees":
        while inventory.is_full() == False:
            target_coord = find_target.FindTarget(target)
            action.chop_trees()


if __name__ == "__main__":
    args = arg_parser()
    main()