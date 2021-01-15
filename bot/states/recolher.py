
from pynput.mouse import Button, Controller
import time

mouse = Controller()

def peixe():
    print("Recolher...")
    mouse.press(Button.left)
    time.sleep(0.5)
    mouse.press(Button.right)
    time.sleep(0.5)
    mouse.release(Button.right)
    time.sleep(0.25)
    mouse.release(Button.left)
    





