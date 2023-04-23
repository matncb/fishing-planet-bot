import pyautogui
import time
import keyboard
import random
import numpy as np
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

zero_thres = 10
CONFIDENCE = 0.9
CONFIDENCE_BUTTON = 0.75                     

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
box_path = 'box.png'
zero_path = 'zero.png'
discard_button_path = 'discard_button.png'

#functions
def key(coisa):
    keyboard.press(coisa)
    time.sleep(0.1)
    keyboard.release(coisa)

def cast(CASTING_TIME):
    mouse.press(Button.left)
    time.sleep(CASTING_TIME)
    mouse.release(Button.left)
    
def reel():
    mouse.press(Button.right)
    mouse.press(Button.left)
    time.sleep(2)
    mouse.release(Button.left)
    mouse.release(Button.right)

def hooked():
    if pyautogui.locateOnScreen(box_path, confidence=CONFIDENCE) != None:
        return True
    else:
        return False

def keep_fish():
    key('space')

def release_fish():
    key('backspace')

def discard():
    mouse.position = (pyautogui.locateCenterOnScreen(discard_button_path, confidence=CONFIDENCE_BUTTON))
    time.sleep(0.2)
    mouse.press(Button.left)
    time.sleep(0.2)
    mouse.release(Button.left)
    time.sleep(0.5)

def extend_day():
    mouse.position = (pyautogui.locateCenterOnScreen(extend_button_path, confidence=CONFIDENCE_BUTTON))
    time.sleep(0.2)
    mouse.press(Button.left)
    time.sleep(0.2)
    mouse.release(Button.left)
    time.sleep(0.5)
    key('esc')
    time.sleep(0.5)

def next_day():
    key('t')
    time.sleep(0.5)
    mouse.position = (pyautogui.locateCenterOnScreen(next_morning_button_path, confidence=CONFIDENCE_BUTTON))
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
    z = pyautogui.locateCenterOnScreen(zero_path, confidence=CONFIDENCE)

    if z != None:
        soma = abs(z[0] + z[1] - zero_pos[0] - zero_pos[1])

        if soma <= zero_thres:
            return True
        else:
            return False
    else:
        return False


def calibration():
    zero_pos = pyautogui.locateCenterOnScreen(zero_path, confidence=CONFIDENCE)
    return zero_pos

def close():
    mouse.position = pyautogui.locateCenterOnScreen(close_button_path, confidence=CONFIDENCE_BUTTON)
    time.sleep(0.2)
    mouse.press(Button.left)
    time.sleep(0.2)
    mouse.release(Button.left)
    time.sleep(0.5)

def gray_close():
    mouse.position = pyautogui.locateCenterOnScreen(gray_close_button_path, confidence=CONFIDENCE_BUTTON)
    time.sleep(0.2)
    mouse.press(Button.left)
    time.sleep(0.2)
    mouse.release(Button.left)
    time.sleep(0.5)

def achiv():
    if pyautogui.locateOnScreen(close_button_path, confidence=CONFIDENCE_BUTTON) != None:
        close()
        time.sleep(2)
    if pyautogui.locateOnScreen(gray_close_button_path, confidence=CONFIDENCE_BUTTON) != None:
        gray_close()
        time.sleep(2)

def ok():
    mouse.position = pyautogui.locateCenterOnScreen(ok_button_path, confidence=CONFIDENCE_BUTTON)
    time.sleep(0.2)
    mouse.press(Button.left)
    time.sleep(0.2)
    mouse.release(Button.left)
    time.sleep(0.5)

def level():
    if pyautogui.locateOnScreen(ok_button_path, confidence=CONFIDENCE_BUTTON) != None:
        ok()
        time.sleep(2)

def verification():
    
    if pyautogui.locateOnScreen(keep_button_path, confidence=CONFIDENCE_BUTTON) != None:
        keep_fish()
        time.sleep(2)

    elif pyautogui.locateOnScreen(black_keep_button_path, confidence=CONFIDENCE_BUTTON) != None:
        release_fish()
        time.sleep(3)

        level()
        achiv()

        if pyautogui.locateOnScreen(extend_button_path, confidence=CONFIDENCE_BUTTON) != None:
            extend_day()
            time.sleep(3)
            achiv()
        else:
            next_day()
            time.sleep(3)
            achiv()

    elif pyautogui.locateOnScreen(discard_button_path, confidence=CONFIDENCE_BUTTON) != None:
        discard()
        time.sleep(2)


    level()
    achiv()

    if pyautogui.locateOnScreen(extend_button_path, confidence=CONFIDENCE_BUTTON) != None:
        extend_day()
        time.sleep(3)
        achiv()

time.sleep(2)

zero_pos = calibration()

if (style == 2): 
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
    time.sleep(1)

    while True:
        if is_zero():
            time.sleep(1.7)
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
            mouse.press(Button.right)
            mouse.press(Button.left)
            while is_zero() == False:
                pass    
            mouse.release(Button.left)
            mouse.release(Button.right)
