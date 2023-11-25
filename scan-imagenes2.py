import os
import threading
#from PIL import Image
#import json
import leeguarda
"""
def obtener_atributos_imagen(ruta_imagen):
    try:
        with Image.open(ruta_imagen) as img:
            ancho, alto = img.size
            modo = img.mode
            return {"nombre": os.path.basename(ruta_imagen), "ruta": ruta_imagen, "ancho": ancho, "alto": alto, "modo": modo}
    except Exception as e:
        print(f"No se pudo procesar la imagen {ruta_imagen}. Error: {str(e)}")
        return None
"""


def procesar_carpeta(carpeta, resultados):
    for nombre_archivo in os.listdir(carpeta):
        ruta_archivo = os.path.join(carpeta, nombre_archivo)
        if os.path.isfile(ruta_archivo): #and nombre_archivo.lower().endswith(('.jpg', '.jpeg', '.png')):
            atributos = leeguarda.obtiene_atributos_imagen(ruta_archivo)
            if atributos:
                resultados.append(atributos)
               # print(ruta_archivo)
        elif os.path.isdir(ruta_archivo):
            procesar_carpeta(ruta_archivo, resultados)
"""
def guardar_en_json(resultados, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo_json:
        json.dump(resultados, archivo_json, indent=4)
"""
def procesar_carpeta_principal(carpeta_principal, nombre_archivo_json):
    resultados = []
    hilos = []
    cont = 0
    for carpeta, _, _ in os.walk(carpeta_principal):
        hilo = threading.Thread(target=procesar_carpeta, args=(carpeta, resultados))
        hilos.append(hilo)
        hilo.start()
        cont += 1
        print(cont)

    for hilo in hilos:
        hilo.join()

    leeguarda.guarda_json(resultados, nombre_archivo_json)

if __name__ == "__main__":
    # Carpeta principal que quieres procesar .
    carpeta_principal = "/home/usuario/Downloads/"
    #carpeta_principal = "/home/usuariopy/imagenes-zapatos/rfzs-2023-11-09/"
    # Nombre del archivo JSON de salida
    nombre_archivo_json = "resultados.json"

    procesar_carpeta_principal(carpeta_principal, nombre_archivo_json)

