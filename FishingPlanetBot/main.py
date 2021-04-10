from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
from pynput.mouse import Button, Controller
mouse = Controller()

#starting

print("Welcome to the Fishing Planet Bot!")
print("")
print("Select your fishing style:")
print("Enter 0 for lure fishing")
print("Enter 1 for bottom or float fishing")
print("")

style = int(input("Enter your style: "))

print("")

print("Enter your CAST_LENTH: ")
print("Enter 0 if you want to go default (full cast)")
print("")

CAST_LENGTH = int(input("Enter the CAST_LENGTH: "))

print("")
print("[STATUS] Starting...")

#vars
FULL_CASTING_TIME = 1.9
FULL_CASTING_LENGTH = 81

if CAST_LENGTH  == 0:
    CAST_LENGTH = FULL_CASTING_LENGTH
    
CASTING_TIME = (CAST_LENGTH * (FULL_CASTING_TIME - 0.9))/FULL_CASTING_LENGTH + 0.9

keep_button_path = 'keep_button.png'
release_button_path = 'release_button.png'
extend_button_path = 'extend_button.png'
next_morning_button_path = 'next_morning_button.png'

#functions
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def cast(CASTING_TIME):
    mouse.press(Button.left)
    time.sleep(CASTING_TIME)
    mouse.release(Button.left)
    
def reel():
    mouse.press(Button.right)
    mouse.press(Button.left)
    time.sleep(1)
    mouse.release(Button.left)
    mouse.release(Button.right)

def hooked():
    #width, height = pic.size
    #pyautogui.displayMousePosition
    
    pic = pyautogui.screenshot(region=(2249, 794, 43, 6))   # (x1,y1) (x2, y2)  ----->  (x1, y1, x2-x1, y2-y1)
    r,g,b = pic.getpixel((20, 3))

    if b in range(185,200):
        return True
    else:
        return False

def keep_fish():
     mouse.position = (pyautogui.locateCenterOnScreen(keep_button_path, confidence=0.8))
     time.sleep(0.1)
     mouse.press(Button.left)
     time.sleep(0.2)
     mouse.release(Button.left)
     time.sleep(0.1)

def release_fish():
    mouse.position = (pyautogui.locateCenterOnScreen(release_button_path, confidence=0.8))
    time.sleep(0.1)
    mouse.press(Button.left)
    time.sleep(0.2)
    mouse.release(Button.left)
    time.sleep(0.1)

def extend_day():
    mouse.position = (pyautogui.locateCenterOnScreen(extend_button_path, confidence=0.8))
    time.sleep(0.1)
    mouse.press(Button.left)
    time.sleep(0.2)
    mouse.release(Button.left)
    time.sleep(0.5)
    pyautogui.press('esc')
    time.sleep(0.5)

def next_day():
    pyautogui.press('t')
    time.sleep(0.2)
    mouse.position = (pyautogui.locateCenterOnScreen(next_morning_button_path, confidence=0.8))
    time.sleep(0.1)
    mouse.press(Button.left)
    time.sleep(0.2)
    mouse.release(Button.left)
    time.sleep(0.5)
    extend_day()


time.sleep(2)
if style == 1:
    while True:
        time.sleep(1)
        cast(CASTING_TIME)
        time.sleep(3)
        
        while hooked() == False:
            if keyboard.is_pressed('q') == True:
                break
        while hooked() == True:
            if keyboard.is_pressed('q') == True:
                break
            reel()
        
        time.sleep(2)

        if pyautogui.locateOnScreen(keep_button_path, confidence=0.8) != None:
            keep_fish()
            time.sleep(1)

            if pyautogui.locateOnScreen(extend_button_path, confidence=0.8) != None:
                extend_day()
        else:
            release_fish()
            time.sleep(1)

            if pyautogui.locateOnScreen(extend_button_path, confidence=0.8) != None:
                extend_day()
            else:
                next_day()
        
    
else:
    pass

