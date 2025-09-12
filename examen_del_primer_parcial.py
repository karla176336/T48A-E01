import numpy as np

# Importante: verifica que tu nombre y número de matrícula esten correctos

nombre = "Karla Julieta Torres Elias"
numero_de_matricula = 176336
fecha = '2025-11-09'

def capitalizacion():
    datos = np.array([17, 21, 44, 50, 79, 86, 140, 178, 203])
    media = np.mean(datos)
    mediana = np.median(datos)
    elementos_unicos, conteos = np.unique(datos, return_counts=True)
    moda = elementos_unicos[np.argmax(conteos)]
    desv_est = np.std(datos)
    return (media, mediana, moda, desv_est)
