import pyscreenshot as ImageGrab
from PIL import Image
import pytesseract
from pynput.mouse import Button, Controller
import time
import pyautogui
from pynput.keyboard import Key, Listener
from threading import Thread

mouse = Controller()

#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

from data import kg
from data import fisgou
from data import linha

from states import pescar
from states import recolher
from states import arremessar
from states import trocar


##### Definicao das classes #####
class Config:
   def __init__(self):
        #positions
        self.next_morning_button = (1283, 869)
        self.extend_button = (1095, 677)
        self.saco_bbox = (115,175,254,202)
        self.line_bbox = (2141,917,2300,1014)
        self.fisgar_pos = (2411, 953)

        #config vars
        self.casting_time = 2
        self.velocidade_recolhimento = 2
        self.kg_max = 100.0

class Saco(Thread):
    def __init__(self, config):
        super().__init__()
        self.kg_atual = 0.0
        self.config = config
    def run(self):
        print('Configurar saco!!!' )
        #while True:
        kg_ = kg.atualizar(self.config.saco_bbox)
        if kg_ != None:
            self.kg_atual = kg_

class Line(Thread):
    def __init__(self,config):
        super().__init__()
        self.n_line = 0
        self.config = config
    def run(self):
        print('Configurar linha!!!' )
        #while True:
        line_ = linha.atualizar(self.config.line_bbox)
        if line_ != None:
            self.n_line = line_

class Fisgar(Thread):
    def __init__(self, config):
        super().__init__()
        self.fisgou = False
        self.config = config
    def run(self):
        print('Fisgar!!!' )
        #while True:
        self.fisgou = fisgou.atualizar(self.config.fisgar_pos)

class State(Thread):
    def __init__(self, config, saco, fisgar, line):
        super().__init__()
        self.config = config
        self.saco = saco
        self.fisgar = fisgar
        self.line = line

    def run(self):
        print('Pescar!!!' )
        #while True:
        if self.saco.kg_atual < self.config.kg_max:
            if self.line.n_line == 0:
                arremessar.arremessar(self.config.casting_time)
            elif self.fisgar.fisgou:
                recolher.peixe()
            else:
                #pescar.twiching()
                pescar.stopgo()
        else:
           trocar.trocar(self.config.next_morning_button, self.config.extend_button)



def main():    
 
    #dados
    config = Config()
    #time.sleep(3)

    try:

       start = time.strftime("%d.%m.%Y-%H:%M:%S")
       print('Iniciar pesca....', start )

       while True:
           
            saco = Saco(config)
            saco.start()
        
            line = Line(config)
            line.start()

            #time.sleep(2)
            pescar.config(config.velocidade_recolhimento)

            fisgar = Fisgar(config)
            fisgar.start()
                            
            state = State(config, saco, fisgar, line)
            #time.sleep(1)
            state.start()

    except KeyboardInterrupt:
        end = time.strftime("%d.%m.%Y-%H:%M:%S")
        print('Finalizar pesca....', end) 
        pass


if __name__ == "__main__":
   main()





