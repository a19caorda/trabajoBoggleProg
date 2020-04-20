package boggle.juego;

/**
 * Esta clase crea un cubilete de dados con las caras que salgan aleatoriamente
 * Tiene los siguientes métodos:
 *  tirarDados()
 *  toString()
 * @author Antonio García García
 * @version 1.0
 */
public class Cubilete {

  /**
   * Dados
   */
  private final char d1[] = new char[] { 'Q', 'B', 'Z', 'J', 'X', 'L' };
  private final char d2[] = new char[] { 'T', 'O', 'U', 'O', 'T', 'O' };
  private final char d3[] = new char[] { 'O', 'V', 'C', 'R', 'G', 'R' };
  private final char d4[] = new char[] { 'A', 'A', 'A', 'F', 'S', 'R' };
  private final char d5[] = new char[] { 'A', 'U', 'M', 'E', 'E', 'O' };

  private final char d6[] = new char[] { 'E', 'H', 'L', 'R', 'D', 'O' };
  private final char d7[] = new char[] { 'N', 'H', 'D', 'T', 'H', 'O' };
  private final char d8[] = new char[] { 'L', 'H', 'N', 'R', 'O', 'D' };
  private final char d9[] = new char[] { 'A', 'D', 'A', 'I', 'S', 'R' };
  private final char d10[] = new char[] { 'U', 'I', 'F', 'A', 'S', 'R' };

  private final char d11[] = new char[] { 'T', 'E', 'L', 'P', 'C', 'I' };
  private final char d12[] = new char[] { 'S', 'S', 'N', 'S', 'E', 'U' };
  private final char d13[] = new char[] { 'R', 'I', 'Y', 'P', 'R', 'H' };
  private final char d14[] = new char[] { 'D', 'O', 'R', 'D', 'L', 'N' };
  private final char d15[] = new char[] { 'C', 'C', 'Ñ', 'N', 'S', 'T' };

  private final char d16[] = new char[] { 'T', 'T', 'O', 'T', 'E', 'M' };
  private final char d17[] = new char[] { 'S', 'C', 'T', 'I', 'E', 'P' };
  private final char d18[] = new char[] { 'E', 'A', 'N', 'D', 'N', 'N' };
  private final char d19[] = new char[] { 'M', 'N', 'N', 'E', 'A', 'G' };
  private final char d20[] = new char[] { 'U', 'O', 'T', 'O', 'Ñ', 'N' };

  private final char d21[] = new char[] { 'A', 'E', 'A', 'E', 'E', 'H' };
  private final char d22[] = new char[] { 'Y', 'I', 'F', 'P', 'S', 'R' };
  private final char d23[] = new char[] { 'E', 'E', 'E', 'E', 'M', 'A' };
  private final char d24[] = new char[] { 'I', 'T', 'A', 'T', 'I', 'E' };
  private final char d25[] = new char[] { 'E', 'T', 'I', 'L', 'A', 'C' };

  /**
   * Matriz con todos los dados
   */
  private final char dados[][] = new char[][] {d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17,d18,d19,d20,d21,d22,d23,d24,d25};  

  /**
   * Matriz donde se almacenarán las caras de los dados
   */
  char caras[][] = new char[5][5];

  /**
   * Crea un array bidimensional con las letras que salgan de haber "tirado" el dado
   * @return Un array bidimensional con las caras de los dados resultantes de "tirar" los dados
   */
  public char[][] tirarDados() {
    int dado = 0;
    for (int fila=0;fila<5;fila++) {
      for (int columna=0;columna<5;columna++) {
        caras[fila][columna] = (char) (dados[dado][(int) (Math.random()*5+1)]);
        dado++;
      }
    }
    return caras;
  }

  /**
   * Imprime por pantalla el objeto de la manera indicada en el método
   * @return Una cadena para ver graficamente el cubilete
   */
  public String toString() {
    String cadenaFinal = "\n";
    for (int fila=0;fila<5;fila++) {
      for (int columna=0;columna<5;columna++) {
        cadenaFinal += caras[fila][columna]+" ";
      }
      cadenaFinal += "\n";
    }
    return cadenaFinal;
  }

}