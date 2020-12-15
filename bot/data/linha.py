
import time
import pyscreenshot as ImageGrab
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def atualizar():
    l = ImageGrab.grab(bbox=(2141,917,2300,1014))

    half = 3
    out = l.resize([int(half * s) for s in l.size])
    out.save('linha.jpg', 'jpeg')

    try:
        texto = pytesseract.image_to_string(Image.open('linha.jpg'), config='--psm 6')
        texto = int(texto)
        return texto
    except:
        pass
    




