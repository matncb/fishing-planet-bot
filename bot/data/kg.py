import pyscreenshot as ImageGrab
from PIL import Image
import pytesseract
import time
from numpy import asarray

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

kg = 0.0

def get_kg_max(saco_bbox):
<<<<<<< HEAD
    saco = ImageGrab.grab(bbox=saco_bbox)
    #saco = asarray(saco)
    saco.save('saco.jpg', 'jpeg')
=======
    #saco = ImageGrab.grab(bbox=saco_bbox)
    #saco.save('saco.jpg', 'jpeg')
>>>>>>> edb2b3567bd302ea69aed00d23e8a1447e0dcdb7

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

    half = 3
    out = saco.resize([int(half * s) for s in saco.size])
    #out.save('saco.jpg', 'jpeg')

    try:
<<<<<<< HEAD
        texto = pytesseract.image_to_string(Image.open('saco.jpg'))
        #texto = pytesseract.image_to_string(saco)
=======
>>>>>>> edb2b3567bd302ea69aed00d23e8a1447e0dcdb7

        #texto = pytesseract.image_to_string(Image.open('/home/denilso/desenv/fishing-planet/fishing-planet-bot/bot/saco.jpg'))
        #texto = pytesseract.image_to_string(Image.open('saco.jpg'), config='--psm 6')
        texto = pytesseract.image_to_string(out, config='--psm 6')
        print('kg-texto------> ', texto)
        #texto = pytesseract.image_to_string(saco)
        kg_atual, kg_max = texto.split('/')
        kg_atual = kg_atual.replace(',','.')
        kg = float(kg_atual)
        if kg != None:
            return kg
    
    except:
        #print("error-kg")
        pass



    



