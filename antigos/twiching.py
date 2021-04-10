from pynput.mouse import Button, Controller
import time
import pyautogui
import sys
from pynput.keyboard import Key, Listener
mouse = Controller()


def pescar():
    #mouse.position = (1444, 925)
    #mouse.position = (1190, 994)
    #mouse.position = (1312, 1018)
    #mouse.position = (1299, 1010)
    mouse.position = (1540, 1200)
    #mouse.click(Button.left)
    mouse.press(Button.left)
    time.sleep(1.9)
    #time.sleep(2)
    mouse.release(Button.left)
    mouse.click(Button.left)
    time.sleep(0.05)
    #time.sleep(0.08)
    mouse.press(Button.right)
    time.sleep(0.5)
    #time.sleep(0.3)
    mouse.release(Button.right)
    time.sleep(0.05)
    #time.sleep(0.08)
   
    
def pegar():
    mouse.position = (1540, 1200)
    mouse.click(Button.left)
    time.sleep(0.05)
    #mouse.position = (pos)

while True:  
    mouse.position = (1444, 1200)
    pescar()
    #pegar()
    
    #pos = mouse.position
    #print(pos)



'''
def pescar():
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

def pescar2():
    #mouse.position = (1444, 925)
    #mouse.click(Button.left)
    mouse.press(Button.left)
    time.sleep(1.9)
    #mouse.release(Button.left)
    mouse.click(Button.left)
    time.sleep(0.025)
    mouse.press(Button.right)
    time.sleep(0.25)
    mouse.release(Button.right)
    mouse.release(Button.left)
    time.sleep(0.025)
    
    
def pegar():
    mouse.position = (1444, 925)
    time.sleep(0.0000000000001)
    mouse.click(Button.left)
    time.sleep(0.0000000000001)
    mouse.position = pos
    time.sleep(0.001)

time.sleep(2)
mouse.position = (1444, 925)
time.sleep(3)

pos = mouse.position
    
    
while True:  
    pescar()
    #pegar()
      
'''    
