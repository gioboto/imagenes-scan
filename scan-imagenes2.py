import os
import threading

import leeguarda



def procesar_carpeta(carpeta, resultados):
    """lee las carpetas dentro del directorio y llama la funciòn para leer los atributos de los archvios de imagen

    Args:
        carpeta (string): lee la carpeta
        resultados (dictionary): diccionario de atributos
    """    
    for nombre_archivo in os.listdir(carpeta):
        ruta_archivo = os.path.join(carpeta, nombre_archivo)
        if os.path.isfile(ruta_archivo): #and nombre_archivo.lower().endswith(('.jpg', '.jpeg', '.png')):
            atributos = leeguarda.obtiene_atributos_imagen(ruta_archivo)
            if atributos:
                resultados.append(atributos)
               # print(ruta_archivo)
        elif os.path.isdir(ruta_archivo):
            procesar_carpeta(ruta_archivo, resultados)

def procesar_carpeta_principal(carpeta_principal, nombre_archivo_json):
    """Llama a función procesar_carpeta, y por meido de hilos guarda los resultados con la función leeguarda.guarda_json

    Args:
        carpeta_principal (string): _description_
        nombre_archivo_json (string): _description_
    """    
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
    # Carpeta principal que se  quiere procesar .
    carpeta_principal = "/home/usuario/Downloads/"
    #carpeta_principal = "/home/usuariopy/imagenes-zapatos/rfzs-2023-11-09/"
    # Nombre del archivo JSON de salida
    nombre_archivo_json = "resultados.json"

    procesar_carpeta_principal(carpeta_principal, nombre_archivo_json)

