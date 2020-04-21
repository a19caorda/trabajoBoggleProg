from boggle.cubilete import Cubilete
import time
import requests

from boggle import cubilete

"""
 * Clase Partida.
 * 
 * Atributos: -maxRondas <-- Almacena el número máximo de rondas que puede tener
 * una partida. -partidasCreadas <-- Almacena un número entero que representa
 * las veces que se han inicializado partidas. -jugadores[] <-- Array de objetos
 * de tipo Jugador. -numRondas <-- Número entero.
 * 
 * Métodos: -iniciar_partida <-- Se encarga de inicializar la partida y gestionar
 * los turnos de los jugadores. -decide_ganador <-- Lee la puntuación de los
 * jugadores de la partida y devuelve el que tenga la puntuación más alta.
 * 
 * @author David Fontalba
 * @version 1.1.
"""

class Partida:
    """
    @param numRondas El número de rondas que se jugará
    @param jugadores Los jugadores que van a participar
    """
    # Atributos de la clase, el número de partidas creadas.
    __MAXRONDAS = 5
    __partidas_creadas = 0

    # Atributos de la partida.
    __jugadores = []
    __num_rondas = -1
    __cubilete = Cubilete()

    def __init__(self, num_rondas, jugadores):
        self.__class__.__partidas_creadas += 1
        self.__num_rondas = min(self.__MAXRONDAS, num_rondas)

        self.__jugadores = jugadores


    def iniciar_partida(self):
        """
        iniciar_partida se encarga del desarrollo de los turnos, y al final llama a {@link decide_ganador}
        """

        # Bucle para las rondas
        for i in range(0, self.__num_rondas):
            print("Prepárate, la ronda " + str(i + 1) + " va a comenzar.")

            # Bucle para los turnos
            for j in self.__jugadores:
                print("Es el turno de " + str(j) + ".")
                # Añadida tirada de dado y muestra del resultado
                self.__cubilete.tirar_dados()
                print(self.__cubilete)
                # Quitamos las repeticiones
                palabras = j.inicio_turno()
                print("\nFin del turno " + str(i + 1) + ".")

                palabras_procesadas = self.comprueba(palabras)

                print("Palabras válidas")
                for palabraProcesada in palabras_procesadas:
                    print(" - " + palabraProcesada)

                j.sumar_puntuacion(self.suma_puntos(palabras_procesadas))

                time.sleep(1)

            print("Fin de la ronda " + str(i + 1) + ".")

        self.decide_ganador()
    def decide_ganador(self):


        ganador = []  # Almacena la posición del jugador que tiene más
        # puntuación
        aux = 0  # Almacena la puntuación máxima

        # Bucle para leer la puntuación de los jugadores
        for (i, j) in enumerate(self.__jugadores):

            # Si el jugador a leer tiene más puntuación
            if j.puntuacion > aux:
                ganador.clear()
                ganador.append(i)
                aux = j.puntuacion

                # Si el jugador a leer tiene la misma puntuación
            elif j.puntuacion == aux:
                ganador.append(i)

        # Si hay más de un ganador
        if (len(ganador) > 1):
            print("Felicidades a los ganadores, ", end="")

            for i in ganador:
                # El último ganador de la lista
                if (i + 1 == len(ganador)):
                    print("y " + self.jugadores[i].nombre + ".")

                    # El resto de ganadores
                else:
                    print(self.jugadores[i].nombre + ", ", end="")
        # Si solo hay un ganador
        else:
            print("Felicidades " + self.jugadores[ganador[0]].nombre + ", ¡Has ganado!")

        print("Recuento de puntuaciones: ")
        for jugador in self.__jugadores:
            print(jugador.nombre + ": " + str(jugador.puntuacion))


    def comprueba(self, a_filtrar):
        """
        comprueba se encarga de comprobar que las palabras sean correctas y filtra
        las incorrectas.
        
        @param aFiltrar La lista de palabras no filtradas
        @return La lista de palabras filtrada
        """
        palabras_filtradas = []

        for palabra_no_filtrada in a_filtrar:

            if (len(palabra_no_filtrada) < 3 or len(palabra_no_filtrada) > 23):
                continue

            palabra_no_filtrada = self.comprobar_existencia_palabra(palabra_no_filtrada)

            if (palabra_no_filtrada == ""):
                continue

            palabra_no_filtrada = self.comprobar_matriz_bien_formada(palabra_no_filtrada)

            if (palabra_no_filtrada == ""):
                continue

            palabras_filtradas.append(palabra_no_filtrada)

        return palabras_filtradas


    def suma_puntos(self, palabras):
        """
        suma_puntos se encarga de sumar los puntos de las palabras
        
        @param palabras La lista de palabras que ya ha sido filtrada
        @return La suma de lo que puntúa cada palabra
        """

        resultado_final = 0

        for palabra in palabras:
            if len(palabra) in [0, 1, 2, 3]:
                pass
            elif len(palabra) == 4:
                resultado_final += 1
            elif len(palabra) == 5:
                resultado_final += 2
            elif len(palabra) == 6:
                resultado_final += 3
            elif len(palabra) == 7:
                resultado_final += 5
            else:
                resultado_final += 11

        return resultado_final
    def comprobar_existencia_palabra(self, palabra_a_filtrar: str):
        """
        comprobar_existencia_palabra comprueba a través de un api la existencia de la palabra
        que llega a través del argumento palabraAFiltrar
        
        @param palabraAFiltrar La palabra a comprobar si existe
        @return Devulve la palabra si existe, en caso contrario, devuelve una cadena vacía
        """

        try:

            url = f"https://dle.rae.es/{palabra_a_filtrar.lower()}"

            conn = requests.get(url)

            exists = f"La palabra <b>{palabra_a_filtrar.lower()}</b> no está en el Diccionario." in conn.text
            if  exists:
                return ""

        except:
            return ""

        return palabra_a_filtrar

    def comprobar_matriz_bien_formada(self, palabra):
        """
        Compruba si la palabra está bien formada respecto a lo que dicen las normas del Boggle,
        es decir que que letra de la palabra tenga que estar continua o adyadcente tanto a la
        siguiente como a la anterior.
        
        @param palabra Palabra para comprobar
        @return Devulve la palabra si está bien formada, en caso contrario, devuelve una {@link String} vacía
        """
        c = self.__cubilete.caras
        palabra = palabra.upper()
        validador = ""

        for x in range(0, 5):
            for y in range(0, 5):
                new_x = x
                new_y = y
                for letra_pos in range(len(palabra)):
                    if c[new_x][new_y] == palabra[letra_pos]:

                        validador += c[new_x][new_y]
                        if validador == palabra:
                            return palabra

                        try:
                            if c[new_x + 1][new_y] == palabra[letra_pos + 1]:
                                new_x = new_x + 1
                                continue

                        except IndexError:
                            pass
                        try:
                            if c[new_x - 1][new_y] == palabra[letra_pos + 1]:
                                new_x = new_x - 1

                        except IndexError:
                            pass
                        try:
                            if c[new_x][new_y + 1] == palabra[letra_pos + 1]:
                                new_y = new_y + 1
                                continue

                        except IndexError:
                            pass
                        try:
                            if c[new_x][new_y - 1] == palabra[letra_pos + 1]:
                                new_y = new_y - 1
                                continue

                        except IndexError:
                            pass
                        try:
                            if c[new_x + 1][new_y + 1] == palabra[letra_pos + 1]:
                                new_y = new_y + 1
                                new_x = new_x + 1
                                continue

                        except IndexError:
                            pass
                        try:
                            if c[new_x + 1][new_y - 1] == palabra[letra_pos + 1]:
                                new_y = new_y - 1
                                new_x = new_x + 1
                                continue

                        except IndexError:
                            pass
                        try:
                            if c[new_x - 1][new_y + 1] == palabra[letra_pos + 1]:
                                new_y = new_y + 1
                                new_x = new_x - 1
                                continue

                        except IndexError:
                            pass
                        try:
                            if c[new_x - 1][new_y - 1] == palabra[letra_pos + 1]:
                                new_y = new_y - 1
                                new_x = new_x - 1
                                continue

                        except IndexError:
                            pass
                    else:
                        validador = ""
                        break

                    letra_pos += 1

        return ""

    # Getters
    def get_partidas_creadas(self):
        """
        @return El número de partidas creadas
        """
        return self.__class__.__partidas_creadas