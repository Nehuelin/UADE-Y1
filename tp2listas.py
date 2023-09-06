import random 
import time

ejercicio = int(input("Que ejercicio queres probar? (NOW TESTING: 12): "))

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
        suma = sum(listarandom)
        return suma
    
    def exterminar(listarandom, target):
        i = 0
        while i < len(listarandom):
            if target in listarandom:
                listarandom.remove(target)
            i += 1
        return listarandom
    
    def escapicua(listarandom):
        reverso = listarandom.reverse()
        return listarandom == reverso
    
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
        print("d) Ninguna de las listas es capicua")
    
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
            cantidad = listarandom.count(listarandom[i])
            if cantidad > 1:
                rep = True
                break
        if rep:
            return True
        else:
            return False
                 
    def exterminar(listarandom):
        nuevalista = []
        for i in range(len(listarandom)):
            cantidad = listarandom.count(listarandom[i])
            if cantidad == 1:
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
    time.sleep(4)

    # Definir la lista original de palabras
    lista_original = ["Obelisco", "Azul", "Auto", "Gorra", "Avion"]
    print("Lista original:", lista_original)
    # Definir la lista de palabras a eliminar
    palabras_a_eliminar = ["Azul", "Avion", "Bicicleta"]

    # Crear una copia de la lista original utilizando list()
    lista_copia = list(lista_original)

    # Utilizar un bucle for con range() para iterar a través de los índices de la lista copia
    for i in range(len(lista_copia)):
        palabra = lista_copia[i]
        # Verificar si la palabra está en la lista de palabras a eliminar
        if palabra in palabras_a_eliminar:
            # Si la palabra está en la lista de palabras a eliminar, elimínala de la lista original
            lista_original.remove(palabra)
        
    # Imprimir las tres listas
    print("Palabras a eliminar:", palabras_a_eliminar)
    print("Lista Final:", lista_original)   
    
    
# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 5

if ejercicio == 5:
    print("\nEscribir una funcion que reciba una lista como parametro y devuelva True si la lista esta ordenada en forma ascendente o False en caso contrario. \nPor ejemplo ordenada([1 ,2, 3]) retorna True y ordenada(['b', 'a']) retorna False. \nDesarrollar ademas un programa para verificar el comportamiento de la funcion")
    print()
    time.sleep(4)

    def ordenada(lista):
        copia = list(lista)
        copia.sort()
        if copia == lista:
            return True
        else:
            return False
    
    lista1 = [1, 2, 3]
    lista2 = ['b', 'a']
    lista3 = [6, 5, 4]
    lista4 = ['x', 'y', 'z']
    
    ascendente = ordenada(lista1)
    if ascendente:
        print("La lista esta ordenada de forma ascendente (True)")
    elif not ascendente:
        print("La lista esta ordenada de forma descendente (False)")
    
        
    
# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 6

if ejercicio == 6:
    print("\nEscribir una funcion que reciba una lista de numeros enteros como parametro y la normalice, es decir que todos sus elementos deben sumar 1.0, respetando las posiciones relativas que cada elemento tiene en la lista original.")
    print("Desarrollar tambien un programa que permita verificar el comportamiento de la funcion. \nPor ejemplo, normalizar ([1, 1, 2]) debe devolver ([0.25, 0.25, 0.50]).")
    print()
    time.sleep(4)  

    def normalizar(lista):
        suma_total = sum(lista) # Calcula la suma de todos los elementos en la lista original
        
        if suma_total == 0: # Verifica que la suma total no sea cero para evitar divisiones por cero
            return -1  
        
        lista_normalizada = []
        
        for i in range(len(lista)): # Itera a través de la lista original y calcula los elementos normalizados
            elemento_normalizado = lista[i] / suma_total
            lista_normalizada.append(elemento_normalizado)
        
        return lista_normalizada

    # MAIN
    lista_original = []
    numero = int(input("Ingresar numero (-1 para finalizar): "))
    while numero != -1:
        lista_original.append(numero)
        numero = int(input("Ingresar numero (-1 para finalizar): "))

    resultado = normalizar(lista_original)
    print(resultado)   

# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 7

if ejercicio == 7:
    print("\nIntercalar los elementos de un lista entre los elementos de otra. \nLa intercalacion debe realizarse exclusivamente mediante la tecnica de rebanadas y no se creara una nueva lista, sino que se modificara la primera. ")
    print("Por ejemplo, si lista1 = [8, 1, 3] y lista2 = [5, 9, 7], lista1 debera quedar como [8, 5, 1, 9, 3, 7]")
    print()
    time.sleep(4)  
    
    lista1 = [8, 1, 3]
    lista2 = [5, 9, 7]
    
    a = 1
    b = 1
    for i in range(len(lista2)):
        lista1[a:b] = [lista2[i]]
        a += 2
        b += 2
    
    print(lista1)
    
# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 8

if ejercicio == 8:
    print("Utilizar la tecnica de listas por comprension para construir una lista con todos los numeros impares comprendidos entre 100 y 200.")
    print()
    time.sleep(4)  

    listaimpar = [i for i in range(100, 200) if i % 2 != 0]
    print(listaimpar)
    
# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 9

if ejercicio == 9:
    print("Generar e imprimir una lista por comprension entre A y B con los multiplos de 7 que no sean multiplos de 5. A y B se ingresan desde el teclado.")
    print()
    time.sleep(4)
    
    a = int(input("Ingresar numero A: "))
    b = int(input("Ingresar numero B: "))
    
    lista = [i for i in range(a, b) if i % 7 == 0 and i % 5 != 0]
    print(lista)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 10

if ejercicio == 10:
    print("Generar una lista con numeros al azar entre 1 y 100 y crear una nueva lista con los elementos de la primera que sean impares. \nEl proceso debera realizarse utilizando listas por comprension. Imprimir las dos listas por pantalla")
    print()
    time.sleep(4)    

    listarandom = [random.randint(1,100) for i in range(1, 50)]
    listaimpar = [listarandom[i] for i in range(len(listarandom)) if listarandom[i] % 2 != 0]
    
    print(listarandom)
    print(listaimpar)
    
# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 11

if ejercicio == 11:
    print("Una clinica necesita un programa para atender a sus pacientes. \nCada paciente que ingresa se anuncia en la recepcion indicando su numero de afiliado (numero entero de cuatro digitos) y ademas indica si viene por una urgencia (ingresando un 0) o con turno (ingresando un 1).")
    print("Para finalizar se ingresa -1 como numero de socio. Luego se solicita: \na- Mostrar un listado de los pacientes atendidos por urgencia y un listado de los pacientes atendidos por turno, en el orden que llegaron a la clinica.")
    print("b- Realizar la busqueda de un numero de afiliado e informar cuantas veces fue atendido por turno y cuantas por urgencia. Repetir esta busqueda hasta que se ingrese -1 como numero de afiliado")
    print()
    time.sleep(4)
    
    def checkdigitos(n):
        contador = 0
        while n > 0:
            n = n // 10
            contador = contador + 1
        return contador == 4
    
    def armarlistas(lista1, lista2):
        lista3 = []
        lista4 = []
        for i in range(len(lista2)):
            if lista2[i] == 0:
                lista3.append(lista1[i])
            else:
                lista4.append(lista1[i])
        return lista3, lista4

    def buscardatos(n, lista1, lista2):
        x = 0
        y = 0
        for i in range(len(lista1)):
            if n == lista1[i]:
                if lista2[i] == 0:
                    x += 1
                else:
                    y += 1
        return x, y
     
    #MAIN
    
    listaafiliados = []
    listarazon = []
    error = False
    listaurgencias = []
    listaturnos = []
    
    
    numafil = int(input("Ingresar numero de afiliado (4 digitos)(-1 para finalizar): "))
    while numafil != -1:
        cuatrodigitos = checkdigitos(numafil)
        if not cuatrodigitos:
            print("Numero de afiliado incorrecto")
            error = True
            break
        razon = int(input("0 para atencion de urgencia, 1 para atencion con Turno: "))
        if razon < 0 or razon > 1:
            print("Dato Incorrecto")
            error = True
            break
        else:
            listaafiliados.append(numafil)
            listarazon.append(razon)
        numafil = int(input("Ingresar numero de afiliado (4 digitos)(-1 para finalizar): "))
    
    if error:
        print()
    else:
        listaurgencias, listaturnos = armarlistas(listaafiliados, listarazon)
        print("a- LISTADO DE PACIENTES: ")
        print("Atendidos por urgencias:", listaurgencias)
        print("Atendidos por Turno:",listaturnos)
        
        
        print("b- BUSQUEDA DE AFILIADO: ")
        objetivo = int(input("Ingresar numero de afiliado (-1 para finalizar): "))
        while objetivo != -1:
            canturg, cantturn = buscardatos(objetivo, listaafiliados, listarazon)
            print("La persona con el numero de afiliado",objetivo,"fue atendido",canturg,"veces por urgencia, y",cantturn,"veces por turno")
            objetivo = int(input("Ingresar numero de afiliado (-1 para finalizar): "))
    
# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 12

if ejercicio == 12:
    print("Resolver el siguiente problema, utilizando funciones: ")
    print("Se desea llevar un registro de los socios que visitan un club cada dia. Para ello, se ingresa el numero de socio de cinco digitos hasta ingresar un 0 como fin de carga.\nSe solicita: ")
    print("a- Informar para cada socio, cuantas veces ingreso al club (cada socio debe aparecer solo una vez en el informe).")
    print("b- Solicitar un numero de socio que se dio de baja del club y eliminar todos sus ingresos. Mostrar los registros de entrada al club antes y despues de eliminarlo. Informar \ncuantos ingresos se eliminaron.")
    print()
    time.sleep(0)    
    
    def checkdigitos(n):
        contador = 0
        while n > 0:
            n = n // 10
            contador = contador + 1
        return contador == 5    
    
    def cantidad_ingresos(lista, target):
        cant = lista.count(target)
        return cant
    
    def borrar_ingresos(lista, target):
        contador = 0
        for i in range(len(lista)):
            while target in lista:
                lista.remove(target)
                contador += 1
        return contador
                        
    
    # MAIN
    listasocios = []
    listaunicos = []
    
    numsocio = int(input("Ingresar numero de socio (5 digitos)(0 para finalizar): "))
    while numsocio != 0:
        cincodigitos = checkdigitos(numsocio)
        if not cincodigitos:
            print("Cantidad de digitos invalida")
            break
        else:
            listasocios.append(numsocio)
            numsocio = int(input("Ingresar numero de socio (5 digitos)(0 para finalizar): ")) 
    
    for i in range(len(listasocios)):
        if listasocios[i] not in listaunicos:
            cantidad = cantidad_ingresos(listasocios, listasocios[i])
            print("El socio numero",listasocios[i],"ha ingresado",cantidad,"veces.")
            listaunicos.append(listasocios[i])    
    
    objetivo = int(input("Ingresar numero de socio a dar de baja: "))
    print("Registro de ingresos: ",listasocios)
    eliminados = borrar_ingresos(listasocios, objetivo)
    print("Registro actualizado: ",listasocios)
    print("Se han borrado",eliminados,"ingresos")
    
    
