#!/usr/bin/env python3

import os
from PIL import Image
import json

#ruta = "/home/usuario/Downloads/images.jpeg"
def obtiene_atributos_imagen(ruta):
    try:
        with Image.open(ruta) as img:
            ancho, alto = img.size
            modo = img.mode
            im = img.im
            format = img.format
            formatd = img.format_description
            info = img.info
            palette = img.palette
            
            #print({'nombre': os.path.basename(ruta), 'ancho': ancho, 'alto': alto, 'modo': modo, 'im' : im, 'format' : format, 'formatd': formatd, 'info': info, 'palette' : palette})
            return({'ruta': ruta, 'nombre': os.path.basename(ruta), 'ancho': ancho, 'alto': alto, 'modo': modo, 'im' : im, 'format' : format, 'formatd': formatd, 'info': info, 'palette' : palette})
    except Exception as ex:
        return {'nombre': os.path.basename(ruta), 'error': str(ex)}
    

def guarda_json(datos, nombre_archivo):
    try:
        with open(nombre_archivo,'w') as archivo:
            json.dump(datos, archivo, indent=2)
        print(f"Satos cuardafod en {nombre_archivo}")
    except Exception as e:
        print(f"Error en guardar jcon: {e}")
            