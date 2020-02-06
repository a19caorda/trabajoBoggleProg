package boggle;

import java.util.ArrayList;
import java.util.Scanner;
import java.util.concurrent.atomic.AtomicBoolean;
import java.awt.Robot;
import java.awt.event.KeyEvent;
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

    public String nombre;
    public int puntuacion = 0;
    public Dado dado;
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
     * inicioTurno se encarga de iniciar el turno y seguir pidiendo palabras,
     * despues filtrandolas y, ya por ultimo, sumando los puntos que tiene de las
     * palabras intrucidas.
     */
    public void inicioTurno() {

        System.out.printf("----------------Empieza el turno de %s!----------------\n", this.nombre);
        System.out.printf("Preparate bien!\n");

        dado.tirarDados();
        System.out.println("Tus dados son...");
        System.out.println(dado);

        final ArrayList<String> palabras = new ArrayList<>();
        final AtomicBoolean isGettingWords = new AtomicBoolean(true);

        Thread wordsThread = new Thread(new Runnable() {

            @Override
            public void run() {
                Scanner scan = new Scanner(System.in);
                while (isGettingWords.get()) {
                    System.out.printf("Palabra #%d: ", palabras.size() + 1);
                    String nuevaPalabra = scan.nextLine();
                    palabras.add(nuevaPalabra);
                }
                scan.close();
            }
        });

        try {
            wordsThread.start();
            Thread.sleep(3 * 1000);
            Robot r = new Robot();
            r.keyPress(KeyEvent.VK_ENTER);
            r.keyRelease(KeyEvent.VK_ENTER);
            isGettingWords.set(false);

            wordsThread.interrupt();
        } catch (InterruptedException e) {
            return;
        } catch (AWTException a) {
            return;
        }

        ArrayList<String> palabrasFiltradas = comprueba(palabras);
        this.puntuacion += sumaPuntos(palabrasFiltradas);

    }

    /**
     * 
     * sumaPuntos se encarga de sumar los puntos de las palabras
     * 
     * @param palabras La lista de palabras que ya ha sido filtrada
     * @return La suma de lo que puntua cada palabra
     */
    private int sumaPuntos(ArrayList<String> palabras) {

        int resultadoFinal = 0;

        for (String palabra : palabras) {
            switch (palabra.length()) {
            case 3:
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

    /**
     * comprueba se encarga de comprobar que las palabras sean correctas
     * y filtra las incorrectas.
     * 
     * @param aFiltrar La lista de palabras no filtradas
     * @return La lista de palabras filtrada
     */
    private ArrayList<String> comprueba(ArrayList<String> aFiltrar) {

        ArrayList<String> palabrasFiltradas = new ArrayList<>();

        for (String palabraNoFiltrada : aFiltrar) {

            if (palabraNoFiltrada.isEmpty() && palabraNoFiltrada.length() < 3) {
                continue;
            }

            palabrasFiltradas.add(palabraNoFiltrada);

        }

        return palabrasFiltradas;
    }

}