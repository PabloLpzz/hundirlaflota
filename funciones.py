import numpy as np
from clases import Tablero

def generar_disparo_aleatorio(dimensiones):
    fila = np.random.randint(0, dimensiones[0])
    columna = np.random.randint(0, dimensiones[1])
    return fila, columna
