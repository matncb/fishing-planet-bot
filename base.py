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

#imagem = ImageGrab.grab()
#imagem.save('print.jpg', 'jpeg')

global rec
rec = int(3)

def kilo():
    while True:
        #saco =ImageGrab.grab(bbox=(105,171,205,200))
        saco =ImageGrab.grab(bbox=(115,175,254,202))
        #saco.show()
        saco.save('saco.jpg', 'jpeg')
        texto = pytesseract.image_to_string(Image.open('saco.jpg'))
        texto = list(texto)

        #linha2 = False
        #kg = []
        
        '''
        for i in range(len(texto)):
            if linha2:
                kg.append(texto[i])
            if texto[i] == "\n":
                linha2 = True
        '''
        v1 = False
        v2 = False
        
        global kg_atual
        kg_atual = ""
        
        for i in range(len(texto)):
            if texto[i] == "/":
                v1 = True
            if v1 == False:
                kg_atual += texto[i]
        try:
            kg_atual = float(kg_atual)
            if kg_atual < 0:
                kg_atual = kg_atual * -1
            print (kg_atual)
            if kg_atual >= 98.0 and kg_atual <= 103.0:
                time.sleep(40)
            time.sleep(2)
        except:
            pass
        
def linha():
    while True:
        linha = ImageGrab.grab()
        #linha.show()
        linha.save('linha.png', 'png')
        im = Image.open('linha.png')
        pix = im.load()
        '''
        print(pix[2198, 936])
        print(pix[2198, 997])
        print(pix[2183, 962])
        print(pix[2214, 962])
        '''
        global dis

        '''
        if pix[2198, 936] == (247, 247, 247) and pix[2198, 997] == (247, 247, 247) and pix[2183, 962] == (247, 247, 247) and pix[2214, 962] == (247, 247, 247):
            dis = True
        else:
            dis = False
        '''

        if pix[2201, 967] != (247, 247, 247) and pix[2201, 959] != (247, 247, 247) and pix[2200, 973] != (247, 247, 247) and pix[2196, 980] != (247, 247, 247):
            dis = True
        else:
            dis = False
        
        '''
        texto = pytesseract.image_to_string(Image.open('linha.jpg'))
        print(texto)

        global dist
        
        try:
            dist = float(texto)
            #print(dist)
        except:
            #print("deu ruim")
            pass
        '''
        
def pescar():
    while True:
        mouse.position = (1444, 925)
        #mouse.click(Button.left)
        mouse.press(Button.left)
        time.sleep(1.9)
        #mouse.release(Button.left)
        mouse.click(Button.left)
        time.sleep(0.05)
        mouse.press(Button.right)
        time.sleep(0.5)
        mouse.release(Button.right)
        mouse.release(Button.left)
        time.sleep(0.05)
        try:
            if kg_atual >= 98.0 and kg_atual <= 102.0:
                zerar()
                time.sleep(10) 
        except:
            pass
        
def arremesso():
    time.sleep(3)
    mouse.position = (1444, 925)
    mouse.press(Button.left)
    time.sleep(2)
    mouse.release(Button.left)
    time.sleep(5)
    
def pescar_carretilha():
    mouse.position = (1444, 925)
    mouse.press(Button.left)
    time.sleep(0.5)
    mouse.press(Button.right)
    time.sleep(0.25)
    mouse.release(Button.left)
    time.sleep(0.25)
    mouse.release(Button.right)
    time.sleep(0.2)
    
def carretilha():
    while True:
        try:
            if kg_atual >= 98.0 and kg_atual <= 103.0:
                zerar()
                time.sleep(10)
        except:
            pass
        if dis == True:
            arremesso()
        else:
            pescar_carretilha()
        
def stopgo():
    while True:
        mouse.position = (1444, 925)
        #mouse.click(Button.left)
        mouse.press(Button.left)
        time.sleep(1.9)
        #mouse.release(Button.left)
        mouse.click(Button.left)
        time.sleep(0.7)
        try:
            if kg_atual >= 49.0:
                zerar()
                time.sleep(10)
        except:
            pass

def config(n):
    for i in range(5):
        pyautogui.press('k')
        time.sleep(0.1)
    for i in range(n):
        pyautogui.press('l')
	
def confirm():
	mouse.position = (1102, 672)
	time.sleep(1)
	mouse.click(Button.left)
	time.sleep(1)

def recolher():
	pyautogui.press('l')
	time.sleep(0.1)
	pyautogui.press('l')
	time.sleep(0.1)
	pyautogui.press('l')
	time.sleep(0.1)
	pyautogui.press('l')
	time.sleep(0.1)
	mouse.press(Button.left)
	time.sleep(30)
	mouse.release(Button.left)
	time.sleep(1)
	config(rec)
	time.sleep(1)
	
	

def zerar():
    mouse.click(Button.left)
    time.sleep(0.5)
    recolher()
    time.sleep(1)
    pyautogui.press('t')
    time.sleep(1)
    mouse.position = (1277, 735)
    time.sleep(1)
    mouse.click(Button.left)
    time.sleep(1)
    confirm()
    mouse.position = (873, 840)
    time.sleep(1)
    mouse.click(Button.left)
    time.sleep(1)
    kg_atual = ""

 
def thread_function1(name):
    logging.info("Thread %s: starting", name)
    kilo()
    logging.info("Thread %s: finishing", name)
    
def thread_function2(name):
    logging.info("Thread %s: starting", name)
    #pescar()
    #stopgo()
    carretilha()
    logging.info("Thread %s: finishing", name)
      
def thread_function3(name):
    logging.info("Thread %s: starting", name)
    linha()
    logging.info("Thread %s: finishing", name)
      

time.sleep(3)
config(rec)
time.sleep(1)


kilo_thread = threading.Thread(target=thread_function1, args=(1,))
kilo_thread.start()

linha_thread = threading.Thread(target=thread_function3, args=(2,))
linha_thread.start()

time.sleep(3)

pesca_thread = threading.Thread(target=thread_function2, args=(3,))
pesca_thread.start()




'''
im = Image.open('base.png')
pix = im.load()

print(pix[2198, 936])
print(pix[2198, 997])
print(pix[2183, 962])
print(pix[2214, 962])

(247, 247, 247, 255)

'''



