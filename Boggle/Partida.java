package Boggle;

import java.util.Scanner;

import javax.swing.JOptionPane;

import sun.security.util.Length;

/**
 * Clase Partida. 
 * 
 * Atributos:
 * 	-maxRondas				<-- Almacena el número máximo de rondas que puede tener una partida.
 * 	-partidasCreadas	<-- Almacena un número entero que representa las veces que se han inicializado 
 * 												partidas.
 * 	-jugadores[]			<-- Array de objetos de tipo Jugador.
 * 	-numRondas 				<-- Número entero.
 * 
 * Métodos:
 * 	-iniciarPartida		<-- Se encarga de inicializar la partida y gestionar los turnos de los jugadores.
 * 	-decideGanador		<-- Lee la puntuación de los jugadores de la partida y devuelve el que tenga la 
 * 												puntuación más alta.
 * 
 * @author David Fontalba
 * @version 1.0.
 *
 */
public class Partida {
	// Atributos de la clase, el número de partidas creadas.
	public static int maxRondas = 5;
	private static int partidasCreadas = 0;

	// Atributos de la partida.
	private Jugador jugadores[];
	private int numRondas;
	
	public Partida(int numJugadores, int numRondas) {
		
		// se almacena numRondas.
		assert maxRondas >= numRondas && numRondas > 0;
		if (maxRondas >= numRondas && numRondas > 0) {	// El número de rondas tiene que ser positivo y menor al máximo.
			this.numRondas = numRondas;
			
		} else if (numRondas > maxRondas) {	// Si el número de rondas es mayor al máximo, aplica el máximo.
			this.numRondas = maxRondas;
			
		} else {														// numRondas es menor que 0, muestra un mensaje de error.
			JOptionPane.showMessageDialog(null, "ERROR: El número de rondas tiene que ser mayor que 0.");
		}
		
		// se almacenan jugadores
		assert numJugadores > 0;		// El número de jugadores tiene que ser positivo.
		if (numJugadores > 0) {
			Scanner s = new Scanner(System.in); // Scanner para leer los nombres de los jugadores.
			
			String aux;	// Auxiliar para almacenar los nombres de los jugadores.
			
			Jugador jugadores[] = new Jugador[numJugadores];	// Defino el tamaño del array.
			
			// Pido nombres de tantos jugadores como número de jugadores halla.
			for (int i = 0; i < numJugadores; i++) {
				System.out.print("Introduce el nombre del jugador " + (i+1) + ": ");
				aux = s.nextLine();
				
				this.jugadores[i] = Jugador(aux);
				System.out.println();	// Salto de línea.
			}
			
		} else {	// numJugadores es menor que 0, muestra un mensaje de error.
			JOptionPane.showMessageDialog(null, "ERROR: El número de jugadores tiene que ser mayor que 0.");
		}
	}
	
	public void iniciarPartida() {
		
		for (int i = 0; i < this.numRondas; i++) {
			for (int j = 0; j < this.jugadores[].length; j++) {
				
			}
		}
		
	}
	
	public Jugador decideGanador() {
		
	}
}