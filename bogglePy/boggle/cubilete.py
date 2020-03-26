# -*- coding: utf-8 -*-

import random

class Cubilete:

    d1 = [ 'Q', 'B', 'Z', 'J', 'X', 'L' ]
    d2 = [ 'T', 'O', 'U', 'O', 'T', 'O' ]
    d3 = [ 'O', 'V', 'C', 'R', 'G', 'R' ]
    d4 = [ 'A', 'A', 'A', 'F', 'S', 'R' ]
    d5 = [ 'A', 'U', 'M', 'E', 'E', 'O' ]
    
    d6 = [ 'E', 'H', 'L', 'R', 'D', 'O' ]
    d7 = [ 'N', 'H', 'D', 'T', 'H', 'O' ]
    d8 = [ 'L', 'H', 'N', 'R', 'O', 'D' ]
    d9 = [ 'A', 'D', 'A', 'I', 'S', 'R' ]
    d10 = [ 'U', 'I', 'F', 'A', 'S', 'R' ]

    d11 = [ 'T', 'E', 'L', 'P', 'C', 'I' ]
    d12 = [ 'S', 'S', 'N', 'S', 'E', 'U' ]
    d13 = [ 'R', 'I', 'Y', 'P', 'R', 'H' ]
    d14 = [ 'D', 'O', 'R', 'D', 'L', 'N' ]
    d15 = [ 'C', 'C', 'Ñ', 'N', 'S', 'T' ]

    d16 = [ 'T', 'T', 'O', 'T', 'E', 'M' ]
    d17 = [ 'S', 'C', 'T', 'I', 'E', 'P' ]
    d18 = [ 'E', 'A', 'N', 'D', 'N', 'N' ]
    d19 = [ 'M', 'N', 'N', 'E', 'A', 'G' ]
    d20 = [ 'U', 'O', 'T', 'O', 'Ñ', 'N' ]

    d21 = [ 'A', 'E', 'A', 'E', 'E', 'H' ]
    d22 = [ 'Y', 'I', 'F', 'P', 'S', 'R' ]
    d23 = [ 'E', 'E', 'E', 'E', 'M', 'A' ]
    d24 = [ 'I', 'T', 'A', 'T', 'I', 'E' ]
    d25 = [ 'E', 'T', 'I', 'L', 'A', 'C' ]

    dados = [d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17,d18,d19,d20,d21,d22,d23,d24,d25]

    caras = [[None] * 5 for i in range(5)]
    
    def tirarDados(self):
        dado = 0
        for fila in range(5):
            for columna in range(5):
                self.caras[fila][columna] = self.dados[dado][random.randint(1,5)]
                dado += 1
        return self.caras
    
    # Método sobrecargado para poder imprimir el cubilete
    def __str__(self):
        cadenaFinal = "\n"
        for fila in range(5):
            for columna in range(5):
                cadenaFinal += f"{self.caras[fila][columna]} "
            cadenaFinal += "\n"
        return cadenaFinal