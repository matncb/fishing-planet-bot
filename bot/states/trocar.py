from pynput.mouse import Button, Controller
import pyautogui
import time

mouse = Controller()


def trocar(next_morning_button, extend_button):
    print("Trocar...")
    pyautogui.press('t')
    time.sleep(0.2)
    mouse.position = next_morning_button
    time.sleep(0.2)
    mouse.click(Button.left)
    time.sleep(0.2)
    mouse.position = extend_button
    time.sleep(0.2)
    mouse.click(Button.left)
    time.sleep(0.5)
    pyautogui.press('esc')
    time.sleep(2)







