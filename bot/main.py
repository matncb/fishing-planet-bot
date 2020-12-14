import pyscreenshot as ImageGrab
from PIL import Image
import pytesseract
from pynput.mouse import Button, Controller
import time
import pyautogui
from pynput.keyboard import Key, Listener
from threading import Thread

mouse = Controller()

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

from data import kg
from data import fisgou
from data import linha
#######

#vars

global state #pescar, recolher, arremessar, trocar dia

#dados

time.sleep(3)

kg_max = kg.get_kg_max()

class Saco(Thread):
    def __init__(self):
        super().__init__()
        self.kg_atual = 0.0
    def run(self):
        while True:
            kg_ = kg.atualizar()
            if kg_ != None:
                self.kg_atual = kg_

saco = Saco()
saco.start()

        










