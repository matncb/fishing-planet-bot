import pyautogui
import time
import keyboard
import random
import numpy as np
from pynput.mouse import Button, Controller
mouse = Controller()

#######################################################################
#starting

print("Welcome to the Fishing Planet Bot!")
print("")
print("Select your fishing style:")
print("Enter 1 for lure fishing")
print("Enter 2 for bottom or float fishing")
print("")

style = int(input("Enter your style: ")) #selec style

print("")

if style == 1:
    print("Select the lure work: ")
    print("Enter 1 for stop and go")
    print("Enter 2 for twiching or popping")
    print("")
    work = int(input("Enter the work: ")) #selec work for lure
    print("")

print("Enter your CAST_LENTH: ")
print("Enter 0 if you want to go default (full cast)")
print("")

CAST_LENGTH = int(input("Enter the CAST_LENGTH: ")) #Casting lenght

print("")
print("[STATUS] Starting...")
print("")

########################################################################
#load configs

import configparser  #para carregar as configurações
Config = configparser.ConfigParser()
Config.read("config.ini") #ler arquivo de configurações

FULL_CASTING_TIME = float(Config.get('Casting', 'FULL_CASTING_TIME'))
FULL_CASTING_LENGTH = float(Config.get('Casting', 'FULL_CASTING_LENGTH'))
SINKING_TIME = float(Config.get('Casting', 'SINKING_TIME'))

ZERO_THRES =  float(Config.get('Confidence', 'ZERO_THRES'))
CONFIDENCE = float(Config.get('Confidence', 'CONFIDENCE'))
CONFIDENCE_BUTTON = float(Config.get('Confidence', 'CONFIDENCE_BUTTON'))   

VERBOSE = bool(Config.get('Verbose', 'VERBOSE'))

#calculos com base nos parametros carregados
if CAST_LENGTH  == 0:
    CAST_LENGTH = FULL_CASTING_LENGTH

CASTING_TIME = (CAST_LENGTH * (FULL_CASTING_TIME - 0.9))/FULL_CASTING_LENGTH + 0.9 #calculo do tempo de lancamento --> puramente empirico

#carrega os caminhos das imagens necessarias
keep_button_path = './images/keep_button.png'
black_keep_button_path = './images/black_keep_button.png'
release_button_path = './images/release_button.png'
extend_button_path = './images/extend_button.png'
next_morning_button_path = './images/next_morning_button.png'
close_button_path = './images/close_button.png'
gray_close_button_path = './images/gray_close_button.png'
ok_button_path = './images/ok_button.png'
box_path = './images/box.png'
zero_path = './images/zero.png'
discard_button_path = './images/discard_button.png'

########################################################################################
#funcoes genericas

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
    if VERBOSE: print("[STATUS] Kept fish!")
    key('space')

def release_fish():
    if VERBOSE: print("[STATUS] Realeased fish!")
    key('backspace')

def discard():
    mouse.position = (pyautogui.locateCenterOnScreen(discard_button_path, confidence=CONFIDENCE_BUTTON))
    time.sleep(0.2)
    mouse.press(Button.left)
    time.sleep(0.2)
    mouse.release(Button.left)
    time.sleep(0.5)
    if VERBOSE: print("[STATUS] Discarted something!")

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

def is_zero():
    z = pyautogui.locateCenterOnScreen(zero_path, confidence=CONFIDENCE)

    if z != None:
        soma = abs(z[0] + z[1] - zero_pos[0] - zero_pos[1])
        if soma <= ZERO_THRES: #verificacao se o zero em questao esta na posicao correta
            return True
        else:
            return False
    else:
        return False


def calibration():
    print("[STATUS] Calibrating zero...")
    zero_pos = pyautogui.locateCenterOnScreen(zero_path, confidence=CONFIDENCE)

    if zero_pos != None:
        print("[STATUS] Done.")
    else:
        print("[STATUS] No zero found.")
        print("[STATUS] Quiting...")
        exit()
    print("")

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

##############################################################################
#trabalhos

STOPGO_PRESSING_TIME = float(Config.get('Stopgo', 'STOPGO_PRESSING_TIME'))
STOPGO_RELEASE_TIME = float(Config.get('Stopgo', 'STOPGO_RELEASE_TIME'))

def stopgo():
    mouse.press(Button.left)
    time.sleep(STOPGO_PRESSING_TIME)
    mouse.release(Button.left)
    time.sleep(STOPGO_RELEASE_TIME) 

TWICHING_LEFT_PRESSING_TIME = float(Config.get('Twiching', 'TWICHING_LEFT_PRESSING_TIME'))
TWICHING_RIGHT_PRESSING_TIME = float(Config.get('Twiching', 'TWICHING_RIGHT_PRESSING_TIME'))

def twiching():
    mouse.press(Button.left)
    time.sleep(TWICHING_LEFT_PRESSING_TIME)
    mouse.release(Button.left)
    time.sleep(0.1)
    mouse.press(Button.right)
    time.sleep(TWICHING_RIGHT_PRESSING_TIME)
    mouse.release(Button.right)
    time.sleep(0.1)


##############################################################################################################
#ordem das verificacoes 

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

###################################################################################################################
#inicio da pescaria

time.sleep(2)

zero_pos = calibration() #calibra a posicao do zero

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
            time.sleep(SINKING_TIME)
    
elif (style == 1): #artificial
    time.sleep(1)

    while True:
        if is_zero():
            time.sleep(1.7)
            verification()
            time.sleep(0.2)

            if VERBOSE: print("[STATUS] Casting...")

            cast(CASTING_TIME)
            time.sleep(SINKING_TIME) 
          
        if work == 1:
            stopgo()
        else:
            twiching()

        if hooked() == True:
            if VERBOSE: print("[STATUS] Hooked!!")

            mouse.press(Button.right)
            mouse.press(Button.left)
            while is_zero() == False:
                pass    
            mouse.release(Button.left)
            mouse.release(Button.right)
