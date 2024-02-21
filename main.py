# main access point for the application
import find_target
import action

def arg_parser():
    """
    Parse the command line arguments
    """
    parser = argparse.ArgumentParser(description="Find the target and click on it")
    parser.add_argument("--model", help="The model to use for finding the target", required=True)
    return parser.parse_args()


def __init__(self, model):
    self.model = model

def main():
    find_target.find_target()
    action.click()

if __name__ == "__main__":
    main()