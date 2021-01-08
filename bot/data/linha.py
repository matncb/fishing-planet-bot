import pyscreenshot as ImageGrab
from PIL import Image
import pytesseract
import time

#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def atualizar(line_bbox):
    l = ImageGrab.grab(bbox=line_bbox)

    
    half = 1
    out = l.resize([int(half * s) for s in l.size])
    #out.save('linha.jpg', 'jpeg')

    try:
        #texto = pytesseract.image_to_string(Image.open('linha.jpg'), config='--psm 6')
        texto = pytesseract.image_to_string(out, config='--psm 6')
        print('linha-texto------> ', texto)
        texto = int(texto)
        return texto
    except:
        print("error-linha")
        pass
    




