import requests
import time
from threading import Thread

from states import pescar
from states import recolher
from states import arremessar
from states import trocar

class Status(Thread):
    def __init__(self):
        super().__init__()
        self.saco = { "kg_atual": 0.0 }
        self.line = { "n_line": 0 }
        self.fisgar = { "fisgou": False }

    def run(self):
       while True: 
          self.saco = requests.get('http://localhost:5000/saco').json()
          self.line = requests.get('http://localhost:5000/linha').json()
          self.fisgar = requests.get('http://localhost:5000/fisga').json()
        

def main():    
 
    try:

       start = time.strftime("%d.%m.%Y-%H:%M:%S")
       print('Robo: Iniciar pesca....', start )
       time.sleep(3)
       
       config = requests.get('http://localhost:5000/config').json()
       pescar.config(config["velocidade_recolhimento"])

       status = Status()
       status.start()
       
       while True:
 
           if status.saco["kg_atual"] < config['kg_max']:
                if status.line["n_line"] == 0:
                    arremessar.arremessar(config["casting_time"])
                elif status.fisgar["fisgou"]:
                   recolher.peixe()
                else:
                    pescar.twiching()
                    #pescar.stopgo()
           else:
                trocar.trocar(config["next_morning_button"], config["extend_button"])
           
    except KeyboardInterrupt:
        end = time.strftime("%d.%m.%Y-%H:%M:%S")
        print('Robo: Finalizar pesca....', end) 
        pass

main()