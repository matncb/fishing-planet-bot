from pynput.mouse import Button, Controller
import time
import asyncio
from pynput.keyboard import Key, Listener

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

        #self.saco_bbox = (115,175,254,202)
        self.saco_bbox = (2074,237,2261,274)

        #self.line_bbox = (2141,917,2300,1014)
        #self.line_bbox = (3910,1206,3993,1299)
        self.line_bbox = (3938,1230,4120,1353)

        #self.fisgar_pos = (2411, 953)
        #self.fisgar_pos = (4286, 1276)

        self.fisgar_pos = (4273, 1274, 4291, 1280)

        #config vars
        self.casting_time = 2
        self.velocidade_recolhimento = 2
        self.kg_max = 100.0



class Saco():
    def __init__(self, config):
        super().__init__()
        self.kg_atual = 0.0
        self.config = config
    def run(self):
        print('Executar: Saco()' )
        kg_ = kg.atualizar(self.config.saco_bbox)
        if kg_ != None:
            self.kg_atual = kg_

class Line():
    def __init__(self,config):
        super().__init__()
        self.n_line = 0
        self.config = config
    def run(self):
        print('Executar: Line()' )
        line_ = linha.atualizar(self.config.line_bbox)
        if line_ != None:
            self.n_line = line_

class Fisgar():
    def __init__(self, config):
        super().__init__()
        self.fisgou = False
        self.config = config
    def run(self):
        print('Executar: Fisgar()' )
        self.fisgou = fisgou.atualizar(self.config.fisgar_pos)

class State():
    def __init__(self):
        super().__init__()

    def run(self, config, saco, fisgar, line):
          if saco.kg_atual < config.kg_max:
             if line.n_line == 0:
                print("Arremessar....")
                #time.sleep(1)
                #arremessar.arremessar(config.casting_time)
             elif fisgar.fisgou:
                print("Fisgou....")
                #recolher.peixe()
                #time.sleep(10)
             else:
                print("Pescar....")
                #pescar.twiching()
                #pescar.stopgo()
                #time.sleep(10)
          else:
              print("Trocar....")
              #time.sleep(5)
              #trocar.trocar(config.next_morning_button, config.extend_button)

def get_saco(config):
    global saco
    saco.run()
    #time.sleep(0.5)

def get_line(config):
    global line
    line.run()
    #time.sleep(0.5)


def get_fisgar(config):
    global fisgar
    fisgar.run()
    #time.sleep(0.5)

def get_state(config, saco, fisgar, line ):
    global state
    state.run(config, saco, fisgar, line)
    #time.sleep(0.5)

config = Config()
saco = Saco(config)
line = Line(config)
fisgar = Fisgar(config)
state = State()

async def main(loop):    

    try:

       start = time.strftime("%d.%m.%Y-%H:%M:%S")
       print('Iniciar pesca....', start )
       
       #get_saco(config)
       #get_line(config)
       #get_fisgar(config)
       #pescar.config(config.velocidade_recolhimento)

       while True:
            
           loop.run_in_executor(None, get_saco, config)
           loop.run_in_executor(None, get_line, config)
           loop.run_in_executor(None, get_fisgar, config)
           loop.run_in_executor(None, get_state, config, saco, fisgar, line)

         
    except KeyboardInterrupt:

        mouse = Controller()
        mouse.release(Button.left)
        mouse.release(Button.right)

        end = time.strftime("%d.%m.%Y-%H:%M:%S")
        print('Finalizar pesca....', end) 
        pass


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))




