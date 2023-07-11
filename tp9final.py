import random 
import time

ejercicio = int(input("Que ejercicio queres probar?: "))


# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 1

if ejercicio == 1:
    print("\nLeer los números de legajo de los alumnos de un curso y su nota de examen final. \nEl fin de la carga se determina ingresando un -1 como legajo. \nSe debe validar que la nota ingresada esté entre 1 y 10. \nTerminada la lectura de datos, informar:")
    print("---> Cantidad de alumnos que aprobaron con nota mayor o igual a 4")
    print("---> Cantidad de alumnos que desaprobaron el examen. Nota menor a 4")
    print("---> Promedio de notas y legajos que superan el promedio")
    print("Luego se solicita mostrar un listado de legajos y calificaciones ordenado de manera ascendente según el número de legajo. \nResolver de dos formas: Utilizando dos listas paralelas y utilizando una matriz de dos filas.")
    time.sleep(4)
    
    def promediar(lista):
        total = 0
        contador = 0
        for i in range (len(lista)):
            total = total + lista[i]
            contador = contador + 1
        resultado = total/contador
        return resultado
    
    def burbujeolistas(lista1, lista2):
        desordenado = True
        while desordenado:
            desordenado = False
            for i in range(len(lista1)-1):
                if lista1[i] > lista1[i + 1]:
                    lista1[i], lista1[i + 1] = lista1[i + 1], lista1[i]
                    lista2[i], lista2[i + 1] = lista2[i + 1], lista2[i]                
                    desordenado = True
        return lista1, lista2
    
    def burbujeomatriz(matrixdata):
        desordenado = True
        while desordenado:
            desordenado = False
            for i in range(len(matrixdata[0])):
                for j in range(len(matrixdata[0])-1):
                    if matrixdata[0][j] > matrixdata[0][j+1]:               
                        matrixdata[0][j], matrixdata[0][j+1] = matrixdata[0][j+1], matrixdata[0][j]
                        matrixdata[1][j], matrixdata[1][j+1] = matrixdata[1][j+1], matrixdata[1][j]
                        desordenado = True
        return matrixdata
    
    def crearmatriz(lista1, lista2):
        matrix = []
        filas = 2
        columnas = len(lista2)
        
        for i in range(filas):
            matrix.append([])
            for j in range(columnas):
                matrix[i].append(0)
        
        for i in range(len(matrix[0])):
            for j in range(columnas):
                matrix[0][j] = lista1[j]
        
        for i in range(len(matrix[1])):
            for j in range(columnas):
                matrix[1][j] = lista2[j]
                
        return matrix
        
        
    legajo = 0
    nota = 0, True
    contaprobados = 0
    contdesaprobados = 0
    listalegajo = []
    listanota = []
    matriz = []
    metodo = 0
    
    metodo = int(input("\nElegir metodo de resolucion (1 para listas paralelas, 2 para matriz): "))
    
    if metodo == 1:
        legajo = int(input("Numero de legajo: "))
        while legajo != -1:
            if nota:
                listalegajo.append(legajo)
            nota = int(input("Nota del Alumno: "))
            
            if nota < 1 or nota > 10:
                print("La nota ingresada es invalida.")
                nota = False
            else:            
                listanota.append(nota)
                if nota >= 4:
                    contaprobados = contaprobados + 1
                elif nota < 4:
                    contdesaprobados = contdesaprobados + 1            
                nota = True
                legajo = int(input("Numero de legajo: "))

        promedio = promediar(listanota)    
        
        print("Cantidad de alumnos aprobados:", contaprobados)
        print()
        print("Cantidad de alumnos desaprobados:", contdesaprobados)
        print()
        print("El promedio es:", promedio)
        
        print("El legajo de los alumnos con nota por encima del promedio son: ")
        for n in range(len(listanota)):
            if listanota[n] > promedio:
                print(listalegajo[n])
        
        listafinallegajo, listafinalnota = burbujeolistas(listalegajo, listanota)
        
        print()
        print("Listas ordenadas de forma ascendente (por legajo): ")
        print(listafinallegajo)
        print(listafinalnota)
    
    
    contacolumnas = 0
    
    if metodo == 2:
        legajo = int(input("Numero de legajo: "))
        while legajo != -1:
            if nota:
                listalegajo.append(legajo)
                contacolumnas = contacolumnas + 1
            nota = int(input("Nota del Alumno: "))
            
            if nota < 1 or nota > 10:
                print("La nota ingresada es invalida.")
                nota = False           
                
            else:            
                listanota.append(nota)
                if nota >= 4:
                    contaprobados = contaprobados + 1
                elif nota < 4:
                    contdesaprobados = contdesaprobados + 1            
                nota = True
                legajo = int(input("Numero de legajo: "))        
        
        promedio = promediar(listanota)
            
        print("Cantidad de alumnos aprobados:", contaprobados)
        print()
        print("Cantidad de alumnos desaprobados:", contdesaprobados)
        print()
        print("El promedio es:", promedio)
        
        print("El legajo de los alumnos con nota por encima del promedio son: ")
        for n in range(len(listanota)):
            if listanota[n] > promedio:
                print(listalegajo[n])        
        
        matriz = crearmatriz(listalegajo, listanota)
        col = len(listanota)
        matrizfinal = burbujeomatriz(matriz)
    
        print("Matriz ordenada de forma ascendente (por legajo): ")
        for f in range(2):
            for c in range(col):
                print(matrizfinal[f][c], end=" ")
            print()
        

# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 2

if ejercicio == 2:
    print("\nUna Administradora de Consorcios necesita un sistema para poder gestionar el cobro de las expensas de un edificio de departamentos de 20 unidades. \nEn dos listas almacena la siguiente información: Número de unidad y superficie en metros cuadrados. \nValidar que no se ingresen números de unidades duplicadas. \nCada unidad paga de expensas un valor fijo por metro cuadrado, el que se ingresa por teclado. Se pide:")
    print("---> Informar el promedio de expensas del mes")
    print("---> Ordenar los listados de mayor a menor según la superficie. Mostrar por pantalla el listado ordenado informando el número de unidad y la superficie en metros cuadrados.")
    print()
    time.sleep(4)
    
    
    #Ingresar Numero de unidad, superficie en Metros^2, valor fijo. El valor fijo se multiplica por cada M^2
    #Lista de hasta 20 unidades (controlar el limite y los duplicados)
    #LIsta para superificie en M2
    #Ingresar valor fijo, indicar promedio final
    
    def promedioexpensas(listam):
        contador = 0
        total = 0
        for k in range(len(listam)):
            total = total + listam[k]
            contador = contador + 1
        final = total / contador
        return final
    
    def burbujeo(listan, listam):
        desordenado = True
        while desordenado:
            desordenado = False    
            for k in range(len(listam)-1):
                    if listam[k] < listam[k+1]:
                        aux = listam[k]
                        listam[k] = listam[k+1]
                        listam[k+1] = aux
                        aux = listan[k]
                        listan[k] = listan[k+1]
                        listan[k+1] = aux
                        desordenado = True
        
        return listan, listam
    
    listaunidades = []
    listasuperficie = []
    valorfijo = 0
    listaexpensas = []
    
    
    valorfijo = int(input("Ingresar valor fijo: "))
    
    for i in range(20):
        unidad = int(input("Ingresar el numero de la unidad: "))
        duplicado = False        
        for j in range(len(listaunidades)):
            if listaunidades[j] == unidad:
                duplicado = True
        if duplicado:
            print("El numero ingresado es invalido")
        elif duplicado == False: 
            superficie = int(input("Ingresar tamaño de superficie: "))
            if superficie > 0:
                listaunidades.append(unidad)
                listasuperficie.append(superficie)
            else: 
                print("El numero es invalido")
    
    for i in range(len(listasuperficie)):
        resultado = valorfijo * listasuperficie[i]
        listaexpensas.append(resultado)
    
    promediofinal = promedioexpensas(listaexpensas)
    
    listafinal1, listafinal2 = burbujeo(listaunidades, listasuperficie)
    
    print()
    for i in range(len(listafinal1)):
        print("Numero de Unidad: ", listafinal1[i])
        print("Superficie en Metros Cuadrados: ",listafinal2[i])
        
    print("\nEl promedio final de las expensas es:", promediofinal)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 3

if ejercicio == 3:
    print("\nHora de jugar: Desarrollar un programa que genere un número entero al azar de cuatro cifras y le proponga al usuario que lo descubra, ingresando valores repetidamente hasta hallarlo. \nEn cada intento el programa mostrará mensajes indicando si el número ingresado es mayor o menor que el valor secreto. \nPermitir que el usuario abandone la partida al ingresar -1. \nAl terminar el juego informar la cantidad de intentos realizada, haciendo que el usuario ingrese su número de documento si mejoró la mejor marca de intentos obtenida hasta el momento. \nLuego mostrar la lista ordenada de los 5 mejores puntajes (indicando también a quién pertenecen) y preguntar si se desea jugar otra vez, reiniciando el juego en caso afirmativo.")
    print()
    time.sleep(4)
    
    def burbujeo(lista1, lista2):
            desordenado = True
            while desordenado:
                desordenado = False
                for i in range(len(lista2)-1):
                    if lista2[i] < lista2[i+1]:
                        aux = lista2[i]
                        lista2[i] = lista2[i+1]
                        lista2[i+1] = aux
                        aux = lista1[i]
                        lista1[i] = lista1[i+1]
                        lista1[i+1] = aux                        
                        desordenado = True 
            return lista1, lista2
    
    
    listaintentos = []
    listadni = []
    pregunta = int(input("Para a jugar, introduzca 1. Sino, introduzca cualquier numero: "))
    if pregunta == 1:
        quierojugar = True
    else: 
        quierojugar = False
       
    while quierojugar:
        print("Generando numero secreto")
        numerosecreto = random.randint(1000, 9999)
        time.sleep(2)
    
        print("Listo! Intenta encontrar el numero secreto!")
        contador = 0
        terminarjuego = False
        while terminarjuego == False:
            n = int(input("Ingresar numero: ")) 
            if n == -1:
                print("Terminando juego")
                print("Cantidad de intentos:",contador)
                terminarjuego = True 
                pregunta = 0
            else:
                contador += 1     
                if n < numerosecreto:
                    print("El numero secreto es Mayor!")
                elif n > numerosecreto: 
                    print("El numero secreto es Menor!")        
                elif n == numerosecreto:
                    print("Encontraste el numero secreto!")
                    print("Cantidad de intentos: ", contador)
                    pregunta = 0 
                    terminarjuego = True
    
        dni = int(input("Ingresar DNI: "))
        listadni.append(dni)
        listaintentos.append(contador)
        
        listafinaldni, listafinalintentos = burbujeo(listadni, listaintentos)
        print("Leaderboard (5 BEST): ")
        
        for k in range(len(listafinalintentos)):
            print(listafinalintentos[k], "(DNI: ",listafinaldni[k],")")
        
        pregunta = int(input("Para a jugar, introduzca 1. Sino, introduzca cualquier numero: "))
        if pregunta == 1:
            quierojugar = True
        else: 
            quierojugar = False
    
# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 4

if ejercicio == 4:
    print("\nModificar el programa anterior para que las pistas brindadas por el programa no sean del tipo 'es mayor' o 'es menor' sino 'M dígitos correctos' y 'N dígitos aproximados'. \nSe considera que un dígito es correcto cuando tanto su valor como su posición coinciden con los del número secreto, \nmientras que un dígito es aproximado cuando coincide el valor, pero no su posición")
    print()
    time.sleep(4)    
    
    def burbujeo(lista1, lista2):
        desordenado = True
        while desordenado:
            desordenado = False
            for i in range(len(lista2)-1):
                if lista2[i] < lista2[i+1]:
                    aux = lista2[i]
                    lista2[i] = lista2[i+1]
                    lista2[i+1] = aux
                    aux = lista1[i]
                    lista1[i] = lista1[i+1]
                    lista1[i+1] = aux                        
                    desordenado = True 
        return lista1, lista2
    
    def revisardigitos(a):
        digits = []
        divisor = 1000
        while divisor >= 1:
            digito = a // divisor
            digits.append(digito)
            a %= divisor
            divisor //= 10
        return digits
    
    def controlador(b, c):
        digitossecretos = revisardigitos(b)
        digitosn = revisardigitos(c)
        
        m = 0
        n = 0        
        
        for i in range(len(digitossecretos)):
            if digitossecretos[i] == digitosn[i]:
                m += 1
            else:
                for j in range(len(digitossecretos)):
                    if j != i and digitosn[i] == digitossecretos[j]:
                        n += 1        

        return m, n
        
    listaintentos = []
    listadni = []
    pregunta = int(input("Para a jugar, introduzca 1. Sino, introduzca cualquier numero: "))
    if pregunta == 1:
        quierojugar = True
    else: 
        quierojugar = False
       
    while quierojugar:
        print("Generando numero secreto")
        numerosecreto = random.randint(1000, 9999)
        time.sleep(2)
        
    
        print("Listo! Intenta encontrar el numero secreto!")
        contador = 0
        terminarjuego = False
        while terminarjuego == False:
            n = int(input("Ingresar numero: ")) 
            if n == -1:
                print("Terminando juego")
                print("Cantidad de intentos:",contador)
                terminarjuego = True 
                pregunta = 0
            else:
                contador += 1
                correctos, aproximados = controlador(numerosecreto, n)              
                if n == numerosecreto:
                    print("Encontraste el numero secreto!")
                    print("Cantidad de intentos: ", contador)
                    pregunta = 0 
                    terminarjuego = True
                else: 
                    print("Numeros Correctos:",correctos)
                    print("Numeros Aproximados:",aproximados)
    
        dni = int(input("Ingresar DNI: "))
        listadni.append(dni)
        listaintentos.append(contador)
        
        listafinaldni, listafinalintentos = burbujeo(listadni, listaintentos)
        print("Leaderboard (5 BEST): ")
        
        for k in range(len(listafinalintentos)):
            print(listafinalintentos[k], "(DNI: ",listafinaldni[k],")")
        
        pregunta = int(input("Para a jugar, introduzca 1. Sino, introduzca cualquier numero: "))
        if pregunta == 1:
            quierojugar = True
        else: 
            quierojugar = False    

# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 5

if ejercicio == 5:
    print("\nIngresar por teclado un número N y construir una lista llamada SECUENCIAS con N números enteros al azar entre 1 y 20. \nEsta lista se caracterizará porque sus valores deben encontrarse divididos en secuencias de números separadas por ceros, cuya suma no sea mayor que 20. \nPara eso se deberá agregar un elemento de valor 0 a fin de separar cada secuencia de la siguiente, cuidando que ninguna secuencia sume más de 20. \nAgregar un 0 adicional al final de la lista y mostrar la lista obtenida por pantalla.")
    print()
    time.sleep(4)
    
    
    n = int(input("Ingresar numero entero: "))
    
    secuencia = []
    suma = 0
    contador = 0
    
    for i in range(n):
        numero = (random.randint(1,20))
        contador += 1
        suma += numero
        if suma > 20:
            secuencia.append(0)
            suma = 0
        elif contador == (n):
            secuencia.append(0)
        else: 
            secuencia.append(numero)
    
    print(secuencia)     

# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 6

if ejercicio == 6:
    print("\nA partir de la lista SECUENCIAS generada en el ejercicio anterior, imprimir la secuencia más larga almacenada en la misma. \nSi hubiera varias secuencias con la misma longitud máxima deberán mostrarse todas las que correspondan.")
    print()
    time.sleep(0)   

    n = int(input("Ingresar numero entero: "))
    
    secuencia = []
    suma = 0
    contador = 0
    secuenciaactual = []
    secuenciafinal = []
    maximo = 0
    
    for i in range(n):
        numero = (random.randint(1,20))
        contador += 1
        suma += numero
        if suma > 20:
            secuencia.append(0)
            suma = 0
        elif contador == (n):
            secuencia.append(0)
        else: 
            secuencia.append(numero)
    
    print(secuencia) 
    
    for num in range (len(secuencia)):
        num = secuencia[i]
        if num != 0:
            secuenciaactual.append(num)
        else:
            if len(secuenciaactual) > maximo:
                secuenciafinal = [secuenciaactual]
                maximo = len(secuenciaactual)
            elif len(secuenciaactual) == maximo:
                secuenciafinal.append(secuenciaactual)
            secuenciaactual = []
    
    if len(secuenciaactual) > maximo:
        secuenciafinal = [secuenciaactual]
    elif len(secuenciaactual) == maximo:
        secuenciafinal.append(secuenciaactual)            

    
    print("Secuencia mas larga almacenada:")
    
    for i in secuenciafinal:
        print(i)