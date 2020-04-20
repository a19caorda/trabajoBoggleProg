from boggle.cubilete import Cubilete
import time
import requests

"""
 * Clase Partida.
 * 
 * Atributos: -maxRondas <-- Almacena el número máximo de rondas que puede tener
 * una partida. -partidasCreadas <-- Almacena un número entero que representa
 * las veces que se han inicializado partidas. -jugadores[] <-- Array de objetos
 * de tipo Jugador. -numRondas <-- Número entero.
 * 
 * Métodos: -iniciarPartida <-- Se encarga de inicializar la partida y gestionar
 * los turnos de los jugadores. -decideGanador <-- Lee la puntuación de los
 * jugadores de la partida y devuelve el que tenga la puntuación más alta.
 * 
 * @author David Fontalba
 * @version 1.1.
"""


class Partida:
    # Atributos de la clase, el número de partidas creadas.
    __MAXRONDAS = 5
    __partidasCreadas = 0

    # Atributos de la partida.
    __jugadores = []
    __numRondas = -1
    __cubilite = Cubilete()

    def __init__(self, numRondas, jugadores):
        self.__partidasCreadas += 1
        self.__numRondas = min(self.__MAXRONDAS, numRondas)

        self.__jugadores = jugadores

    def iniciarPartida(self):

        # Bucle para las rondas
        for i in range(0, self.__numRondas):
            print("Prepárate, la ronda " + (i + 1) + " va a comenzar.")

            # Bucle para los turnos
            for j in self.__jugadores:
                print("Es el turno de " + j + ".")
                # Añadida tirada de dado y muestra del resultado
                self.__cubilete.tirarDados()
                print(self.cubilete.toString())
                # Quitamos las repeticiones
                palabras = j.inicioTurno()
                print("\nFin del turno " + (j + 1) + ".")

                palabrasProcesadas = comprueba(palabras)

                print("Palabras válidas")
                for palabraProcesada in palabrasProcesadas:
                    print(" - " + palabraProcesada)

                j.sumaPuntuacion(sumaPuntos(palabrasProcesadas))

                time.sleep(1)

            print("Fin de la ronda " + (i + 1) + ".")

        decideGanador()

    def decideGanador(self):
        ganador = []  # Almacena la posición del jugador que tiene más
        # puntuación
        aux = 0  # Almacena la puntuación máxima

        # Bucle para leer la puntuación de los jugadores
        for (i, j) in enumerate(self.__jugadores):

            # Si el jugador a leer tiene más puntuación
            if (j.getPuntuacion() > aux):
                ganador.clear()
                ganador.add(i)
                aux = j.getPuntuacion()

                # Si el jugador a leer tiene la misma puntuación
            elif (j.getPuntuacion() == aux):
                ganador.add(i)

        # Si hay más de un ganador
        if (ganador.size() > 1):
            print("Felicidades a los ganadores, ", end="")

            for i in ganador:
                # El último ganador de la lista
                if (i + 1 == ganador.size()):
                    print("y " + self.jugadores[i].getNombre() + ".")

                    # El resto de ganadores
                else:
                    print(self.jugadores[i].getNombre() + ", ", end="")
            # Si solo hay un ganador
            else:
                print("Felicidades " + self.jugadores[ganador[0]].getNombre() + ", ¡Has ganado!")

        print("Recuento de puntuaciones: ")
        for jugador in self.__jugadores:
            print(jugador.getNombre() + ": " + jugador.getPuntuacion())

    """
    comprueba se encarga de comprobar que las palabras sean correctas y filtra
    las incorrectas.
    
    @param aFiltrar La lista de palabras no filtradas
    @return La lista de palabras filtrada
  """

    def comprueba(self, aFiltrar):

        palabrasFiltradas = []

        for palabraNoFiltrada in aFiltrar:

            if (len(palabraNoFiltrada) < 3 and len(palabraNoFiltrada) > 23):
                continue

            palabraNoFiltrada = comprobarExistenciaPalabra(palabraNoFiltrada)

            if (palabraNoFiltrada.isEmpty()):
                continue

            palabraNoFiltrada = comprobarMatrizBienFormada(palabraNoFiltrada)

            if (palabraNoFiltrada.isEmpty()):
                continue

            palabrasFiltradas.add(palabraNoFiltrada)

        return palabrasFiltradas

    """
  sumaPuntos se encarga de sumar los puntos de las palabras
  @param palabras La lista de palabras que ya ha sido filtrada
  @return La suma de lo que puntúa cada palabra
  """

    def sumaPuntos(self, palabras):

        resultadoFinal = 0

        for palabra in palabras:
            if palabra.length() in [0, 1, 2, 3]:
                pass
            elif palabra.length() == 4:
                resultadoFinal += 1
            elif palabra.length() == 5:
                resultadoFinal += 2
            elif palabra.length() == 6:
                resultadoFinal += 3
            elif palabra.length() == 7:
                resultadoFinal += 5
            else:
                resultadoFinal += 11

        return resultadoFinal

    def comprobarExistenciaPalabra(self, palabraAFiltrar: str):

        try:

            url = f"https://dle.rae.es/{palabraAFiltrar.lower()}"

            conn = requests.get(url)

            exists = f"La palabra <b>{palabraAFiltrar.lower()}</b> no está en el Diccionario." in conn.text
            if  exists:
                return ""

        except:
            return ""

        return palabraAFiltrar

    def comprobarMatrizBienFormada(self, palabra):
        c = cubilete.caras
        palabra = palabra.toUpperCase()
        validador = ""

        for x in range(0, 5):
            for y in range(0, 5):
                newX = x
                newY = y
                for letraPos in palabra:
                    if (c[newX][newY] == (palabra.charAt(letraPos))):

                        validador += c[newX][newY]
                        if (validador.equals(palabra)):
                            return palabra

                        try:
                            if (c[newX + 1][newY] == (palabra.charAt(letraPos + 1))):
                                newX = newX + 1
                                continue

                        except IndexError:
                            pass
                        try:
                            if (c[newX - 1][newY] == (palabra.charAt(letraPos + 1))):
                                newX = newX - 1

                        except IndexError:
                            pass
                        try:
                            if (c[newX][newY + 1] == (palabra.charAt(letraPos + 1))):
                                newY = newY + 1
                                continue

                        except IndexError:
                            pass
                        try:
                            if (c[newX][newY - 1] == (palabra.charAt(letraPos + 1))):
                                newY = newY - 1
                                continue

                        except IndexError:
                            pass
                        try:
                            if (c[newX + 1][newY + 1] == (palabra.charAt(letraPos + 1))):
                                newY = newY + 1
                                newX = newX + 1
                                continue

                        except IndexError:
                            pass
                        try:
                            if (c[newX + 1][newY - 1] == (palabra.charAt(letraPos + 1))):
                                newY = newY - 1
                                newX = newX + 1
                                continue

                        except IndexError:
                            pass
                        try:
                            if (c[newX - 1][newY + 1] == (palabra.charAt(letraPos + 1))):
                                newY = newY + 1
                                newX = newX - 1
                                continue

                        except IndexError:
                            pass
                        try:
                            if (c[newX - 1][newY - 1] == (palabra.charAt(letraPos + 1))):
                                newY = newY - 1
                                newX = newX - 1
                                continue

                        except IndexError:
                            pass
                    else:
                        validador = ""
                        break

                    letraPos += 1

        return ""

    # Getters

    def getPartidasCreadas(self):
        return self.__partidasCreadas
