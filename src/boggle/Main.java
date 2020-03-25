package boggle;

import boggle.juego.Jugador;
import boggle.juego.Partida;
import boggle.utiles.Teclado;

class Main {

  /**
   * Punto de entrada a la aplicación
   */
  public static void main(String[] args) {

    int jug = Teclado.readInt("¿Cuántos jugadores hay? ");
    int rondas = Teclado.readInt("¿Cuántas rondas se jugarán? ");
    Teclado.readString();

    Jugador[] jugadores = new Jugador[jug];

    for (int i = 0; i < jugadores.length; i++) {
      String aux = Teclado.readString("Introduce el nombre del jugador " + (i + 1) + ": ");
      Jugador j = new Jugador(aux);
      jugadores[i] = j;
    }

    Partida p = new Partida(rondas, jugadores);
    p.iniciarPartida();

    Teclado.close();

    if (Partida.getPartidasCreadas() == 1) {
      System.out.println("Has jugado " + Partida.getPartidasCreadas() + " partida.");
    } else {
      System.out.println("Has jugado " + Partida.getPartidasCreadas() + " partidas.");
    }

  }

}