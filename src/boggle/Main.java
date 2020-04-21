package boggle;

import boggle.juego.Jugador;
import boggle.juego.Partida;
import boggle.utiles.Teclado;

class Main {

  /**
   * 
   * Punto de entrada a la aplicación
   * 
   * @param args Argumentos que recibe desde la consola
   * 
   */
  public static void main(String[] args) {

    Teclado teclado = new Teclado();

    do {
      int jug = teclado.readInt("¿Cuántos jugadores hay? ");
      teclado.readString();

      Jugador[] jugadores = new Jugador[jug];
      int rondas = teclado.readInt("¿Cuántas rondas se jugarán? ");

      for (int i = 0; i < jugadores.length; i++) {
        String aux = teclado.readString("Introduce el nombre del jugador " + (i + 1) + ": ");
        Jugador j = new Jugador(aux);
        jugadores[i] = j;
      }

      Partida p = new Partida(rondas, jugadores);
      p.iniciarPartida();
      
      if (Partida.getPartidasCreadas() == 1) {
        System.out.println("Has jugado " + Partida.getPartidasCreadas() + " partida.");
      } else {
        System.out.println("Has jugado " + Partida.getPartidasCreadas() + " partidas.");
      }
      
    } while (teclado.readString("Quieres jugar otra partida? (Si/No) ").toLowerCase().equals("si"));

    teclado.close();

  }

}