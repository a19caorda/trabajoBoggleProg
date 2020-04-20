from boggle.partida import Partida
from boggle.jugador import Jugador

if __name__ == "__main__":

    jug = int(input("¿Cuántos jugadores hay? "))
    rondas = int(input("¿Cuántas rondas se jugarán? "))

    jugadores = [];

    for i in range(0, jug):
        aux = input("Introduce el nombre del jugador " + (i + 1) + ": ")
        j = Jugador(aux)
        jugadores.append(j)


    p = Partida(rondas, jugadores);
    p.iniciarPartida();

    if (Partida.getPartidasCreadas() == 1) :
        print("Has jugado " + Partida.getPartidasCreadas() + " partida.");
    else:
        print("Has jugado " + Partida.getPartidasCreadas() + " partidas.");
