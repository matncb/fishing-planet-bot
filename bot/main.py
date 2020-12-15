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

from states import pescar
from states import recolher
from states import arremessar
from states import trocar


#######

#vars

keep_button = (1444, 925)
casting_time = 2
velocidade_recolhimento = 2

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

class Linha(Thread):
    def __init__(self):
        super().__init__()
        self.n_linha = 0
    def run(self):
        while True:
            linha_ = linha.atualizar()
            if linha_ != None:
                self.n_linha = linha_

line = Linha()
line.start()

####

time.sleep(2)
pescar.config(velocidade_recolhimento)

class State(Thread):
    def __init__(self):
        super().__init__()
        self.state = 'arremessar'
    def run(self):
        while True:
            if saco.kg_atual < kg_max:
                if line.n_linha == 0:
                    #self.state = 'arremessar'
                    arremessar.arremessar(casting_time, keep_button)
                else:
                    #self.state = 'pescar'
                    pescar.twiching(keep_button)
            else:
                trocar.trocar()

state = State()
state.start()

time.sleep(1)

###

'''
while True:
    if state.state == 'arremessar':
        arremessar.arremessar(casting_time)
    elif state.state == 'pescar':
        pescar.twiching(keep_button)
        print(line.n_linha)

'''






