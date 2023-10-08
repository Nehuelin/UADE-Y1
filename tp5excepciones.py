import random 
import time
import math

ejercicio = int(input("Que ejercicio queres probar? (NOW TESTING: 7): "))
# 1 y 3

# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 1

if ejercicio == 1:
    print("Desarrollar una funcion para ingresar a traves del teclado un numero natural. \nLa funcion rechazara cualquier ingreso invalido de datos utilizando excepciones y mostrara la razon exacta del error. \nControlar que se ingrese un numero, que ese numero sea entero y que sea mayor que 0. \nDevolver el valor ingresado cuando este sea el correcto. Escribir tambien un programa que permita probar el correcto funcionamiento de la misma.")
    print()
    time.sleep(0)
    
    def ingresarnumero():
        while True:
            try:
                numero = input("Ingresar numero natural positivo: ")
                for digitos in numero:
                    assert digitos != ".", "El numero no es entero"
                assert int(numero) > 0, "El numero no es mayor que 0"
            except ValueError:
                print("No se ingresó un numero")
            except AssertionError as mensaje:
                print(mensaje)
            else:
                return numero
    
    # Programa Principal
    valor = ingresarnumero()
    print(f"El numero {valor} cumple con las condiciones ")

# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 2

if ejercicio == 2:
    print('Realizar una funcion que reciba como parametro dos cadenas de caracteres conteniendo numeros reales, sume ambos valores y devuelva el resultado como un numero real. \nDevolver -1 si alguna de las cadenas no contiene un numero valido, utilizando manejo de excepciones para detectar el error.')
    print()
    time.sleep(0)
    
    def sumarreales(real1, real2):
        try:
            total = float(real1) + float(real2)
        except ValueError:
            return -1
        else:
            return total
    
    # Programa Principal
    num1 = input("Ingresar primer numero real: ")
    num2 = input("Ingresar segundo numero real: ")
    resultado = sumarreales(num1, num2)
    print(f"El resultado es {resultado}")
    
# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 3

if ejercicio == 3:
    print('Desarrollar una funcion que devuelva una cadena de caracteres con el nombre del mes cuyo numero se recibe como parametro. \nLos nombres de los meses deberan obtenerse de una lista de cadenas de caracteres inicializada dentro de la funcion. \nDevolver una cadena vacia si el numero de mes es invalido. La deteccion de meses invalidos debera realizarse a traves de excepciones.')
    print()
    time.sleep(0)
    
    def nombremes(numero):
        lista = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
        try:
            assert 0 < numero < 13
        except AssertionError:
            print("Numero de mes invalido")
            return ""
        else:
            nombre = lista[numero-1]
            return nombre
        
    # Programa Principal
    num = int(input("Ingresar numero de mes: "))
    mes = nombremes(num)    
    print(mes)
    
# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 4

if ejercicio == 4:
    print('Todo programa Python es susceptible de ser interrumpido mediante la pusalcion de las teclas Ctrl-C, lo que genera una excepcion del tipo "KeyboardInterrupt". \nRealizar un programa para imprimir los numeros enteros entre 1 y 100000, y que solicite confirmacion al usuario antes de detenerse cuando se presione Ctrl-C.')
    print()
    time.sleep(0)
    
    for i in range(1,100001):
        try:
            print(i, end=" ") 
        except KeyboardInterrupt:
            print()
            seguir = input("Quiere finalizar el programa? (S/N): ")
            if seguir == "S":
                raise KeyboardInterrupt

# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 5

if ejercicio == 5:
    print('La raiz cuadrada de un numero puede obtenerse mediante la funcion ".sqrt()" del modulo "math". \nEscribir un programa que utilize esa funcion para calcular la raiz cuadrada de un numero cualquiera ingresado a traves del teclado. \nEl programa debe utilizar manejo de excepciones para evitar errores si se ingresa un numero negativo.')
    print()
    time.sleep(0)
    
    while True:
        numero = int(input("Ingresar numero positivo: "))
        try:
            resultado = math.sqrt(numero)
        except ValueError:
            print("No se admiten numeros negativos")
        else:
            print(f"El resultado es {resultado}")
            break

# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 6

if ejercicio == 6:
    print('El metodo "index" permite buscar un elemento dentro de una lista, devolviendo la posicion que este ocupa. \nSin embargo, si el elemento no pertenece a la lista se produce una excepcion del tipo "ValueError". \nDesarrollar un programa que cargue una lista con numeros enteros ingresados a traves del teclado (terminando con -1) y permita que el usuario ingrese el valor de algunos elementos para visualizar la posicion que ocupan, utilizando el metodo "index". \nSi el numero no pertenece a la lista se imprimira un mensaje de error y se solicitara otro para buscar. \nAbortar el proceso al tercer error detectado. No utilizar el operador "in" durante la busqueda.')
    print()
    time.sleep(0)
    
    lista = []
    
    numero = int(input("Ingresar numero entero (-1 para terminar): "))
    while numero != -1:
        lista.append(numero)
        numero = int(input("Ingresar numero entero (-1 para terminar): "))
    
    contador = 0
    while True:
        objetivo = int(input("Ingresar valor a buscar: "))
        try: 
            for i in range(len(lista)):
                coordenada = lista.index(objetivo)
        except ValueError:
            print("Error, el valor ingresado no esta en la lista.")
            contador += 1
            if contador == 3:
                break
        else:
            print(f"Posicion del valor: {coordenada}")

# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 7

if ejercicio == 7:
    print('Escribir un programa que juegue con el usuario a adivinar un numero. El programa debe generar un numero al azar entre 1 y 500 y el usuario debe adivinarlo. \nPara eso, cada vez que se introduce un valor se muestra un mensaje indicando si el numero que tiene que adivinar es mayor o menor que el ingresado. \nCuando consiga adivinarlo, se debe imprimir en pantalla la cantidad de intentos que le tomo hallar el numero. \nSi el usuario introduce algo que no sea un numero se mostrara un mensaje en pantalla y se lo contara como un intento mas.')
    print()
    time.sleep(0)
    
    objetivo = random.randint(1,500)
    intentos = 0
    print("Intenta encontrar el numero secreto!")
    while True:    
        try:
            intentos += 1
            numero = int(input("Ingresar numero: "))
        except ValueError:
            print("Datos invalidos")
        else:
            if numero < objetivo:
                print("El numero secreto es mayor")
            elif numero > objetivo:
                print("El numero secreto es menor")
            elif numero == objetivo:
                print("Hallaste el numero!! ")
                break
    
    print(f"Intentos realizados: {intentos}")     
