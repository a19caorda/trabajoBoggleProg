package boggle.utiles;

import java.util.Scanner;

/**
 * Teclado es un singleton que se encarga del input del programa Para usarlo se
 * debe usar el método estático `getTeclado()`
 */
public class Teclado {

  private Scanner SCAN = new Scanner(System.in);

  public Teclado() {
  }

  /**
   * Método estático para obtener la instancia
   * 
   * @return Instancia de clase Teclado
   
  public static Teclado getTeclado() {
    return teclado;
  }
  */

  /**
   * Método para obtener una cadena que introduzca el usuario
   * 
   * @return La cadena puesta por el usuario
   */
  public String readString() {
    return SCAN.nextLine();
  }
  
  public String readString(String mensaje) {
    System.out.print(mensaje);
    return readString();
  }

  /**
   * Método para obtener un número que introduzca el usuario
   * 
   * @return El número puesta por el usuario
   */
  public int readInt() {
    return SCAN.nextInt();
  }
  
  public int readInt(String mensaje) {
    System.out.print(mensaje);
    return readInt();
  }

  /**
   * Método para cerrar el Scanner, debe llamarse cuando finaliza el programa
   */
  public void close() {
    SCAN.close();
  }

}