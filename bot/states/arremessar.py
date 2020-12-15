from pynput.mouse import Button, Controller
mouse = Controller()
import time

def arremessar(t, keep_button):
    mouse.position = (keep_button)
    time.sleep(0.2)
    mouse.press(Button.left)
    time.sleep(t)
    mouse.release(Button.left)
    time.sleep(5)
