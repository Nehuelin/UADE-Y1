import random 
import time

ejercicio = int(input("Que ejercicio queres probar? (NOW TESTING: ): "))
# 2, 7 y 10

# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 1

if ejercicio == 1:
    print("Escribir una funcion que devuelva la cantidad de digitos de un numero entero, sin utilizar cadenas de caracteres.")
    print()
    time.sleep(0)   
    
    def contar_digitos(numero):
        if abs(numero) < 10:
            return 1
        return 1 + contar_digitos(numero // 10)
        
    #Programa Principal
    num= int(input("Ingresar numero entero: "))
    cantidad = contar_digitos(num)
    print(f"El número {num} tiene {cantidad} dígitos.")
# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 2

if ejercicio == 2:
    print("Desarrollar una funcion que reciba un numero binario y lo devuelva convertido a su base decimal.")
    print()
    time.sleep(0)   

    def binario_a_decimal(_numero):
        if len(_numero) == 0:
            return 0  # Caso base: cadena vacía, el valor es 0 en decimal.

        # Obtenemos el último dígito (0 o 1) y lo convertimos a entero.
        ultimo_digito = int(_numero[-1])

        # Llamada recursiva para el resto de la cadena sin el último dígito.
        valor_restante = binario_a_decimal(_numero[:-1])

        # Calculamos el valor en decimal multiplicando el valor restante por 2 y sumando el último dígito.
        valor_decimal = valor_restante * 2 + ultimo_digito

        return valor_decimal
    numero = int(input("Ingresar numero binario: "))

# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 3

if ejercicio == 3:
    print("Escribir una funcion que devuelva la suma de los N primeros numeros naturales.")
    print()
    time.sleep(0)   

    def suma_naturales(n):
        if n == 1:
            return 1
        else:
            return n + suma_naturales(n - 1)
                    
    num = int(input("Ingresar numero natural: "))
    suma = suma_naturales(num)
    print(f"La suma de los numeros naturales hasta {num} da: {suma}")

# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 4

if ejercicio == 4:
    print("Desarrollar una funcion que devuelva el producto de dos numeros enteros por sumas sucesivas.")
    print()
    time.sleep(0) 
    
    def producto(x, y):
        if y == 0:
            return 0
        else:
            return x + producto(x, y - 1)
    
    num1 = int(input("Ingresar primer numero: "))
    num2 = int(input("Ingresar segundo numero: "))
    resultado = producto(num1, num2)
    print(f"El producto entre {num1} y {num2} es {resultado}.")

# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 5

if ejercicio == 5:
    print("Realizar una funcion que devuelva el resto de dos numeros enteros, utilizando restas sucesivas.")
    print()
    time.sleep(0) 

    def resto(x, y):
        if x < y:
            return x
        else:
            return resto(x - y, y)
    
    num1 = int(input("Ingresar primer numero: "))
    num2 = int(input("Ingresar segundo numero: "))
    resultado = resto(num1, num2)
    print(f"El resto entre {num1} y {num2} es {resultado}.")
    
# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 6

if ejercicio == 6:
    print("La funcion de Ackermann A(m,n) se define de la siguiente manera: ")
    print("--> n + 1             si m = 0")
    print("--> A(m-1,1)          si n = 0")
    print("--> A(m-1,A(m,n-1))   de otro modo")
    print("Imprimir un cuadro con los valores que adopta la funcion de m entre 0 y 3 y de n entre 0 y 7.")
    print()
    time.sleep(0) 

    def ackermann(m, n):
        if m == 0:
            return n + 1
        elif m > 0 and n == 0:
            return ackermann(m - 1, 1)
        elif m > 0 and n > 0:
            return ackermann(m - 1, ackermann(m, n - 1))
    
    for i in range(4):
        for j in range(7):
            valor = ackermann(i,j)
            print(valor, end=" ")
        print()
    
    

# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 7

if ejercicio == 7:
    print("Dados dos numero enteros no negativos, devolver el resultado de calcular el Maximo Comun Divisor (Tambien llamado Divisor Comun Mayor) basandose en las siguientes propiedades: ")
    print("--> MCD(X, X) = X")
    print("--> MCD(X, Y) = MCD(Y, X)")
    print("--> Si X > Y  => MCD(X, Y) = MCD(X-Y, Y)")
    print("Utilizando la funcion anterior calcular el MCD de todos los elementos de una lista de numeros enteros, sabiendo que MCD(X,Y,Z) = MCD((X,Y),Z). \nNo se permite utilizar iteraciones en ninguna etapa del proceso.")
    print()
    time.sleep(0) 

# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 8

if ejercicio == 8:
    print("Realizar la implementacion recursiva del metodo de seleccion para ordenar una lista de numeros enteros. \n\033[1mSugerencia\033[0m: Colocar el elemento mas pequeño en la primera posicion, y luego ordenar el resto de la lista con una llamada recursiva.")
    print()
    time.sleep(0) 
    
    def seleccion_recursiva(arr):
        # Caso base: si la lista está vacía o tiene un solo elemento, ya está ordenada.
        if len(arr) <= 1:
            return arr

        # Encontrar el índice del elemento más pequeño en la lista.
        indice_minimo = 0
        for i in range(1, len(arr)):
            if arr[i] < arr[indice_minimo]:
                indice_minimo = i

        # Intercambiar el elemento más pequeño con el primer elemento.
        arr[0], arr[indice_minimo] = arr[indice_minimo], arr[0]

        # Llamada recursiva para ordenar el resto de la lista (sin el primer elemento).
        resto_ordenado = seleccion_recursiva(arr[1:])

        # Combinar el primer elemento (ya ordenado) con el resto de la lista.
        return [arr[0]] + resto_ordenado

    # Ejemplo de uso
    lista = [64, 25, 12, 22, 11]
    lista_ordenada = seleccion_recursiva(lista)
    print("Lista ordenada:", lista_ordenada)
    
# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 9

if ejercicio == 9:
    print("Realizar una funcion recursiva para imprimir una matriz de MxN.")
    print()
    time.sleep(0)   
    
    
    def imprimir_matriz(matriz, fila, columna, m, n):
        # Caso base: si hemos llegado al final de la matriz
        if fila == m:
            return

        # Imprimir el elemento actual
        print(f"{matriz[fila][columna]:4}", end=" ")

        # Avanzar a la siguiente columna o fila cuando lleguemos al final de una fila
        if columna == n - 1:
            print()  # Cambiar de línea al final de la fila
            imprimir_matriz(matriz, fila + 1, 0, m, n)  # Pasar a la siguiente fila, columna 0
        else:
            imprimir_matriz(matriz, fila, columna + 1, m, n)  # Permanecer en la misma fila, siguiente columna

    # Solicitar la cantidad de filas (m) y columnas (n) al usuario
    m = int(input("Ingrese la cantidad de filas (m): "))
    n = int(input("Ingrese la cantidad de columnas (n): "))

    # Crear una matriz de ejemplo
    matriz_ejemplo = [[i * n + j + 1 for j in range(n)] for i in range(m)]

    # Imprimir la matriz
    imprimir_matriz(matriz_ejemplo, 0, 0, m, n)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 10

if ejercicio == 10:
    print("Escribir una funcion que sume todos los elementos de una matriz de MxN y devuelva el resultado")
    print()
    time.sleep(0)

    def suma_matriz(matriz, fila, columna):
        # Caso base: Si hemos llegado al final de la matriz, devolvemos 0.
        if fila == len(matriz):
            return 0
        # Caso recursivo: Sumamos el elemento actual y llamamos recursivamente para el siguiente elemento.
        suma_elemento_actual = matriz[fila][columna]
        
        # Moverse a la siguiente columna o siguiente fila cuando llegamos al final de la fila actual.
        if columna + 1 < len(matriz[fila]):
            return suma_elemento_actual + suma_matriz(matriz, fila, columna + 1)
        else:
            return suma_elemento_actual + suma_matriz(matriz, fila + 1, 0)

    # Ejemplo de uso
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    resultado = suma_matriz(matriz, 0, 0)
    print("La suma de todos los elementos de la matriz es:", resultado)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 11

if ejercicio == 11:
    print("Desarrollar una funcion que devuelva el minimo elemento de una matriz de MxN")
    print()
    time.sleep(0)
    
    def encontrar_minimo(matriz, fila, columna, minimo_actual):
        if fila == len(matriz):
            return minimo_actual  # Hemos recorrido toda la matriz, devolvemos el valor mínimo actual.
        
        elemento_actual = matriz[fila][columna]
        
        if elemento_actual < minimo_actual:
            minimo_actual = elemento_actual

        if columna + 1 < len(matriz[fila]):
            # Si hay más columnas en la fila actual, llamamos recursivamente para la siguiente columna.
            return encontrar_minimo(matriz, fila, columna + 1, minimo_actual)
        elif fila + 1 < len(matriz):
            # Si no hay más columnas en la fila actual pero hay más filas, llamamos recursivamente para la siguiente fila.
            return encontrar_minimo(matriz, fila + 1, 0, minimo_actual)
        else:
            return minimo_actual

    # Ejemplo de uso
    matriz = [
        [4, 2, 7],
        [1, 5, 3],
        [8, 6, 9]
    ]

    minimo = encontrar_minimo(matriz, 0, 0, matriz[0][0])
    print("El valor mínimo en la matriz es:", minimo)
