import random 
import time

#2f, 5

ejercicio = int(input("Que ejercicio queres probar? (NOW TESTING: ): "))

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
    time.sleep(10)

    def cargar_matriz(matrix):
        for f in range(len(matrix)):
            for c in range(len(matrix[f])):
                matrix[f][c] = int(input("Ingresar numero entero: "))
                # matriz[f][c] = random.randint(1,50) # <--- TEMPORAL
                
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
    
    def transponer_matriz(matrix):
        for f in range(len(matrix)):
            for c in range(f + 1, len(matrix[0])):
                matrix[f][c], matrix[c][f] = matrix[c][f], matrix[f][c]    
    
    def calcular_promedio(matrix, x):
        if x < 0 or x >= (len(matrix)):
            return -1
        
        fila_seleccionada = matrix[x]
        total = sum(fila_seleccionada)
        promedio = total / len(fila_seleccionada)
        return promedio
    
    def calcular_porcentaje(matrix, y):
        if y < 0 or y >= (len(matrix)):
            return -1
        
        elementos = len(matrix)
        impares = [fila[y] for fila in matrix if fila[y] % 2 != 0]
        porcentaje = ((len(impares)) * 100) / elementos
        return porcentaje
    
    def matriz_simetrica_principal(matrix): # PARA PROBAR CASO SIMETRICO ---> N = 2, poner numeros en el siguiente orden: 1, 3, 3, 5. NO intercambiar filas/columnas
        simetrica = True
        for f in range(len(matrix)):
            for c in range(f + 1, len(matrix[0])):
                if matrix[f][c] != matrix[c][f]:
                    simetrica = False
                    break
        return True if simetrica else False
    
    def matriz_simetrica_secundaria(matrix): # PARA PROBAR CASO SIMETRICO ---> N = 2, NO intercambiar filas/columnas
        simetrica = True
        filas = len(matrix)
        columnas = len(matrix[0])
        
        for f in range(filas):
            for c in range(columnas):
                if matrix[f][c] != matrix[filas - c - 1][columnas - f - 1]:
                    simetrica = False
                    break
        return True if simetrica else False
    
    def es_palindromo(numero):
    # Función para verificar si un número es palíndromo sin convertirlo a cadena
        original = numero
        invertido = 0

        while numero > 0:
            digito = numero % 10
            invertido = invertido * 10 + digito
            numero = numero // 10

        return original == invertido
    
    def columnas_capicuas(matrix):
        colcap = []
        filas = len(matrix)
        columnas = len(matrix[0])

        for c in range(columnas):
            columna = [matrix[f][c] for f in range(filas)]
            palindromo = True

            for elemento in columna:
                if not es_palindromo(elemento):
                    palindromo = False
                    break

            if palindromo:
                colcap.append(c)

        return colcap
         
    
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
    
    print()
    transponer_matriz(matriz)
    print("Matriz Transpuesta: ")
    for filas in matriz:
        for elemento in filas:
            print("%3d"%elemento, end=" ")
        print() 
    
    print()
    a = int(input("Ingresar numero de fila para calcular promedio de sus elementos (Recordar que la primera fila es 0): ")) 
    resultado = calcular_promedio(matriz, a)
    print("El promedio de los elementos de la fila",a,"da:",resultado)
    
    print()
    b = int(input("Ingresar numero de columna para calcular procentaje de elementos impares (Recordar que la primera colummna es 0): ")) 
    resultado = calcular_porcentaje(matriz, b)
    print("El porcentaje de elementos impares de la columna",b,"es:",resultado,"%")
    
    print()
    es_simetrica = matriz_simetrica_principal(matriz)
    if es_simetrica:
        print("La matriz es simetrica respecto a su diagonal principal")
    else:
        print("La matriz NO es simetrica respecto a su diagonal principal")
    
    print()
    es_simetrica = matriz_simetrica_secundaria(matriz)
    if es_simetrica:
        print("La matriz es simetrica respecto a su diagonal secundaria")
    else:
        print("La matriz NO es simetrica respecto a su diagonal secundaria")
        
    print()
    indices = columnas_capicuas(matriz)
    print("Las columnas capicuas son:", indices)
    
# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 2

if ejercicio == 2:
    print("Para cada una de las matrices del punto, desarrollar una funcion que la genere y escribir un programa que invoque a cada una de ellas y muestre por pantalla la matriz obtenida. \nEl tamaño de las matrices debe establecerse como NxN, y las funciones deben servir aunque este valor se modifique.")
    print()
    time.sleep(4)

    def matrizalpha(matriz):
        # 1 0 0 0 
        # 0 3 0 0
        # 0 0 5 0
        # 0 0 0 7
        d = 1
        for f in range(filas):
            for c in range(columnas):
                if f == c:
                    matriz[f][c] = d
                    d += 2
    
    def matrizbravo(matriz):
        # 0 0 0 27
        # 0 0 9 0
        # 0 3 0 0 
        # 1 0 0 0
        
        for f in range(filas):
            for c in range(columnas):
                if f + c == filas - 1:
                    matriz[f][c] = 3 ** (filas - 1 - f)         
    
    def matrizcharlie(matriz):
        # 4 0 0 0
        # 3 3 0 0 
        # 2 2 2 0
        # 1 1 1 1
        d = filas + 1
        for f in range(filas):
            d -= 1
            for c in range(columnas):
                if f >= c:
                    matriz[f][c] = d            
    
    def matrizdelta(matriz):
        # 8 8 8 8
        # 4 4 4 4
        # 2 2 2 2
        # 1 1 1 1
        
        for f in range(filas):
            for c in range(columnas):
                matriz[f][c] = 2 ** (filas - 1 - f)
    
    def matrizecho(matriz):
        # 0 1 0 2
        # 3 0 4 0
        # 0 5 0 6
        # 7 0 8 0
        d = 1
        for f in range(filas):
            for c in range(filas):
                if (f + c) % 2 == 1:  # Verificar si la suma de fila y columna es impar
                    matriz[f][c] = d
                    d += 1
    
    def matrizfoxtrot(matriz):
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
    
    def matrizgolf(matriz):
        # 1 2 3 4
        # 12 13 14 5
        # 11 16 15 6
        # 10 9 8 7
        d = 1
        inicio_fila, inicio_columna = 0, 0
        fin_fila, fin_columna = filas - 1, columnas - 1

        while inicio_fila <= fin_fila and inicio_columna <= fin_columna:
            # Llenar la fila superior
            for c in range(inicio_columna, fin_columna + 1):
                matriz[inicio_fila][c] = d
                d += 1
            inicio_fila += 1

            # Llenar la columna derecha
            for f in range(inicio_fila, fin_fila + 1):
                matriz[f][fin_columna] = d
                d += 1
            fin_columna -= 1

            # Llenar la fila inferior (en reversa)
            if inicio_fila <= fin_fila:
                for c in range(fin_columna, inicio_columna - 1, -1):
                    matriz[fin_fila][c] = d
                    d += 1
                fin_fila -= 1

            # Llenar la columna izquierda (en reversa)
            if inicio_columna <= fin_columna:
                for f in range(fin_fila, inicio_fila - 1, -1):
                    matriz[f][inicio_columna] = d
                    d += 1
                inicio_columna += 1
    
    def matrizhotel(matriz):
        # 1 2 4 7
        # 3 5 8 11
        # 6 9 12 14
        # 10 13 15 16
        d = 1
        for suma_filas_columnas in range(filas + columnas - 1):
            if suma_filas_columnas < columnas:
                fila_inicio = 0
                columna_inicio = suma_filas_columnas
            else:
                fila_inicio = suma_filas_columnas - columnas + 1
                columna_inicio = columnas - 1

            while fila_inicio < filas and columna_inicio >= 0:
                matriz[fila_inicio][columna_inicio] = d
                d += 1
                fila_inicio += 1
                columna_inicio -= 1
    
    def matrizindia(matriz):
        # 1 2 6 7
        # 3 5 8 13
        # 4 9 12 14
        # 10 11 15 16
        d = 1
        
        for suma_filas_columnas in range(filas + columnas - 1):
            if suma_filas_columnas % 2 == 0:  # Cambiar dirección de llenado en cada diagonal par
                if suma_filas_columnas < filas:
                    fila_inicio = suma_filas_columnas
                    columna_inicio = 0
                else:
                    fila_inicio = filas - 1
                    columna_inicio = suma_filas_columnas - filas + 1

                while fila_inicio >= 0 and columna_inicio < columnas:
                    matriz[fila_inicio][columna_inicio] = d
                    d += 1
                    fila_inicio -= 1
                    columna_inicio += 1
            else:
                if suma_filas_columnas < columnas:
                    fila_inicio = 0
                    columna_inicio = suma_filas_columnas
                else:
                    fila_inicio = suma_filas_columnas - columnas + 1
                    columna_inicio = columnas - 1

                while fila_inicio < filas and columna_inicio >= 0:
                    matriz[fila_inicio][columna_inicio] = d
                    d += 1
                    fila_inicio += 1
                    columna_inicio -= 1
    
    def reset(matriz):
        for f in range(filas):
            for c in range(columnas):
                matriz[f][c] = 0                
    
    factor = int(input("Ingresar numero N: "))
    
    filas = factor
    columnas = factor
    matriz = [[0]*columnas for i in range(filas)]
    
    matrizalpha(matriz)
    for fila in matriz:
        for elemento in fila:
            print("%3d" %elemento, end=" ")
        print()
    print()
    reset(matriz)
    matrizbravo(matriz)
    for fila in matriz:
        for elemento in fila:
            print("%3d" %elemento, end=" ")
        print()
    print()
    reset(matriz)    
    matrizcharlie(matriz)
    for fila in matriz:
        for elemento in fila:
            print("%3d" %elemento, end=" ")
        print()
    print()
    reset(matriz)
    matrizdelta(matriz)
    for fila in matriz:
        for elemento in fila:
            print("%3d" %elemento, end=" ")
        print()
    print()
    reset(matriz)
    matrizecho(matriz)
    for fila in matriz:
        for elemento in fila:
            print("%3d" %elemento, end=" ")
        print()
    print()
    reset(matriz)
    matrizfoxtrot(matriz)
    for fila in matriz:
        for elemento in fila:
            print("%3d" %elemento, end=" ")
        print()
    print()
    reset(matriz)
    matrizgolf(matriz)
    for fila in matriz:
        for elemento in fila:
            print("%3d" %elemento, end=" ")
        print()
    print()
    reset(matriz)
    matrizhotel(matriz)
    for fila in matriz:
        for elemento in fila:
            print("%3d" %elemento, end=" ")
        print()
    print()
    reset(matriz)
    matrizindia(matriz)
    for fila in matriz:
        for elemento in fila:
            print("%3d" %elemento, end=" ")
        print()
    print()

# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 3

if ejercicio == 3:
    print("Desarrollar una programa para rellenar una matriz de NxN con numeros enteros al azar comprendidos en el intervalo (0,N^2], de tal forma de que ningun numero se repita. \nImprimir la matriz por pantalla.")
    print()
    time.sleep(4)

    def rellenarmatriz(matriz, numero):
        filas = len(matriz)
        columnas = len(matriz[0])
        
        valores_unicos = list(range(1, numero**2 + 1))
        random.shuffle(valores_unicos)  # Mezclar la lista de valores únicos
        
        for f in range(filas):
            for c in range(columnas):
                if valores_unicos:
                    valor = valores_unicos.pop()  # Tomar el valor único siguiente
                    matriz[f][c] = valor
    
    def imprimirmatriz(matriz):
        for fila in matriz:
            for elemento in fila:
                print("%3d" %elemento, end=" ")
            print()
    
    # PROGRAMA PRINCIPAL 
    n = int(input("Ingresar numero N: "))
    filas = n
    columnas = n
    matriz = [[0]* columnas for i in range(filas)]
    rellenarmatriz(matriz, n)
    imprimirmatriz(matriz)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 4

if ejercicio == 4:
    print("Una fabrica de bicicletas guarda en una matriz la cantidad de unidades producidas en cada una de sus plantas durante una semana. \nDe este modo, cada columna representa el dia de la semana (Lunes: columna 0, Martes: Columna 1...) y cada fila representa a una de sus fabricas")
    print("Se solicita:")
    print("a- Crear una matriz con datos generados al azar de N fabricas durante una semana, considerando que la capacidad maxima de fabricacion es de 150 unidades por dia y puede suceder \nque en ciertos dias no se fabrique ninguna.")
    print("b- Mostrar la cantidad total de bicicletas fabricadas por cada fabrica.")
    print("c- Cual es el fabricante que mas produjo en un solo dia (detallar dia y fabrica).")
    print("d- Cual es el dia mas productivo, considerando todas las fabricas combinadas.")
    print("e- Crear una lista por comprension que contenga la menor cantidad fabricada por cada fabrica.")
    print()
    time.sleep(0)
    
    def rellenarmatriz(matriz):
        filas = len(matriz)
        columnas = len(matriz[0])
        for f in range(filas):
            for c in range(columnas):
                matriz[f][c] = random.randint(0, 150)
    
    def imprimirmatriz(matriz):
        for fila in matriz:
            for elemento in fila:
                print("%3d" %elemento, end=" ")
            print()        
    
    def maximo_fabricado(matriz):
        maximo = 0
        indice_f_maximo = 0
        indice_d_maximo = 0
        for f in range(filas):
            for c in range(columnas):
                if matriz[f][c] > maximo:
                    maximo = matriz[f][c]
                    indice_f_maximo = f
                    indice_d_maximo = c
        
        return maximo, indice_f_maximo, indice_d_maximo
            
    def sumar_columna(matriz, columna):
        suma = 0
        for fila in matriz:
            if 0 <= columna < len(fila):
                suma += fila[columna]
        return suma
    
    # PROGRAMA PRINCIPAL
    n = int(input("Ingresar cantidad de fabricas: "))
    filas = n
    columnas = 7
    matriz =[[0]* columnas for i in range(filas)]
    
    rellenarmatriz(matriz)
    imprimirmatriz(matriz)
    
    for f in range(filas):
        total = sum(matriz[f])
        print("La fabrica", f + 1,"fabricó",total,"bicicletas en la semana.")
    
    maxim, fabrica, dia = maximo_fabricado(matriz)
    print("La fabrica",fabrica+1,"fue la que mas produjo:",maxim,"bicicletas el dia",dia)
    
    maxim = 0
    for c in range(columnas):
        resultado = sumar_columna(matriz, c)
        if resultado > maxim:
            maxim = resultado
            dia = c
    print("Dia mas productivo:",dia,"con una produccion total de",maxim,"bicicletas.")
    
    menorfabricada = [min(fabrica) for fabrica in matriz]
    for i, cantidad in enumerate(menorfabricada):
        print("La fábrica", i + 1, "fabricó la menor cantidad de bicicletas:", cantidad)
    
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
