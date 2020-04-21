from boggle.partida import Partida
from boggle.jugador import Jugador

if __name__ == "__main__":

    repetir = True
    while repetir:
        jug = int(input("¿Cuántos jugadores hay? "))
        rondas = int(input("¿Cuántas rondas se jugarán? "))

        jugadores = []

        for i in range(0, jug):
            aux = input("Introduce el nombre del jugador " + str(i + 1) + ": ")
            j = Jugador(aux)
            jugadores.append(j)


        p = Partida(rondas, jugadores)
        p.iniciar_partida()

        if (p.get_partidas_creadas() == 1) :
            print("Has jugado " + str(p.get_partidas_creadas()) + " partida.")
        else:
            print("Has jugado " + str(p.get_partidas_creadas()) + " partidas.")

        repetir = input("Quieres jugar otra partida? (Si/No) ").lower() == "si"
