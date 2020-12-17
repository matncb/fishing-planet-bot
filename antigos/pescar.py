from pynput.mouse import Button, Controller
import time
import pyautogui
import sys
from pynput.keyboard import Key, Listener
mouse = Controller()

def twiching():
    mouse.press(Button.left)
    time.sleep(2)
    mouse.release(Button.left)
    mouse.click(Button.left)
    time.sleep(0.05)
    mouse.press(Button.right)
    time.sleep(0.7)
    mouse.release(Button.right)
    time.sleep(0.05)

def stopgo():
    mouse.press(Button.left)
    time.sleep(2)
    mouse.release(Button.left)
    time.sleep(0.7)    

def iniciar(tipo):    
    start = time.strftime("%d.%m.%Y-%H:%M:%S")
    print('Iniciar pesca....', start )
    time.sleep(2)
    #mouse.position = (1444, 925)
    time.sleep(3)

    print('Entrou no loop....')
    #i = 0 
    #while i < 10:  
    try:
        while True:  
            if ( tipo == '1'):     
                #print('Modo de pesca: twiching') 
                twiching()
            elif ( tipo == '2'):  
                #print('Modo de pesca: stopgo') 
                stopgo() 
            else:
                #print('Modo de pesca não existe !!!') 
                twiching()
                stopgo() 
                #i = 10
            #break
            #i = i + 1

            #Nao funcionou no windows e prejudicou o trabalho do twiching
            #time.sleep(0.1)
            #pyautogui.press('space')
            #time.sleep(1)
 
    except KeyboardInterrupt:
        print("Programa foi interrompido.")
        pass

def main(argv):    
   if ( len(sys.argv) == 2 ):
     iniciar(argv[0])
     end = time.strftime("%d.%m.%Y-%H:%M:%S")
     print('Finalizar pesca....', end) 
     sys.exit()
   else:
     print('pescar.py  <tipo da pesca> ') 
     print(' Tipo da pesca: 1 - twiching , 2 - Stopgo ') 


if __name__ == "__main__":
   main(sys.argv[1:])