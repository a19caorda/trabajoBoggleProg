package boggle.utiles;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Teclado {

  private static BufferedReader scanner = new BufferedReader(new InputStreamReader(System.in));

  public static String readString(String prompt) {
    System.out.print(prompt);
    return readString();
  }

  public static String readString() {

    for (;;)
      try {
        return scanner.readLine();
      } catch (IOException e) {
        // TODO Auto-generated catch block
        e.printStackTrace();
      }
  }

  public static float readFloat(String prompt) {
    System.out.print(prompt);
    for (;;) {
      try {
        return Float.parseFloat(readString());
      } catch (NumberFormatException e) {
        System.err.println("Introduce un decimal válido: ");
      }
    }
  }

  public static int readInt(String prompt) {
    System.out.print(prompt);
    for (;;) {
      try {
        return Integer.parseInt(readString());
      } catch (NumberFormatException e) {
        System.err.println("Introduce un número entero válido: ");
      }
    }
  }

}
