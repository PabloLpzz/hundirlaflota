from clases import Tablero
from funciones import generar_disparo_aleatorio
from variables import DIMENSIONES

def main():
    print("Bienvenido a Hundir la Flota")

    # Inicialización de los tableros
    tablero_jugador = Tablero("Jugador")
    tablero_maquina = Tablero("Máquina")

    # Colocación de los barcos
    tablero_jugador.colocar_barcos()
    tablero_maquina.colocar_barcos()

    turno_jugador = True  # El juego comienza con el turno del jugador

    while tablero_jugador.quedan_barcos() and tablero_maquina.quedan_barcos():
        if turno_jugador:
            print("Tu turno")
            tablero_maquina.imprimir_tablero(mostrar_barcos=False)
            try:
                fila = int(input("Fila: ")) - 1
                columna = int(input("Columna: ")) - 1

                # Comprobamos si ya se ha disparado a esa coordenada
                if tablero_maquina.tablero_disparos[fila, columna] != 0:
                    print("Ya has disparado a esa posición. Elige otra coordenada.")
                    continue

                if tablero_maquina.realizar_disparo(fila, columna):
                    print("¡Tocado!")
                    if not tablero_maquina.quedan_barcos():
                        print("¡Has ganado!")
                        break
                else:
                    print("Agua")
                    turno_jugador = False
            except IndexError:
                print("Coordenadas fuera del tablero, por favor intenta de nuevo.")
            except ValueError:
                print("Por favor, introduce números válidos.")
        else:
            print("Turno de la máquina")
            fila, columna = generar_disparo_aleatorio(DIMENSIONES)
            if tablero_jugador.realizar_disparo(fila, columna):
                print("La máquina te ha tocado")
                if not tablero_jugador.quedan_barcos():
                    print("La máquina ha ganado")
                    break
            else:
                turno_jugador = True

if __name__ == "__main__":
    main()
