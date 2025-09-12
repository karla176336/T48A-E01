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

def asistencia_dispersion():
    """
    La aistencia a los 10 últimos partidos en casa de las Águilas de Baltimore fue la siguiente:

    [20100, 24500, 31600, 28400, 49500, 19350, 25600, 30600, 11300, 28560]

    Calcule el rango, la varianza y la desviación stándard para estos datos
    Regrese una tupla con el siguiente orden, como se muestra a continuación:
    """
    datos = np.array([20100, 24500, 31600, 28400, 49500, 19350, 25600, 30600, 11300, 28560])
    rango = np.ptp(datos) # Peak-to-peak range
    varianza = np.var(datos)
    desv_est = np.std(datos)
    return (rango, varianza, desv_est)

def histograma_np():
    """
    Nota: regrese el histograma generado con la función de numpy, no genere la gráfica
    """
    calificaciones = [7.9, 7.8, 7.8, 6.7, 7.6, 8.7, 8.5, 7.3, 6.6, 9.9, 8.4, 7.2,
                     6.6, 5.7, 9.4, 8.4, 7.2, 6.3, 5.1, 4.8, 5.0, 6.1, 7.1, 8.2,
                     9.3, 10.0, 8.9]
    hist, bin_edges = np.histogram(calificaciones)
    return hist, bin_edges


def correlacion():
    tamaño = np.array([100, 120, 140, 160, 180, 200, 220, 240, 260, 280])
    precio = np.array([1305710, 1658277, 1894167, 2136552, 2298267, 2553624, 2780503, 3289726, 3472743, 3779477])
    coeficiente_pearson = np.corrcoef(tamaño, precio)[0, 1]
    return coeficiente_pearson

# Regresa una cadena de caracteres en cada función

def problema_especifico():
    respuesta = "para que no haya como que trampa en las cosas"

def importancia():
    respuesta = ""

def objetivos():
    respuesta = ""

def tipo_de_datos():
    respuesta = ""
