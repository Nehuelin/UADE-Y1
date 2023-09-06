import random 
import time

#2f, 5

ejercicio = int(input("Que ejercicio queres probar? (NOW TESTING: 1): "))

# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 1

if ejercicio == 1:
    print("Desarrollar cada una de las funciones y escribir un programa que permita verificar su funcionamiento, imprimiendo la matriz luego de invocar a cada funcion: ")
    print("a- Cargar numeros enteros en una matriz de NxN, ingresando los datos desde el teclado.")
    print("b- Ordenar de forma ascendente cada una de las filas de la matriz.")
    print("c- Intercambiar dos filas, cuyos numeros se reciben como parametro.")
    print("d- Intercambiar dos columnas dadas, cuyos numeros se reciben como parametro.")
    print("e- Transponer la matriz sobre si misma.")
    print("f- Calcular el promedio de los elementos de una fila, cuyo numero se recibe como parametro.")
    print("g- Calcular el porcentaje de elementos con valor impar de una columna, cuyo numero se recibe como parametro.")
    print("h- Determinar si la matriz es simetrica respecto a su diagonal principal.") 
    print("i- Determinar si la matriz es simetrica respecto a su diagonal secundaria.") 
    print("j- Determinar que columnas de la matriz son palindromos (capicuas), devolviendo una lista con los numeros de la mismas.")
    print()
    time.sleep(0)

    def cargar_matriz(matrix):
        for f in range(len(matrix)):
            for c in range(len(matrix[f])):
                matrix[f][c] = int(input("Ingresar numero entero: "))
                
    def filas_ascendentes(matrix):
        for f in range(len(matrix)):
            matrix[f].sort()
    
    def intercambiar_filas(matrix, x, y):
        aux = matrix[x]
        matrix[x] = matrix[y]
        matrix[y] = aux
    
    def intercambiar_columnas(matrix, x, y):
        for fila in matrix:
            fila[x], fila[y] = fila[y], fila[x]            
    
    # MAIN
    n = int(input("Ingresar numero N: "))
    
    filas = n
    columnas = n
    matriz = [[0]* columnas for i in range(filas)]
    
    cargar_matriz(matriz)
    for filas in matriz:
        for elemento in filas:
            print("%3d"%elemento, end=" ")
        print()

    print()
    filas_ascendentes(matriz)
    for filas in matriz:
        for elemento in filas:
            print("%3d"%elemento, end=" ")
        print()
     
    print()
    a = int(input("Ingresar numero de la primera fila (Recordar que la primera fila es 0): "))
    b = int(input("Ingresar numero de la segunda fila: "))
    intercambiar_filas(matriz, a, b)
    for filas in matriz:
        for elemento in filas:
            print("%3d"%elemento, end=" ")
        print()    
    
    print()
    a = int(input("Ingresar numero de la primera columna (Recordar que la primera columna es 0): "))
    b = int(input("Ingresar numero de la segunda columna: "))
    intercambiar_columnas(matriz, a, b)
    for filas in matriz:
        for elemento in filas:
            print("%3d"%elemento, end=" ")
        print()      
    
# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 2

if ejercicio == 2:
    print("Para cada una de las matrices del punto, desarrollar una funcion que la genere y escribir un programa que invoque a cada una de ellas y muestre por pantalla la matriz obtenida. \nEl tamaño de las matrices debe establecerse como NxN, y las funciones deben servir aunque este valor se modifique.")
    print()
    time.sleep(0)

    def matrizalpha(n):
        pass
    
    def matrizbravo(n):
        pass
    
    def matrizcharlie(n):
        pass
    
    def matrizdelta(n):
        pass
    
    def matrizecho(n):
        pass
    
    def matrizfoxtrot(n):
        # 0 0 0 1
        # 0 0 3 2
        # 0 6 5 4
        # 10 9 8 7
           
        d = 1
        for f in range(filas):
            for c in range(columnas):
                if f >= c:
                    matriz[f][c] = d
                    d += 1    
        for f in range(filas):
            matriz[f].reverse()
        

    
    def matrizgolf(n):
        pass
    
    def matrizhotel(n):
        pass
    
    def matrizindia(n):
        pass
    
    
    
    factor = int(input("Ingresar numero N: "))
    
    filas = factor
    columnas = factor
    matriz = [[0]*columnas for i in range(filas)]
    
    matrizalpha(factor)
    matrizbravo(factor)
    matrizcharlie(factor)
    matrizdelta(factor)
    matrizecho(factor)
    matrizfoxtrot(factor)
    matrizgolf(factor)
    matrizhotel(factor)
    matrizindia(factor)
    
    for filas in matriz:
        for elemento in filas:
            print("%3d" %elemento, end=" ")
        print()

    
    
    
# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 5

if ejercicio == 5:
    print("Desarrolle un programa que permita realizar reservas en una sala de cine de barrio de N filas con M butacas por cada fila.\nDesarrollar las siguientes funciones y utilizarlas en un mismo programa: ")
    print("\033[1m--> mostrar_butacas\033[0m: Mostrara por pantalla el estado de cada una de las butacas del cine por pantalla. Se debera mostrar antes de que el usuario realice la reserva y se volvera a mostrar luego de la misma, con los estados actualizados.")
    print("\033[1m--> reservar\033[0m: Debera recibir una matriz y la butaca seleccionada, y actualizara la matriz en caso de estar disponible dicha butaca. La funcion devolvera \033[1mTrue/False\033[0m si logro o no reservar la butaca.")
    print("\033[1m--> cargar_sala\033[0m: Recibira una matriz como parametro y la cargara con valores aleatorios para simular una sala con butacas ya reservadas.")
    print("\033[1m--> butacas_libres\033[0m: Recibira como parametro la matriz y retornara cuantas butacas desocupadas hay en la sala.")
    print("\033[1m--> butacas_contiguas\033[0m: Buscara la secuencia mas larga de butacas libres contiguas en una misma fila y devolvera las coordenadas del inicio de la misma.")
    print()
    time.sleep(0)
    
    def mostrar_butacas(matrix): #Basicamente esta funcion imprime la matriz 
        for fila in matrix:
            for elemento in fila:
                print(elemento, end=" ")
            print()
    
    def reservar(matrix, target):
        reserva_exitosa = False
        for f in range(len(matrix)):
            for c in range(len(matrix[0])):
                if target == matrix[f][c]:
                    matrix[f][c] = 'X'
                    reserva_exitosa = True
                    break
        if reserva_exitosa:
            return True
        else:
            return False
    
    def cargar_sala(matrix):
        reserva = 0
        for f in range(len(matrix)):
            for c in range(len(matrix[0])):
                reserva = random.randint(0, 1)
                if reserva == 1:
                    matrix[f][c] = 'X'               
    
    def butacas_libres(matrix):
        contador = 0
        for f in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[f][c] != 'X':
                    contador += 1
        return contador
    
    def butacas_contiguas(matrix):
        max_contiguas = 0
        inicio_max_x = 0
        inicio_max_y = 0
        
        for fila in range(len(matrix)):
            contiguas = 0
            inicio_actual_x = fila
            inicio_actual_y = 0
            
            for columna in range(len(matrix[fila])):
                if matrix[fila][columna] != 'X':
                    contiguas += 1
                else:
                    if contiguas > max_contiguas:
                        max_contiguas = contiguas
                        inicio_max_x = inicio_actual_x
                        inicio_max_y = inicio_actual_y
                    contiguas = 0
                    inicio_actual_y = columna + 1
            
            if contiguas > max_contiguas:
                max_contiguas = contiguas
                inicio_max_x = inicio_actual_x
                inicio_max_y = inicio_actual_y
        
        if max_contiguas > 0:
            return inicio_max_x, inicio_max_y
        else:
            return -1, -1
    
    #MAIN
    n = int(input("Ingresar cantidad de filas: "))
    m = int(input("Ingresar cantidad de butacas por fila: "))
    
    filas = n
    columnas = m
    matriz = [[0]* columnas for i in range(filas)]
    numfila = 1
    for f in range(filas):
        for c in range(columnas):
            matriz[f][c] = numfila  
            numfila += 1
    
    print("Cargando sala: ")
    cargar_sala(matriz)
    mostrar_butacas(matriz)
    cantidad = butacas_libres(matriz)
    print("Hay",cantidad,"butacas libres")
    x, y = butacas_contiguas(matriz)
    print("Coordenadas de butacas contiguas libres mas larga: [",x,",",y,"]" )
    
    butaca = int(input("Ingresar el numero de la butaca a reservar: "))
    pudo_reservar = reservar(matriz, butaca)
    
    if pudo_reservar:
        print("Reserva exitosa!")
        mostrar_butacas(matriz)
    else:
        print("No se pudo hacer la reserva")
    
    print()
    
