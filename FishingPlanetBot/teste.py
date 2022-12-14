import pyautogui
import time
import pynput
keyboard = pynput.keyboard.Controller()

time.sleep(2)
keyboard.press('t')
time.sleep(0.2)
keyboard.release('t')