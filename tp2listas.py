import random 
import time

ejercicio = int(input("Que ejercicio queres probar? (NOTA: Ejercicios 4 y 5 INCOMPLETOS por contenido no visto): "))

# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 1

if ejercicio == 1:
    print("\nDesarrollar cada una de las siguientes funciones y escribir un programa que permita verificar su funcionamiento imprimiendo la lista luego de invocar a cada funci0n:")
    print("a. Cargar una lista con numeros al azar de cuatro digitos. La cantidad de elementos tambien sera un numero al azar de dos digitos. \nb. Calcular y devolver la sumatoria de todos los elementos de la lista anterior. \nc. Eliminar todas las apariciones de un valor en la lista anterior. El valor a eliminar se ingresa desde el teclado y la funcion lo recibe como parametro. \nd. Determinar si el contenido de una lista cualquiera es capicua, sin usar listas auxiliares. Un ejemplo de lista capicua es [50, 17, 91, 17, 50]. ")
    print()
    time.sleep(4)
    
    def cargarlista():
        listarandom = []
        for i in range(random.randint(10,99)):
            listarandom.append(random.randint(1000,9999))
        return listarandom
    
    def sumarlista(listarandom):
        suma = 0
        for i in range(len(listarandom)):
            suma = suma + listarandom[i]
        return suma
    
    def exterminar(listarandom, target):
        i = 0
        while i < len(listarandom):
            if listarandom[i] == target:
                del listarandom[i]
            else:
                i += 1
        return listarandom
    
    def escapicua(listarandom):
        largo = len(listarandom)
        capicua = True
        for i in range(largo // 2):
                if listarandom[i] != listarandom[largo - i - 1]:
                    capicua = False
        
        return capicua    
    
    # MAIN
    
    lista = cargarlista()
    suma = sumarlista(lista)
    
    print("a)", lista)
    print("b) La suma del contenido de la lista da:", suma)
    
    valor = int(input("Ingresar valor a eliminar: "))    
    
    listareducida = exterminar(lista, valor)    
    print("c)", listareducida)
    
    lista1palindromo = escapicua(lista)
    lista2palindromo = escapicua(listareducida)
    
    if lista1palindromo:
        print("d) La primera lista es capicua")
    elif lista2palindromo:
        print("d) La segunda lista es capicua")
    else:
        print("d) Ninguna de las listas es es capicua")
    
# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 2

if ejercicio == 2:
    print("\nEscribir funciones para:")
    print("a. Generar una lista de 50 numeros aleatorios del 1 al 100.")
    print("b. Recibir una lista como parametro y devolver True si la misma contiene algun elemento repetido. La funcion no debe modificar la lista.")
    print("c. Recibir una lista como parametro y devolver una nueva lista con los elementos unicos de la lista original, sin importar el orden.")
    print("Combinar las tres funciones en un mismo programa")
    print()
    time.sleep(4)
    
    def generarlista():
        listarandom = []
        for i in range(50):
            listarandom.append(random.randint(1,100))            
        return listarandom
    
    def repetido(listarandom):
        rep = False
        for i in range(len(listarandom)):
            for j in range(i):
                if listarandom[i] == listarandom[j]:
                    rep = True
        
        if rep:
            return True
        else:
            return False
                 
    def exterminar(listarandom):
        nuevalista = []
        for i in range(len(listarandom)):
            duplicado = False
            for j in range(i):
                if listarandom[i] == listarandom[j]:        
                    duplicado = True
            if duplicado == False:
                nuevalista.append(listarandom[i])

        return nuevalista
        
    # MAIN
    lista = generarlista()
    esrepetido = repetido(lista)
    
    print(lista)
    if esrepetido:
        print("Hay elemento repetido en la lista")  
    else:
        print("No hay elemento repetido en la lista")              
    
    listaunica = exterminar(lista)
    print(listaunica)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 3

if ejercicio == 3:
    print("\nCrear una lista con los cuadrados de los numeros entre 1 y N (ambos incluidos), donde N se ingresa desde el teclado. \nLuego se solicita imprimir los ultimos 10 valores de la lista.")
    print()
    time.sleep(4)
    
    n = int(input("Ingresar ultimo numero de la lista: "))
    
    lista = []
    
    
    for i in range(1, n+1):
        cuadrado = i * i
        lista.append(cuadrado)

    print(lista)
    
    print("Ultimos 10 valores:")
    for i in range(len(lista)-10, len(lista)):
        print(lista[i])
    
# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 4

if ejercicio == 4:
    print("\nEliminar de una lista de palabras las palabras que se encuentran en una segunda lista. \nImprimir la lista original, la lista de palabras a eliminar y la lista resultante.")
    print()
    time.sleep(0)

    primeralista = ['Hola', 'Buenos', 'Dias', 'Como', 'Estas']
    segundalista = ['Malo', 'Omegalul', 'Melodia', 'Hola', 'Buenos']
    terceralista = []
    
    print(primeralista)
    for palabra in range(len(primeralista)):
            print() 
            
    print(terceralista)
    print(primeralista)
    
# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 5

if ejercicio == 5:
    print("\n")
    print()
    time.sleep(0)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 6

if ejercicio == 6:
    print("\nEscribir una funcion que reciba una lista de numeros enteros como parametro y la normalice, es decir que todos sus elementos deben sumar 1.0, respetando las posiciones relativas que cada elemento tiene en la lista original.")
    print("Desarrollar tambien un programa que permita verificar el comportamiento de la funcion. \nPor ejemplo, normalizar ([1, 1, 2]) debe devolver ([0.25, 0.25, 0.50]).")
    print()
    time.sleep(0)  

    def normalizar(numeros):
        suma = sum(numeros)
        
        valoresnormalizados = []
        for i in range(len(numeros)):
            valoresnormalizados.append(i / suma)
        
        return valoresnormalizados
    
    listanumeros = [1, 1, 2]   
    
    listanumeros = normalizar(listanumeros)
    print(listanumeros)    
    