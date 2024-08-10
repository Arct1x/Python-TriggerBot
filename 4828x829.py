import configparser
import ast
import time
import pyautogui
import numpy as np
from PIL import Image
import mss

# Read configuration
config = configparser.ConfigParser()
config.read('config.ini')

# Extract settings from the configuration file
Colorval = ast.literal_eval(config['Settings']['Colorval'])
TolerVal = int(config['Settings']['TolerVal'])
FovVal = int(config['Settings']['FovVal'])
DelVal = float(config['Settings']['DelVal'])
TapVal = float(config['Settings']['TapVal'])
CheckInterval = float(config['Settings'].get('CheckInterval', 0.1))  # Default 0.1 seconds

# Color tolerance adjustment
def is_color_within_tolerance(color, target_color, tolerance):
    return all(abs(c - t) <= tolerance for c, t in zip(color, target_color))

# Capture a screenshot and check for the target color
def check_color():
    with mss.mss() as sct:
        # Define the monitor region
        monitor = {'top': 0, 'left': 0, 'width': FovVal, 'height': FovVal}
        screenshot = sct.grab(monitor)
        img_np = np.array(screenshot)  # Capture and convert to numpy array

        # Create a mask for the target color within tolerance
        target_color = np.array(Colorval)
        lower_bound = target_color - TolerVal
        upper_bound = target_color + TolerVal
        mask = np.all(np.logical_and(lower_bound <= img_np[:, :, :3], img_np[:, :, :3] <= upper_bound), axis=-1)

        # Check if there are any True values in the mask
        if np.any(mask):
            return True
    return False

# Main loop to continuously check for the color and input 'L'
def main():
    while True:
        if check_color():
            pyautogui.press('l')  # Press the 'L' key
            print("kms")
            time.sleep(TapVal)    # Wait for TapVal seconds
        time.sleep(CheckInterval/1000)  # Wait for CheckInterval seconds before the next check

if __name__ == "__main__":
    main()
