import argparse
import pyautogui
from display import Display
from PIL import Image

def capture_screen(region):
    Display.capture(region=region)
    screenshot = pyautogui.screenshot()
    image = screenshot.crop(region)
    return image

def save_image(image, output_dir):
    image.save(output_dir)

def main():
    parser = argparse.ArgumentParser(description='Screen Capture Utility')
    parser.add_argument('-o', '--output', type=str, help='Output directory')
    args = parser.parse_args()

    # Get region coordinates using GUI
    print('Please select the region to capture...')
    region = pyautogui.locateOnScreen('select_region.png')
    if region is None:
        print('Region not found. Exiting...')
        return

    # Capture and save the image
    captured_image = capture_screen(region)
    save_image(captured_image, args.output)

    print('Image captured and saved successfully!')

if __name__ == '__main__':
    main()