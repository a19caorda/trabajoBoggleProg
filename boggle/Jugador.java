package boggle;

import java.util.ArrayList;
import java.util.Set;
import java.util.HashSet;
import java.util.Scanner;
import java.util.concurrent.atomic.AtomicBoolean;
import java.awt.Robot;
import java.awt.event.KeyEvent;
import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.awt.AWTException;

/**
 * La clase Jugador se encarga de mantener el estado de cada jugador y de
 * iniciar el turno
 * 
 * @author David Castilla Ortiz
 * @version 1.0.0
 * 
 */
public class Jugador {

  private String nombre;
  private int puntuacion = 0;
  private final int TURNO = 180;

  /**
   * Constructor para crear un jugador
   * 
   * @param nombre Nombre que se le dará al Jugador.
   */
  public Jugador(String nombre) {
    this.nombre = nombre;
  }

  /**
   * @return the nombre
   */
  public String getNombre() {
    return nombre;
  }

  /**
   * @param puntuacion the puntuacion to set
   */
  public void setPuntuacion(int puntuacion) {
    this.puntuacion = puntuacion;
  }

  /**
   * @return the puntuacion
   */
  public int getPuntuacion() {
    return puntuacion;
  }

  /**
   * inicioTurno se encarga de iniciar el turno y seguir pidiendo palabras,
   * despues filtrandolas y, ya por ultimo, sumando los puntos que tiene de las
   * palabras intrucidas.
   */
  public Set<String> inicioTurno() {

    final ArrayList<String> palabras = new ArrayList<>();
    final AtomicBoolean isGettingWords = new AtomicBoolean(true);

    Thread wordsThread = new Thread(new Runnable() {

      @Override
      public void run() {
        while (isGettingWords.get()) {
          System.out.printf("Palabra #%d: ", palabras.size() + 1);
          String nuevaPalabra = Teclado.getTeclado().readString();
          palabras.add(nuevaPalabra);
        }
      }
    });

    try {
      wordsThread.start();
      Thread.sleep(1000 * TURNO);
      Robot r = new Robot();
      r.keyPress(KeyEvent.VK_ENTER);
      r.keyRelease(KeyEvent.VK_ENTER);
      isGettingWords.set(false);

      wordsThread.interrupt();
    } catch (InterruptedException e) {
      return new HashSet<String>();
    } catch (AWTException a) {
      return new HashSet<String>();
    }

    return new HashSet<String>(palabras);
    
  }

  @Override
  public String toString() {

    return this.nombre;
  }

}