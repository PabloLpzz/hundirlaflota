import numpy as np
import random
from variables import DIMENSIONES, BARCOS

class Tablero:
    def __init__(self, jugador_id):
        self.jugador_id = jugador_id
        self.dimensiones = DIMENSIONES
        self.barcos = BARCOS
        self.tablero = np.zeros(self.dimensiones, dtype=int)  # 0 representa agua
        self.tablero_disparos = np.zeros(self.dimensiones, dtype=int)  # 0 representa disparos no realizados

    def colocar_barcos(self):
        """Coloca todos los barcos en el tablero."""
        for eslora, cantidad in self.barcos.items():
            for _ in range(cantidad):
                self.colocar_barco(eslora)

    def colocar_barco(self, eslora):
        """Coloca un barco de una eslora dada en el tablero."""
        colocado = False
        while not colocado:
            fila = random.randint(0, self.dimensiones[0] - 1)
            columna = random.randint(0, self.dimensiones[1] - 1)
            orientacion = random.choice(['horizontal', 'vertical'])

            if self.puede_colocar_barco(fila, columna, eslora, orientacion):
                self.posicionar_barco(fila, columna, eslora, orientacion)
                colocado = True

    def puede_colocar_barco(self, fila, columna, eslora, orientacion):
        """Verifica si es posible colocar un barco en la posición y orientación dadas."""
        if orientacion == 'horizontal':
            if columna + eslora > self.dimensiones[1]:
                return False
            return np.all(self.tablero[fila, columna:columna + eslora] == 0)
        else:  # orientacion vertical
            if fila + eslora > self.dimensiones[0]:
                return False
            return np.all(self.tablero[fila:fila + eslora, columna] == 0)

    def posicionar_barco(self, fila, columna, eslora, orientacion):
        """Posiciona un barco en el tablero."""
        if orientacion == 'horizontal':
            self.tablero[fila, columna:columna + eslora] = 1
        else:  # orientacion vertical
            self.tablero[fila:fila + eslora, columna] = 1

    def imprimir_tablero(self, mostrar_barcos=False):
        """Imprime el tablero con números de fila y columna para fácil referencia."""
        # Encabezado con los números de columna
        print("   " + " ".join(str(i+1) for i in range(self.dimensiones[1])))
        for fila in range(self.dimensiones[0]):
            # Números de fila al inicio de cada una
            print(f"{fila+1:2}", end=" ")
            for columna in range(self.dimensiones[1]):
                # Se decide qué símbolo imprimir basado en el estado del tablero y los disparos
                if mostrar_barcos and self.tablero[fila][columna] == 1:
                    print('B', end=' ')
                elif self.tablero_disparos[fila][columna] == 2:
                    print('X', end=' ')  # X representa disparo acertado a un barco
                elif self.tablero_disparos[fila][columna] == 1:
                    print('*', end=' ')  # * representa disparo fallido
                else:
                    print('.', end=' ')  # . representa agua o desconocido
            print()

    def realizar_disparo(self, fila, columna):
        """Realiza un disparo en las coordenadas dadas y actualiza el tablero de disparos."""
        if self.tablero[fila, columna] == 1:  # Hay un barco
            self.tablero_disparos[fila, columna] = 2  # Marca el acierto
            self.tablero[fila, columna] = 0  # Quita el barco del tablero principal
            return True
        else:
            self.tablero_disparos[fila, columna] = 1  # Marca el disparo fallido
            return False

    def quedan_barcos(self):
        """Verifica si quedan barcos en el tablero."""
        return np.any(self.tablero == 1)
