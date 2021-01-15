import pyscreenshot as ImageGrab
from PIL import Image
import time

def atualizar(fisgar_pos):

    try:
        fisgou = ImageGrab.grab(bbox=fisgar_pos).load()
        pix = fisgou
        a, b, c = pix[1, 3]
        if (a>=177) and (a<=210) and (b >=180) and (b<=210) and (c>=180) and (c<=210):
            return True
        else:
            return False
    except:
        print("erro-fisgou")
        pass
           


