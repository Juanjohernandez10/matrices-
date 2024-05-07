'''matriz  = [[0,0,0],[0,0,0],[0,0,0]]
matriz2 = [['','',''],['','',''],['','','']]
matriz[2][2] = 100
print(matriz) # impresion lineal 
print(matriz2)'''

'''NOMBRES = [['a' , 'b' , 'c' , 'd'],['f','i','j','k'],['l','m','n','o']]

for i in range(len(NOMBRES)):
    for j in range(len(NOMBRES[i])):
        print (NOMBRES[i][j],end= ' ')
    print()'''
    
nombres= [['','','',''],['','','',''],['','','',''],['','','','']]
import os 
    
def fnt_impresion_matriz ():
    for i in range(len(nombres)):
        for j in range(len(nombres[i])):
            print (nombres[i][j],end= ' ')
        print()
    
def fnt_limpiar ():
    os.system('cls')
    print(' autor: juan jose hernandez duarte ')
    print('\n')
    fnt_impresion_matriz()
    print('\n\n')

def fnt_agregar ():
    fnt_limpiar()
    for i in range(len(nombres)):
        for j in range(len(nombres[i])):
            nombres[i][j] = input(f'ingrese su nombre {i},{j} -> ')
    input('\n todos los nombres han sido registrados <enter> ')
    fnt_impresion_matriz()
fnt_agregar()


        

