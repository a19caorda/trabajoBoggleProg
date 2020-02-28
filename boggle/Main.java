package boggle;

import boggle.juego.Partida;
import boggle.utiles.Teclado;

class Main {

  public static void main(String[] args) {
    
    int jug = Teclado.readInt("¿Cuántos jugadores hay? ");
    int rondas = Teclado.readInt("¿Cuántas rondas se jugarán? ");
    Teclado.readString();
    Partida p = new Partida(jug, rondas);
    p.iniciarPartida();


    Teclado.close();
    
    if ( Partida.getPartidasCreadas() == 1) {
      System.out.println("Has jugado "+ Partida.getPartidasCreadas()+" partida." );
    } else {
      System.out.println("Has jugado "+ Partida.getPartidasCreadas()+" partidas." );
    }
  }

}