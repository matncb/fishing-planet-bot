import pyscreenshot as ImageGrab
from PIL import Image
import pytesseract
import time
from numpy import asarray

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

kg = 0.0

def get_kg_max(saco_bbox):
    saco = ImageGrab.grab(bbox=saco_bbox)
    #saco = asarray(saco)
    saco.save('saco.jpg', 'jpeg')

    try:
        texto = pytesseract.image_to_string(Image.open('saco.jpg'))
        #texto = pytesseract.image_to_string(saco)

        kg_atual, kg_max = texto.split('/')

        kg, str_kg = kg_max.split('k')
        kg = float(kg)
        return kg
    
    except:
        return 100.0

def atualizar(saco_bbox):
    saco = ImageGrab.grab(bbox=saco_bbox)
    #saco = asarray(saco)
    saco.save('saco.jpg', 'jpeg')

    try:
        texto = pytesseract.image_to_string(Image.open('saco.jpg'))
        #texto = pytesseract.image_to_string(saco)

        kg_atual, kg_max = texto.split('/')
        kg = float(kg_atual)
        if kg != None:
            return kg
    
    except:
        pass



    



