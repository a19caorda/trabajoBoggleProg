package boggle.utiles;

/**
 * Menu
 */
public class Menu {

  private String[] opciones;
  private String titulo;

  public Menu(String titulo, String... opciones) {
    this.opciones = opciones;
    this.titulo = titulo;
  }

  private void mostrar() {

    System.out.println("----------------");
    System.out.printf("%s\n", this.titulo);
    System.out.println("----------------");
    for (int i = 0; i < opciones.length; i++) {
      System.out.printf("%d. %s\n", i + 1, this.opciones[i]);
    }

  }

  private int recogerOpcion() {

    for (;;) {
      int i = Teclado.readInt(" ~> ");
      if (i < opciones.length + 1 && i > 0)
        return i;
    }

  }

  public int gestionar() {
    mostrar();
    return recogerOpcion();
  }

}