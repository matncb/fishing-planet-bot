import pyscreenshot as ImageGrab
from PIL import Image
import time

def atualizar(fisgar_pos):
    fisgou = ImageGrab.grab()
    fisgou.save('fisgou.jpg', 'jpeg')

    im = Image.open('fisgou.jpg')
    pix = im.load()

    x, y = fisgar_pos

    a, b, c = pix[x, y]

    if (a>=180) and (a<=210) and (b >=180) and (b<=210) and (c>=180) and (c<=210):
        return True
    else:
        return False


