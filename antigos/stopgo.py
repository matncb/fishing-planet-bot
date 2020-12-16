from pynput.mouse import Button, Controller
import time
mouse = Controller()


def pescar():
    #mouse.position = (1444, 925)
    #mouse.click(Button.left)
    mouse.press(Button.left)
    time.sleep(2)
    mouse.release(Button.left)
    #time.sleep(0.05)
    time.sleep(0.7)
    
def pegar():
    mouse.position = (1444, 925)
    mouse.click(Button.left)
    time.sleep(0.05)
    #mouse.position = (pos)

#time.sleep(2)
#mouse.position = (1491, 1236)
#time.sleep(3)

while True:  
    pescar()
    #pegar()
    
    #pos = mouse.position
    #print(pos)
