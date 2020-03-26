import threading
import time
from pynput.keyboard import Key, Controller as KeyboardController

class Jugador:

    __turno = 10
    __nombre = ""
    __puntuacion = 0
    __recogiendo = False

    def __init__(self, nombre):
        self.__nombre = nombre

    @property
    def nombre(self):
        return self.__nombre

    @property
    def puntuacion(self):
        return self.__puntuacion

    def sumarPuntuacion(self, suma):
        self.__puntuacion += suma

    def recoger_palabras(self, palabras: list):
        while self.__recogiendo:
            palabras.append( input(f"Palabra {len(palabras) + 1:02}: ") )
        

    def inicioTurno(self):
        palabras = []
        self.__recogiendo = True
        thread = threading.Thread(target=self.recoger_palabras, args=(palabras,))
        thread.start()

        time.sleep(self.__turno)
        self.__recogiendo = False

        kbCtrl = KeyboardController()
        kbCtrl.press(Key.enter)
        kbCtrl.release(Key.enter)
        print()

        return list(set(palabras))

    def __str__(self):
        return self.__nombre
