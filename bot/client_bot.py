import requests
import time
import asyncio
import json
from pynput.mouse import Button, Controller

from states import pescar
from states import recolher
from states import arremessar
from states import trocar

saco = {}
line = {}
fisgar = {}

def get_saco():
    global saco
    saco = requests.get('http://localhost:5000/saco').json()

def get_line():
    global line
    line = requests.get('http://localhost:5000/linha').json()

def get_fisgar():
    global fisgar
    fisgar = requests.get('http://localhost:5000/fisga').json()

async def main(loop):    
 
    try:

       start = time.strftime("%d.%m.%Y-%H:%M:%S")
       print('Robo: Iniciar pesca....', start )
       time.sleep(3)
       
       config = requests.get('http://localhost:5000/config').json()
       get_saco()
       get_line()
       get_fisgar()
       pescar.config(config["velocidade_recolhimento"])

       while True:

           loop.run_in_executor(None, get_saco)
           loop.run_in_executor(None, get_line)
           loop.run_in_executor(None, get_fisgar)

           if saco["kg_atual"] < config['kg_max']:
               if line["n_line"] == 0:
                  #print("Arremessar")
                  arremessar.arremessar(config["casting_time"])
               elif fisgar["fisgou"]:
                  #print("Recolher")
                  recolher.peixe()
               else:
                  #print("Pescar")
                  pescar.twiching()
                  #pescar.stopgo()
           else:
              #print("Trocar")
              trocar.trocar(config["next_morning_button"], config["extend_button"])
           
    except KeyboardInterrupt:

        mouse = Controller()
        mouse.release(Button.left)
        mouse.release(Button.right)

        end = time.strftime("%d.%m.%Y-%H:%M:%S")
        print('Robo: Finalizar pesca....', end) 
        pass

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))