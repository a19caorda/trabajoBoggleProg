import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.ArrayList;
import java.util.Set;
import javax.swing.JOptionPane;
import boggle.utiles.Teclado;

"""
 * Clase Partida.
 * 
 * Atributos: -maxRondas <-- Almacena el número máximo de rondas que puede tener
 * una partida. -partidasCreadas <-- Almacena un número entero que representa
 * las veces que se han inicializado partidas. -jugadores[] <-- Array de objetos
 * de tipo Jugador. -numRondas <-- Número entero.
 * 
 * Métodos: -iniciarPartida <-- Se encarga de inicializar la partida y gestionar
 * los turnos de los jugadores. -decideGanador <-- Lee la puntuación de los
 * jugadores de la partida y devuelve el que tenga la puntuación más alta.
 * 
 * @author David Fontalba
 * @version 1.1.
"""
class Partida:
    # Atributos de la clase, el número de partidas creadas.
    __MAXRONDAS = 5;
    __partidasCreadas = 0;

    # Atributos de la partida.
    __jugadores
    __numRondas

    def __init__(self, numJugadores, numRondas):
        __partidasCreadas+=1
        cubilete = Cubilete()
        # se almacena numRondas.
        assert __MAXRONDAS >= numRondas > 0
        compruebaRondas(numRondas)

        # se almacenan jugadores
        assert numJugadores > 0 # El número de jugadores tiene que ser positivo.
        pideJugadores(numJugadores)


    def __init__(self, numRondas, jugadores):
        __partidasCreadas += 1
        if  numRondas >= __MAXRONDAS:
            this.__numRondas = __MAXRONDAS
        else:
            this.__numRondas = numRondas

        this.__jugadores = jugadores

    def pideJugadores(numJugadores):
        if numJugadores > 0:
            aux # Auxiliar para almacenar los nombres de los jugadores.

            this.jugadores = Jugador[numJugadores] #Defino el tamaño del array.

            # Pido nombres de tantos jugadores como número de jugadores halla.
            for i in numJugadores:
                aux = Teclado.readString("Introduce el nombre del jugador " + (i + 1) + ": ")

                this.jugadores[i] = Jugador(aux)

        else: # numJugadores es menor que 0, muestra un mensaje de error.
            print("ERROR: El número de jugadores tiene que ser mayor que 0.");
            System.exit(1)

  def compruebaRondas(int numRondas) {
    if (MAXRONDAS >= numRondas && numRondas > 0) { // El número de rondas tiene que ser positivo y menor al máximo.
      this.numRondas = numRondas;

    } else if (numRondas > MAXRONDAS) { // Si el número de rondas es mayor al máximo, aplica el máximo.
      this.numRondas = MAXRONDAS;

    } else { // numRondas es menor que 0, muestra un mensaje de error.
      JOptionPane.showMessageDialog(null, "ERROR: El número de rondas tiene que ser mayor que 0.");
      System.exit(1);
    }
  }

  public void iniciarPartida() {

    // Bucle para las rondas
    for (int i = 0; i < this.numRondas; i++) {
      System.out.println("Prepárate, la ronda " + (i + 1) + " va a comenzar.");

      // Bucle para los turnos
      for (int j = 0; j < this.jugadores.length; j++) {
        System.out.println("Es el turno de " + this.jugadores[j] + ".");
        // Añadida tirada de dado y muestra del resultado
        this.cubilete.tirarDados();
        System.out.println(this.cubilete.toString());
        // Quitamos las repeticiones
        Set<String> palabras = jugadores[j].inicioTurno();
        System.out.println("\nFin del turno " + (j + 1) + ".");

        ArrayList<String> palabrasProcesadas = comprueba(palabras);

        System.out.println("Palabras válidas");
        for (String palabraProcesada : palabrasProcesadas) {
          System.out.println(" - " + palabraProcesada);
        }

        jugadores[j].sumaPuntuacion(sumaPuntos(palabrasProcesadas));

        try {
          Thread.sleep(1000);
        } catch (InterruptedException e) {
        }

      }
      System.out.println("Fin de la ronda " + (i + 1) + ".");

    }

    decideGanador();

  }

  private void decideGanador() {
    ArrayList<Integer> ganador = new ArrayList<Integer>(); // Almacena la posición del jugador que tiene más
    // puntuación
    int aux = 0; // Almacena la puntuación máxima

    // Bucle para leer la puntuación de los jugadores
    for (int i = 0; i < this.jugadores.length; i++) {

      // Si el jugador a leer tiene más puntuación
      if (this.jugadores[i].getPuntuacion() > aux) {
        ganador.clear();
        ganador.add(i);
        aux = this.jugadores[i].getPuntuacion();

        // Si el jugador a leer tiene la misma puntuación
      } else if (this.jugadores[i].getPuntuacion() == aux) {
        ganador.add(i);
      }

    }

    // Si hay más de un ganador
    if (ganador.size() > 1) {
      System.out.print("Felicidades a los ganadores, ");

      for (int i = 0; i < ganador.size(); i++) {
        // El último ganador de la lista
        if (i + 1 == ganador.size()) {
          System.out.println("y " + this.jugadores[ganador.get(i)].getNombre() + ".");

          // El resto de ganadores
        } else {
          System.out.print(this.jugadores[ganador.get(i)].getNombre() + ", ");
        }

      }
      // Si solo hay un ganador
    } else {
      System.out.println("Felicidades " + this.jugadores[ganador.get(0)].getNombre() + ", ¡Has ganado!");

    }

    System.out.println("Recuento de puntuaciones: ");
    for (Jugador jugador : this.jugadores) {
      System.out.println(jugador.getNombre() + ": " + jugador.getPuntuacion());
    }
  }

  /**
   * comprueba se encarga de comprobar que las palabras sean correctas y filtra
   * las incorrectas.
   *
   * @param aFiltrar La lista de palabras no filtradas
   * @return La lista de palabras filtrada
   */
  private ArrayList<String> comprueba(Set<String> aFiltrar) {

    ArrayList<String> palabrasFiltradas = new ArrayList<>();

    for (String palabraNoFiltrada : aFiltrar) {

      if (palabraNoFiltrada.length() < 3 && palabraNoFiltrada.length() > 23) {
        continue;
      }

      palabraNoFiltrada = comprobarExistenciaPalabra(palabraNoFiltrada);

      if (palabraNoFiltrada.isEmpty()) {
        continue;
      }
      palabraNoFiltrada = comprobarMatrizBienFormada(palabraNoFiltrada);

      if (palabraNoFiltrada.isEmpty()) {
        continue;
      }

      palabrasFiltradas.add(palabraNoFiltrada);

    }

    return palabrasFiltradas;
  }

  /**
   *
   * sumaPuntos se encarga de sumar los puntos de las palabras
   *
   * @param palabras La lista de palabras que ya ha sido filtrada
   * @return La suma de lo que puntúa cada palabra
   */
  private int sumaPuntos(ArrayList<String> palabras) {

    int resultadoFinal = 0;

    for (String palabra : palabras) {
      switch (palabra.length()) {
        case 0:
        case 1:
        case 2:
        case 3:
          break;
        case 4:
          resultadoFinal += 1;
          break;
        case 5:
          resultadoFinal += 2;
          break;
        case 6:
          resultadoFinal += 3;
          break;
        case 7:
          resultadoFinal += 5;
          break;
        default:
          resultadoFinal += 11;
          break;
      }
    }

    return resultadoFinal;
  }

  private String comprobarExistenciaPalabra(String palabraAFiltrar) {

    try {

      URL url = new URL(
          String.format("https://od-api.oxforddictionaries.com:443/api/v2/entries/es/%s?lexicalCategory=noun,verb",
              palabraAFiltrar.toLowerCase()));
      HttpURLConnection conn = (HttpURLConnection) url.openConnection();
      conn.setRequestMethod("GET");
      conn.setRequestProperty("app_id", "46a14e95");
      conn.setRequestProperty("app_key", "384d633d7a131cd0ab86fb6322665e15");
      conn.connect();

      if (conn.getResponseCode() != 200) {
        return "";
      }

    } catch (MalformedURLException e) {
      return "";
    } catch (IOException e) {
      return "";
    }

    return palabraAFiltrar;

  }

  private String comprobarMatrizBienFormada(String palabra) {
    char[][] c = cubilete.caras;
    palabra = palabra.toUpperCase();
    String validador = "";

    for (int x = 0; x < 5; x++) {
      for (int y = 0; y < 5; y++) {
        int newX = x;
        int newY = y;
        for (int letraPos = 0; letraPos < palabra.length(); letraPos++) {
          if (c[newX][newY] == (palabra.charAt(letraPos))) {

            validador += c[newX][newY];
            if (validador.equals(palabra)) {
              return palabra;
            }
            try {
              if (c[newX + 1][newY] == (palabra.charAt(letraPos + 1))) {
                newX = newX + 1;
                continue;
              }
            } catch (IndexOutOfBoundsException e) {
            }
            try {
              if (c[newX - 1][newY] == (palabra.charAt(letraPos + 1))) {
                newX = newX - 1;
              }
            } catch (IndexOutOfBoundsException e) {
            }
            try {
              if (c[newX][newY + 1] == (palabra.charAt(letraPos + 1))) {
                newY = newY + 1;
                continue;
              }
            } catch (IndexOutOfBoundsException e) {
            }
            try {
              if (c[newX][newY - 1] == (palabra.charAt(letraPos + 1))) {
                newY = newY - 1;
                continue;
              }
            } catch (IndexOutOfBoundsException e) {
            }
            try {
              if (c[newX + 1][newY + 1] == (palabra.charAt(letraPos + 1))) {
                newY = newY + 1;
                newX = newX + 1;
                continue;
              }
            } catch (IndexOutOfBoundsException e) {
            }
            try {
              if (c[newX + 1][newY - 1] == (palabra.charAt(letraPos + 1))) {
                newY = newY - 1;
                newX = newX + 1;
                continue;
              }
            } catch (IndexOutOfBoundsException e) {
            }
            try {
              if (c[newX - 1][newY + 1] == (palabra.charAt(letraPos + 1))) {
                newY = newY + 1;
                newX = newX - 1;
                continue;
              }
            } catch (IndexOutOfBoundsException e) {
            }
            try {
              if (c[newX - 1][newY - 1] == (palabra.charAt(letraPos + 1))) {
                newY = newY - 1;
                newX = newX - 1;
                continue;
              }
            } catch (IndexOutOfBoundsException e) {
            }
          } else {
            validador = "";
            break;
          }
          letraPos++;

        }

      }
    }

    return "";

  }

  // Getters
  public static int getPartidasCreadas() {
    return partidasCreadas;
  }
