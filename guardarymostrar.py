matriz = [['-','-','-'],['-','-','-'],['-','-','-']]
import os
def fnt_agregar (dato, x, y):
    if matriz[x][y] == '-':
        matriz[x][y] = dato.upper()
    elif matriz[x][y] == 'x':
        input('\n espacio esta ocupado ')

def fnt_impresion_matriz ():
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print (matriz[i][j], end = '   ')
        print()
sw = True

while sw== True:
    os.system('cls')
    fnt_impresion_matriz()
    fnt_agregar(input( 'dato: '), int(input('fila: ')), int(input('columna: ')))
    
    