import flask 
from flask import request, jsonify
import logging
import json
import time
from pynput.keyboard import Key, Listener
from threading import Thread

from data import kg
from data import fisgou
from data import linha

app = flask.Flask(__name__)
app.config["DEBUG"] = True

##### Definicao das classes #####

class Config:
   def __init__(self):
        #positions
        self.next_morning_button = (1283, 869)
        self.extend_button = (1095, 677)

        #self.saco_bbox = (115,175,254,202)
        self.saco_bbox = (2074,237,2261,274)

        #self.line_bbox = (2141,917,2300,1014)
        #self.line_bbox = (3910,1206,3993,1299)
        self.line_bbox = (3938,1230,4120,1353)

        #self.fisgar_pos = (2411, 953)
        #self.fisgar_pos = (4286, 1276)

        self.fisgar_pos = (4273, 1274, 4291, 1280)

        #config vars
        self.casting_time = 2
        self.velocidade_recolhimento = 2
        self.kg_max = 100.0

        logging.warning("Init Config !!!")

   def toJSON(self):
       return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

#class Saco(Thread):
class Saco():    
    def __init__(self, config):
        #super().__init__()
        self.kg_atual = 0.0
        self.config = config
    def run(self):
        #logging.warning("Start saco!!!")
        #while True:
        kg_ = kg.atualizar(self.config.saco_bbox)
        if kg_ != None:
          self.kg_atual = kg_

    def toJSON(self):
       return { "kg_atual": self.kg_atual }


#class Line(Thread):
class Line():
    def __init__(self,config):
        #super().__init__()
        self.n_line = 0
        self.config = config

    def run(self):
       #logging.warning("Start linha!!!")
       #while True:
       line_ = linha.atualizar(self.config.line_bbox)
       
       if line_ != None:
            self.n_line = line_       

    def toJSON(self):
       return { "n_line": self.n_line }

#class Fisgar(Thread):
class Fisgar():
    def __init__(self, config):
        super().__init__()
        self.fisgou = False
        self.config = config
    def run(self):
        logging.warning("Start fisgar!!!")
        #while True:
        self.fisgou = fisgou.atualizar(self.config.fisgar_pos)

    def toJSON(self):
       return { "fisgou": self.fisgou }



# route Config
@app.route('/config', methods=['GET'])
def getConfig():
    #return jsonify(config.toJSON())    
    return configure.toJSON()    
   
# route Config
@app.route('/saco', methods=['GET'])
def getSaco():
    saco = Saco(configure)
    saco.run()
    return jsonify(saco.toJSON())   
    

# route Config
@app.route('/linha', methods=['GET'])
def getLinha():
    line = Line(configure)
    line.run()
    return jsonify(line.toJSON())   

# route Config
@app.route('/fisga', methods=['GET'])
def getFisga():
    fisgar = Fisgar(configure)
    fisgar.run()
    return jsonify(fisgar.toJSON())   

def iniciar():    
   #start = time.strftime("%d.%m.%Y-%H:%M:%S")
   #print('Iniciar pesca....', start )
   logging.warning('Server: Iniciar pesca....')
   try:
        #saco.start()
        #line.start()
        #fisgar.start()
        #app.run(threaded=True)        
        app.run()        
        
   except KeyboardInterrupt:
        #end = time.strftime("%d.%m.%Y-%H:%M:%S")
        #print('Finalizar pesca....', end) 
        logging.warning('Server: Finalizar pesca....' )
        pass        
        

configure = Config()
#saco = Saco(configure)
#line = Line(configure)
#fisgar = Fisgar(configure)
iniciar()    
