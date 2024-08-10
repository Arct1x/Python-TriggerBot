import configparser
import ast
import time
import pyautogui
from pynput.keyboard import Controller
import numpy as np
from PIL import Image


config = configparser.ConfigParser()
config.read('config.ini')

Colorval = ast.literal_eval(config['Settings']['Colorval'])
TolerVal = int(config['Settings']['TolerVal'])
FovVal = int(config['Settings']['FovVal'])
DelVal = float(config['Settings']['DelVal'])
TapVal = float(config['Settings']['TapVal'])
CheckInterval = float(config['Settings'].get('CheckInterval', 0.1))  

def is_color_within_tolerance(color, target_color, tolerance): # Online resource
    return all(abs(c - t) <= tolerance for c, t in zip(color, target_color))

def get_color_within_fov(x, y, fov): # Online resource
    region = (x - fov // 2, y - fov // 2, fov, fov)
    screenshot = pyautogui.screenshot(region=region)
    img_np = np.array(screenshot)  

    target_color = np.array(Colorval)
    lower_bound = target_color - TolerVal
    upper_bound = target_color + TolerVal

    mask = np.all(np.logical_and(lower_bound <= img_np[:, :, :3], img_np[:, :, :3] <= upper_bound), axis=-1)

    if np.any(mask):
        return True
    return False

def main():
    keyboard = Controller()
    i = 0
    color_detected = False

    while True:
        print("checking")
        x, y = pyautogui.position()
        if get_color_within_fov(x, y, FovVal):
            if not color_detected:
                i += 1
                print(f"Detected color {i} times")
                time.sleep(TapVal/1000)
                color_detected = True
            else:
                keyboard.press('l')
                keyboard.release('l')
                print(f"Detected color {i} times (no delay)")
        else:
            color_detected = False

        time.sleep(CheckInterval)

if __name__ == "__main__":
    main()