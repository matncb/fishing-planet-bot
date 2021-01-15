import requests
import time

from states import pescar
from states import recolher
from states import arremessar
from states import trocar

def main():    
 
    try:
       start = time.strftime("%d.%m.%Y-%H:%M:%S")
       print('Cliente: Iniciar pesca....', start )
       config = requests.get('http://localhost:5000/config').json()
       pescar.config(config["velocidade_recolhimento"])

       while True:
            saco = requests.get('http://localhost:5000/saco').json()
            line = requests.get('http://localhost:5000/linha').json()
            fisgar = requests.get('http://localhost:5000/fisga').json()

            if saco["kg_atual"] < config['kg_max']:
                if line["n_line"]== 0:
                    arremessar.arremessar(config["casting_time"])
                elif fisgar["fisgou"]:
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