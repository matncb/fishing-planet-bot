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

from data import kg
from data import fisgou
from data import linha
#######

#vars

global state #pescar, recolher, arremessar, trocar dia
global kg_atual
global kg_max
global fisgou
global linha

#dados







