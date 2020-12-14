import pyscreenshot as ImageGrab
from PIL import Image
import pytesseract
from pynput.mouse import Button, Controller
import time
import pyautogui
from pynput.keyboard import Key, Listener
import logging
import threading

mouse = Controller()

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def atualizar():

    l = ImageGrab.grab(bbox=(2141,917,2300,1014))

    half = 3
    out = l.resize([int(half * s) for s in l.size])
    out.save('linha.jpg', 'jpeg')
    
    try:
        texto = pytesseract.image_to_string(Image.open('linha.jpg'))
        print(texto)
        texto = int(texto)
        return texto
    except:
        pass
    





