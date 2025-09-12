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

def asistencia_dispersion():
    """
    La aistencia a los 10 últimos partidos en casa de las Águilas de Baltimore fue la siguiente:

    [20100, 24500, 31600, 28400, 49500, 19350, 25600, 30600, 11300, 28560]

    Calcule el rango, la varianza y la desviación stándard para estos datos
    Regrese una tupla con el siguiente orden, como se muestra a continuación:
    """
    datos = np.array([20100, 24500, 31600, 28400, 49500, 19350, 25600, 30600, 11300, 28560])
    rango = np.ptp(datos) 
    varianza = np.var(datos)
    desv_est = np.std(datos)
    return (rango, varianza, desv_est)
