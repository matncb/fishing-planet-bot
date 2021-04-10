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

#positions
#next_morning_button = (1283, 869)
#extend_button = (1095, 677)
#saco_bbox = (115,175,254,202)
#line_bbox = (2141,917,2300,1014)
#fisgar_pos = (2411, 953)

#config vars
#casting_time = 2
#velocidade_recolhimento = 2
#kg_max = 100.0

next_morning_button = (1283, 869)
extend_button = (1095, 677)
saco_bbox = (2074,237,2261,274)
line_bbox = (3938,1230,4120,1353)
fisgar_pos = (4273, 1274, 4291, 1280)

#config vars
casting_time = 2
velocidade_recolhimento = 2
kg_max = 100.0



#dados

time.sleep(3)

#kg_max = kg.get_kg_max(saco_bbox)

class Saco(Thread):
    def __init__(self):
        super().__init__()
        self.kg_atual = 0.0
    def run(self):
        while True:
            kg_ = kg.atualizar(saco_bbox)
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
            linha_ = linha.atualizar(line_bbox)
            if linha_ != None:
                self.n_linha = linha_

line = Linha()
line.start()

class Fisgar(Thread):
    def __init__(self):
        super().__init__()
        self.fisgou = False
    def run(self):
        while True:
            self.fisgou = fisgou.atualizar(fisgar_pos)

fisgar = Fisgar()
fisgar.start()

####

time.sleep(2)
pescar.config(velocidade_recolhimento)

class State(Thread):
    def __init__(self):
        super().__init__()
    def run(self):
        while True:
            if saco.kg_atual < kg_max:
                if line.n_linha == 0:
                    arremessar.arremessar(casting_time)
                elif fisgar.fisgou:
                    recolher.peixe()
                else:
                    #pescar.twiching()
                    pescar.stopgo()
            else:
                trocar.trocar(next_morning_button, extend_button)
                
state = State()
time.sleep(1)
state.start()








