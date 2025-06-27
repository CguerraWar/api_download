from codecs import utf_16_encode, utf_8_decode
import os
import json
import base64

import zlib
import binascii


import sys

x = 1.0
print(sys.getsizeof(x))  # Tamaño del objeto `float`

import struct
print(struct.calcsize('d'))  # Devuelve 8 (bytes)

import math
x = 1.2345678901234567
pp = math.sin(x)  # Resultado:
print(pp)

x = 1.234567890123456789
print(repr(x))  

from mpmath import mp, sin

mp.dps = 50  # 50 dígitos decimales
x = mp.mpf('1.2345678901234567')
print(sin(x))

endpoint_root = 'https://cguerrawar.github.io/api_download/'

# dir      = ["../../../Programer From Sim/", "../../../terralert-station-firmware-teensy/", "../../../terralert-station-firmware-ESP32/"]
# endpoint = ["TestProgramOta", "terralert", "terralert-ESP32"]


dir      = ["../../../terralert-station-firmware-teensy/", "../../../terralert-station-firmware-ESP32/"]
endpoint = ["terralert", "terralert-ESP32"]

idx = 0

dir_need = list() 

for d in dir:
    
    root_dir = os.listdir(d)
    
    dir_util = list()
    
    for fs in root_dir:
        if fs != '.DS_Store' and fs != 'README.md' and fs != 'pymakr.conf' and fs != '.gitignore'  and fs != 'tools' and fs != '.vscode' and fs != '.git' and fs != 'ESP32_GENERIC-20250415-v1.25.0.bin':
            dir_util.append(fs)
            
    count_sub = 0
    
    dir_tree = list()
    
    for fs in dir_util:
        if '.' in fs: 
            dir_tree.append( d + fs)          
        else:
            for nombre_directorio, dirs, ficheros in os.walk(d + fs):                
                for nombre_fichero in ficheros:
                    if nombre_fichero != '.DS_Store':
                        dir_tree.append(nombre_directorio + "/" + nombre_fichero)                 
                        
        
    for fs in dir_tree:
        
        dir_need.append(fs.replace('\\', '/'))
    
    version = ""
    
    for f in dir_need:
        
        if "main.py" in f:
            file = open(f, 'r', encoding='utf-8')
            data = file.read()
            
            #i =  data.find("OtaProgrammer(", 0)
            i = data.find("version", 0)
            
            if i > 0:
                # first =  data.find(",", i) 
                # init = data.find(",", first+1) 
                # end  = data.find(",", init+1) 
                
                first =  data.find('\'', i) 
                end = data.find('\'', first+1) 
                                
                chs = int() 
                
                #version = data[init+1:end].replace('version=','').replace('version =','').replace(' ','').replace('\'','')
                version = data[first+1:end].replace(' ','')
                
                # out = dict()   
                # out['version'] = version 
                
                # files = []
                
                json_config = ""
                
                try:
                    os.stat("../../" + endpoint[idx] + "_config.json")                        
                except:                    
                    conf = dict()
                    
                    for fs in dir_need:
                        conf[fs.replace(d, '')] = 1                      
                        
                    with open("../../" + endpoint[idx] + "_config.json", "w") as outfile: 
                        json.dump(conf, outfile) 
                 
                config = ""

                with open("../../" + endpoint[idx] + "_config.json") as archivo:                  
                    config =  json.load(archivo)
                    
                data_file = str()
                
                data_file +=  f"version:{version}\n"
                
                for fs in dir_need:
                                        
                    is_need_update = True
                    
                    li          = list(config.keys())
                    val_conf    = fs.replace(d,'')

                    if val_conf in li:
                        is_need_update = True if config[val_conf] == 1 else False
                    else:
                        config[val_conf] = 1
                    
                    if is_need_update:
                        data = ""                    
                        with open(fs, 'r') as fichero:
                            data = fichero.read()   
                           
                        compressed_data = zlib.compress(bytearray(data.encode()), 1)
                        
                        data_base64 = binascii.b2a_base64(compressed_data)
                        
                        #ini = binascii.a2b_base64(data_base64)
                        
                        #ddd = zlib.decompress(ini)
                        
                        #data_base64 = base64.b64encode(bytes(data, 'utf-8')) # bytes
                   
                        #dic = dict(patch = fs.replace(d, ''), content = data_base64.decode())

                        data_file += fs.replace(d, '') +'\n'
                        data_file += data_base64.decode()
                        
                        for val in data_file:           
                            chs += ord(val)
                        pp = 1
                        chs = 0
                    
                        # files.append( dic )
                for val in data_file:           
                    chs += ord(val)
                pp = 1
                
                # for val in str(chs):           
                #     chs += ord(val)  
                
                #out['files'] = files 
                data_file += str(chs)               
                
                with open("../../" + endpoint[idx] +  ".json", "w") as outfile: 
                    #json.dump(out, outfile)
                    outfile.write(data_file)
                
                with open("../../" + endpoint[idx] + "_config.json", "w") as outfile: 
                        json.dump(config, outfile, indent = 6)   
    
    dir_need.clear()
    idx += 1
   

tt = 1    
