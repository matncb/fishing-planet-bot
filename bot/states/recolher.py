
from pynput.mouse import Button, Controller
import time

mouse = Controller()

def peixe():
    mouse.press(Button.Left)
    time.sleep(1)
    mouse.release(Button.Left)





