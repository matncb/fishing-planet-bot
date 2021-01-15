from pynput.mouse import Button, Controller
import time
import pyautogui
from pynput.keyboard import Key, Listener

mouse = Controller()

def config(n):
    for i in range(5):
        pyautogui.press('k')
        time.sleep(0.1)
    for i in range(n):
        pyautogui.press('l')
        time.sleep(0.1)
    

def twiching():
    print("Pescar(twiching)...")
    mouse.press(Button.left)
    time.sleep(0.5)
    mouse.press(Button.right)
    time.sleep(0.25)
    mouse.release(Button.left)
    time.sleep(0.25)
    mouse.release(Button.right)
    time.sleep(0.2)

def stopgo():
    print("Pescar(stopgo)...")
    mouse.press(Button.left)
    time.sleep(2)
    mouse.release(Button.left)
    time.sleep(0.7)
    







