from pyautogui import *
import pyautogui
import time
import keyboard
import random
import numpy as np
import win32api, win32con
from pynput.mouse import Button, Controller
mouse = Controller()

#starting

print("Welcome to the Fishing Planet Bot!")
print("")
print("Select your fishing style:")
print("Enter 1 for lure fishing")
print("Enter 2 for bottom or float fishing")
print("")

style = int(input("Enter your style: "))

print("")

if style == 1:
    print("Select the lure work: ")
    print("Enter 1 for stop and go")
    print("Enter 2 for twiching or popping")
    print("")
    work = int(input("Enter the work: "))
    print("")

print("Enter your CAST_LENTH: ")
print("Enter 0 if you want to go default (full cast)")
print("")

CAST_LENGTH = int(input("Enter the CAST_LENGTH: "))

print("")
print("[STATUS] Starting...")
print("")

#vars
FULL_CASTING_TIME = 1.9
FULL_CASTING_LENGTH = 51
#REGION = (2249, 794, 43, 6)
#BOUNDS = (2180, 955, 2185, 979)
REGION = (1610, 793, (1654-1610), (800-793))    # (x1,y1) (x2, y2)  ----->  (x1, y1, x2-x1, y2-y1)
BOUNDS = (1540, 955, 1545, 979)                 # left top right bot

if CAST_LENGTH  == 0:
    CAST_LENGTH = FULL_CASTING_LENGTH

CASTING_TIME = (CAST_LENGTH * (FULL_CASTING_TIME - 0.9))/FULL_CASTING_LENGTH + 0.9


keep_button_path = 'keep_button.png'
black_keep_button_path = 'black_keep_button.png'
release_button_path = 'release_button.png'
extend_button_path = 'extend_button.png'
next_morning_button_path = 'next_morning_button.png'
close_button_path = 'close_button.png'
gray_close_button_path = 'gray_close_button.png'
ok_button_path = 'ok_button.png'

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

    pic = pyautogui.screenshot(region=REGION)   # (x1,y1) (x2, y2)  ----->  (x1, y1, x2-x1, y2-y1)

    r,g,b = pic.getpixel((20, 3))

    if b in range(185,200):
        print("[STATUS] Fish on !!!")
        print("")
        return True
        
    else:
        #print("Não fisgou !!!")
        return False

def keep_fish():
    pyautogui.press('space')
    time.sleep(0.5)

def release_fish():
    pyautogui.press('backspace')
    time.sleep(0.5)

def extend_day():
    mouse.position = (pyautogui.locateCenterOnScreen(extend_button_path, confidence=0.8))
    time.sleep(0.2)
    mouse.press(Button.left)
    time.sleep(0.2)
    mouse.release(Button.left)
    time.sleep(0.5)
    pyautogui.press('esc')
    time.sleep(0.5)

def next_day():
    pyautogui.press('t')
    time.sleep(0.5)
    mouse.position = (pyautogui.locateCenterOnScreen(next_morning_button_path, confidence=0.8))
    time.sleep(0.2)
    mouse.press(Button.left)
    time.sleep(0.2)
    mouse.release(Button.left)
    time.sleep(0.5)
    extend_day()

def stopgo():
    mouse.press(Button.left)
    time.sleep(2)
    mouse.release(Button.left)
    time.sleep(0.7) 

def twiching():
    mouse.press(Button.left)
    time.sleep(2)
    mouse.release(Button.left)
    time.sleep(0.1)
    mouse.press(Button.right)
    time.sleep(0.7)
    mouse.release(Button.right)
    time.sleep(0.1)

def is_zero():
    img = pyautogui.screenshot()
    data = np.array(img)
    bounds= BOUNDS
    
                       
    offset_x= 31     # 1771 - 1740
    segment=data[bounds[1]:bounds[3], bounds[0]:bounds[2]]
    if (segment== (247, 247, 247)).all():
        return True
    else:
        return False    

def close():
    mouse.position = pyautogui.locateCenterOnScreen(close_button_path, confidence=0.8)
    time.sleep(0.2)
    mouse.press(Button.left)
    time.sleep(0.2)
    mouse.release(Button.left)
    time.sleep(0.5)

def gray_close():
    mouse.position = pyautogui.locateCenterOnScreen(gray_close_button_path, confidence=0.8)
    time.sleep(0.2)
    mouse.press(Button.left)
    time.sleep(0.2)
    mouse.release(Button.left)
    time.sleep(0.5)

def achiv():
    if pyautogui.locateOnScreen(close_button_path, confidence=0.8) != None:
        close()
        time.sleep(2)
    if pyautogui.locateOnScreen(gray_close_button_path, confidence=0.8) != None:
        gray_close()
        time.sleep(2)

def ok():
    mouse.position = pyautogui.locateCenterOnScreen(ok_button_path, confidence=0.8)
    time.sleep(0.2)
    mouse.press(Button.left)
    time.sleep(0.2)
    mouse.release(Button.left)
    time.sleep(0.5)

def level():
    if pyautogui.locateOnScreen(ok_button_path, confidence=0.8) != None:
        ok()
        time.sleep(2)

def verification():
    if pyautogui.locateOnScreen(keep_button_path, confidence=0.8) != None:
        keep_fish()
        time.sleep(3)

    elif pyautogui.locateOnScreen(black_keep_button_path, confidence=0.8) != None:
        release_fish()
        time.sleep(3)

        level()
        achiv()

        if pyautogui.locateOnScreen(extend_button_path, confidence=0.8) != None:
            extend_day()
            time.sleep(3)
            achiv()
        else:
            next_day()
            time.sleep(3)
            achiv()

    level()
    achiv()

    if pyautogui.locateOnScreen(extend_button_path, confidence=0.8) != None:
        extend_day()
        time.sleep(3)
        achiv()

time.sleep(2)

if (style == 2): 
    print("Style---> 2:Bottom/float...")
    time.sleep(1)
    cast(CASTING_TIME)
    time.sleep(4)

    while True:
        time.sleep(0.2) 

        if hooked() == True:
            time.sleep(1)
            while is_zero() == False:
                reel()
            time.sleep(3)
            verification()
            cast(CASTING_TIME)
            time.sleep(4)
    
elif (style == 1): #artificial
    print("Style---> 2:Artificial...")
    time.sleep(1)

    while True:
        if is_zero():
            print("[STATUS] Finished reeling.")
            print("")
            time.sleep(3)
            verification()
            mouse.release(Button.right)
            time.sleep(0.2)        
            cast(CASTING_TIME)
            time.sleep(4) 
          
        if work == 1:
            stopgo()
        else:
            twiching()

        if hooked() == True:
            while is_zero() == False:
                reel()
