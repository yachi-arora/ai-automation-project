import pyautogui
import time


def allow_consent():
    time.sleep(1)
    x, y = pyautogui.locateCenterOnScreen('/Users/yachiarora/Documents/Programming/Pyhton/weather_report.py/Screenshot 2024-10-07 at 17.36.10.png')
    pyautogui.click(x/2, y/2)
    time.sleep(2)

