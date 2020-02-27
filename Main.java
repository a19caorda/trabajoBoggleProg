import boggle.Partida;
import boggle.Teclado;

class Main {

  public static void main(String[] args) {

    do{
      System.out.print("Cuantos jugadores hay? ");
      int jug = Teclado.getTeclado().readInt();
      Teclado.getTeclado().readString();
      System.out.print("Cuantas rondas se jugaran? ");
      int rondas = Teclado.getTeclado().readInt();
      Teclado.getTeclado().readString();

      Partida p = new Partida(jug, rondas);
      p.iniciarPartida();

      System.out.print("Quieres seguir? ");
    }while(Teclado.getTeclado().readString().toLowerCase() == "si");


    Teclado.getTeclado().close();
  }

}