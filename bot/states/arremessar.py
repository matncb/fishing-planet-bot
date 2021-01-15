from pynput.mouse import Button, Controller
mouse = Controller()
import time
import pyautogui

def arremessar(t):
    print("Arremessar...")
    time.sleep(0.2)
    mouse.press(Button.left)
    time.sleep(t)
    mouse.release(Button.left)
    time.sleep(1)
    pyautogui.press('space')
    time.sleep(1)
