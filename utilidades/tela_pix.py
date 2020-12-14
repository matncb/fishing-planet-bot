import pyscreenshot as ImageGrab
from PIL import Image
import time

pos1 = 2275
pos2 = 720

time.sleep(2)

img = ImageGrab.grab()
img.save('img.png', 'png')
im = Image.open('img.png')
pix = im.load()

base = pix[pos1, pos2]


while True:
    img= ImageGrab.grab()
    img.save('img.png', 'png')
    im = Image.open('img.png')
    pix = im.load()

    if pix[pos1, pos2] != base:
        print(pix[pos1, pos2])

    

    
