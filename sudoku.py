import numpy as np

class Cuadricula:
    def __init__(self):
        self.matrix = [[0, 0, 0], [0, 0, 0], [0,0,0]]
    def asignar_valor(self,coordenada, numero):
        self.matrix[coordenada[0]][coordenada[1]] = numero
    def dame_fila(self,fila):
        return self.matrix[fila]
    def mostrar(self):
        print(self.matrix)

def mostrar_columnas(columnas,fila):
    imprimir = "|"
    for valor in columnas:
        if valor == 0:
            imprimir += "   "
        else:
            imprimir += " " + str(valor) + " "
        imprimir += " | "
    print(imprimir + "F{}".format(fila+1))
class Sudoku:
    def __init__(self, lista_valores):
        #lista_valores es un conj de (coordenadas, valor), coordenada siendo (columna,fila,cuadricula)
        cuadriculas = [x for x in range(1,10)]
        self.cuadriculas = {}
        for cuadricula in cuadriculas:
            self.cuadriculas[cuadricula] = Cuadricula()
        for elem in lista_valores:
            coordenada = elem[0]
            fila = coordenada[0]
            columna = coordenada[1]
            cuadricula = coordenada[2]
            valor = elem[1]
            self.cuadriculas[cuadricula].asignar_valor((fila,columna),valor)
    def mostrar(self):
        cuadricula = 1
        filas = [x for x in range(9)]
        separacion = ""
        for x in range(54):
            separacion += "-"
        legend_columna = "| "
        for x in range(9):
            legend_columna += " C{}".format(x+1)
            legend_columna += " | "
        print(legend_columna)
        for elem in filas:
            fila = elem % 3
            cuadricula_1 = self.cuadriculas[cuadricula]
            cuadricula_2 = self.cuadriculas[cuadricula + 1]
            cuadricula_3 = self.cuadriculas[cuadricula + 2]
            columnas = cuadricula_1.dame_fila(fila) + cuadricula_2.dame_fila(fila) + cuadricula_3.dame_fila(fila)
            print(separacion)
            mostrar_columnas(columnas,elem)
            if (elem+1) % 3 == 0:   
                cuadricula += 3
        print(separacion)
        


           

if __name__ == "__main__":
    Tablero = [((0,1,1),8),((0,0,2),3),((1,1,1),2),((1,2,1),7),((1,0,2),4),((1,2,2),8),((2,0,1),5),((2,2,1),3),((2,0,2),6)
    ,((2,1,2),2),((2,2,3),7),((0,0,4),2),((0,1,4),7),((0,2,4),9),((0,1,6),1),((0,2,6),3),((1,2,4),4),((1,0,5),2),((1,1,6),5),
    ((1,2,6),8),((2,0,4),8),((2,1,4),5),((2,0,6),2),((2,2,6),6),((0,1,7),3),((0,1,8),7),((0,2,8),5),((0,1,9),6),((1,0,7),6),
    ((1,2,7),2),((1,1,8),3),((1,1,9),7),((1,2,9),5),((2,1,7),9),((2,0,8),8),((2,1,9),4)]
    sudoku = Sudoku(Tablero)
    sudoku.mostrar()
    
   