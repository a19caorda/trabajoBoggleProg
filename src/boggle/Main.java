package boggle;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.text.DateFormat;
import java.text.ParseException;
import java.util.Date;

import com.google.gson.Gson;
import com.google.gson.JsonIOException;
import com.google.gson.JsonObject;
import com.google.gson.JsonSyntaxException;

import boggle.juego.Jugador;
import boggle.juego.Partida;
import boggle.utiles.Menu;
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

    File dir = new File("boggleHistorial");
    if (!dir.exists())
      dir.mkdirs();

    Menu menu = new Menu("Boggle", "Jugar", "Ver historial", "Salir");

    for (;;) {

      switch (menu.gestionar()) {
      case 1:
        jugar();
        break;
      case 2:
        resultados();
        break;
      default:
        return;
      }

    }
  }

  private static void resultados() {
    try {

      String aux = Teclado.readString("Introduce el nombre del jugador para ver su historial: ");
      Jugador j = new Jugador(aux);

      j = new Gson().fromJson(new FileReader(j.getHistorialArchivo()), Jugador.class);
      System.out.printf("Historial de %s: \n", j.getNombre());
      
      System.out.println("\tPuntuación acumulada: " + j.getPuntuacion_acumulada());
      System.out.println("\tPuntuación maxima: " + j.getPuntuacion_maxima());
      System.out.println("\tPartidas jugadas: " + j.getPartidas_jugadas());
      System.out.println("\tPartidas ganadas: " + j.getPartidas_ganadas());
      System.out.println("\tPartidas perdidas: " + j.getPartidas_perdidas());

      System.out.println("\tPartidas:");
      j.getPartidas().forEach(element -> {
        JsonObject jObject = (JsonObject) element;
        
        String fecha = jObject.get("fecha").getAsString();
        int p = jObject.get("puntuacion").getAsInt();
        
        System.out.printf("\t\tLa partida jugada el %s conseguistes %d de puntuación\n", fecha, p);
        
      });
      
    } catch (JsonSyntaxException | JsonIOException | FileNotFoundException e) {

    }

  }

  private static void jugar() {
    int jug = Teclado.readInt("¿Cuántos jugadores hay? ");

    Jugador[] jugadores = new Jugador[jug];
    int rondas = Teclado.readInt("¿Cuántas rondas se jugarán? ");

    for (int i = 0; i < jugadores.length; i++) {
      String aux = Teclado.readString("Introduce el nombre del jugador " + (i + 1) + ": ");
      Jugador j = new Jugador(aux);

      while (j.getHistorialArchivo().exists()) {

        System.out.print("Este jugador ya ha jugado antes, quieres cambiarte el nombre? (Si/No) ");
        if (Teclado.readString().toLowerCase().equals("si")) {
          aux = Teclado.readString("Introduce un nuevo nombre del jugador " + (i + 1) + ": ");
          j = new Jugador(aux);
        } else {
          break;
        }

      }

      jugadores[i] = j;
    }

    Partida p = new Partida(rondas, jugadores);
    p.iniciarPartida();

    if (Partida.getPartidasCreadas() == 1) {
      System.out.println("Has jugado " + Partida.getPartidasCreadas() + " partida.");
    } else {
      System.out.println("Has jugado " + Partida.getPartidasCreadas() + " partidas.");
    }

    try {
      p.guardarArchivo();
    } catch (IOException e) {
      System.err.println("No se ha podido guardar el archivo :(");
    }

  }

}