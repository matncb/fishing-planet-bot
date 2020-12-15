from pynput.mouse import Button, Controller
import pyautogui
import time

mouse = Controller()


def trocar():
    pyautogui.press('t')
    time.sleep(0.2)
    mouse.position = (1283, 869)
    time.sleep(0.2)
    mouse.click(Button.left)
    time.sleep(0.2)
    mouse.position = (1095, 677)
    time.sleep(0.2)
    mouse.click(Button.left)
    time.sleep(0.5)
    pyautogui.press('esc')
    time.sleep(2)







