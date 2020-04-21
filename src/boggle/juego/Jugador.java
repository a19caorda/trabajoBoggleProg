package boggle.juego;

import java.awt.AWTException;
import java.awt.Robot;
import java.awt.event.KeyEvent;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.NoSuchElementException;
import java.util.Set;
import java.util.concurrent.atomic.AtomicBoolean;

import boggle.utiles.Teclado;

/**
 * La clase Jugador se encarga de mantener el estado de cada jugador y de
 * iniciar el turno
 * 
 * @author David Castilla Ortiz
 * @version 1.1.0
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
   * @return el nombre del jugador
   */
  public String getNombre() {
    return nombre;
  }

  /**
   * @param puntuacion la puntuacion a poner
   */
  public void setPuntuacion(int puntuacion) {
    this.puntuacion = puntuacion;
  }

  /**
   * @param puntuacion la puntuacion a sumar
   */
  public void sumaPuntuacion(int puntuacion) {
    this.puntuacion += puntuacion;
  }

  /**
   * @return la puntuacion del jugador
   */
  public int getPuntuacion() {
    return puntuacion;
  }

  /**
   * inicioTurno se encarga de iniciar el turno y seguir pidiendo palabras,
   * y por último devolver una colección de palabras únicas.
   */
  public Set<String> inicioTurno() {

    final ArrayList<String> palabras = new ArrayList<>();
    final AtomicBoolean isGettingWords = new AtomicBoolean(true);

    Thread wordsThread = new Thread(new Runnable() {

      @Override
      public void run() {
        Teclado teclado = new Teclado();
        while (isGettingWords.get()) {
          System.out.printf("Palabra %d: ", palabras.size() + 1);
          try {
            String nuevaPalabra = teclado.readString();
            palabras.add(nuevaPalabra);

          } catch (NoSuchElementException e) {
          } catch (IndexOutOfBoundsException e) {
          }
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

      // wordsThread.interrupt();

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