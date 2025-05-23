import random 
import time

ejercicio = int(input("Que ejercicio queres probar? (NOW TESTING: ): "))

# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 1

if ejercicio == 1:
    print("Desarrollar las siguientes funciones utilizando tuplas para representar fechas y horarios, y luego escribir un programa para verificar su comportamiento:")
    print("a. Ingresar una fecha desde el teclado, verificando que corresponda a una fecha valida")
    print("b. Sumar N dias a la fecha")
    print("c. Ingresar un horario desde el teclado, verificando que sea correcto")
    print("d. Calcular la diferencia entre dos horarios. Si el primer horario fuera mayor al segundo se considerara que el primero corresponde al dia anterior. En ningun caso la diferencia puede superar las 24 horas.")
    print()
    time.sleep(0)   

    def ingresar_fecha():
        dia = int(input("Ingresar dia: "))
        mes = int(input("Ingresar mes: "))
        año = int(input("Ingresar año: "))
    
    def sumar_dias():
        ...
    
    def ingresar_horario():
        hora = int(input("Ingresar hora: "))
        minuto = int(input("Ingresar minuto: "))
        segundo = int(input("Ingresar segundos: "))
    
    def diferencia_horarios():
        ...

# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 2

if ejercicio == 2:
    print("Escribir una funcion que reciba como parametro una tupla conteniendo una fecha (dia,mes,año) y devuelva una cadena de caracteres con la misma fecha expresada en formato extendido.")
    print('Por ejemplo, para (12,10,17) devuelve "12 de Octubre de 2017". Escribir tambien un programa para verificar su comportamiento')
    print()
    time.sleep(0)   

    

# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 3

if ejercicio == 3:
    print("Desarrollar un programa que utilice una funcion que reciba como parametro una cadena de caracteres conteniendo una direccion de correo electronico y devuelva una tupla con las distintas partes que componen dicha direccion. ")
    print("Ejemplo: alguien@uade.edu.ar -> (alguien, uade, edu, ar)")
    time.sleep(0)   

    def dividir_direccion_correo(correo):
        usuario, dominio = correo.split('@')
        partes_dominio = dominio.split('.')
        return usuario, *partes_dominio

    # Programa Principal
    direccion_correo = input("Ingresar correo electronico: ")
    partes = dividir_direccion_correo(direccion_correo)
    print(partes)
    
# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 4

if ejercicio == 4:
    print("Escribir una funcion que indique si dos fichas de domino encajan o no. Las fichas son recibidas en dos tuplas, por ejemplo: (3, 4) y (5, 4). \nLa funcion devuelve True o False. Escribir tambien un programa para verificar su comportamiento.")
    time.sleep(0)   

    def encajan_fichas(_ficha1, _ficha2):
        if _ficha1[0] in _ficha2 or _ficha1[1] in _ficha2:
            return True
        else:
            return False

    # Programa Principal
    try:
        numero1 = int(input("Ingresar numero entre 1 y 6: "))
        assert numero1 > 0 and numero1 < 7
        numero2 = int(input("Ingresar segundo numero entre 1 y 6: "))
        assert numero2 > 0 and numero2 < 7
        ficha1 = numero1, numero2
        print(f"FICHA 1: {ficha1}")
        numero1 = int(input("Ingresar numero entre 1 y 6: "))
        assert numero1 > 0 and numero1 < 7
        numero2 = int(input("Ingresar segundo numero entre 1 y 6: "))
        assert numero2 > 0 and numero2 < 7
        ficha2 = numero1, numero2
        print(f"FICHA 2: {ficha2}")
    except AssertionError as mensaje:
        print("Numero fuera de rango.")
    except ValueError:
        print("Valor invalido.")
    else: 
        encajan = encajan_fichas(ficha1, ficha2)
        if encajan:
            print("Las fichas encajan.")
        else:
            print("Las fichas NO encajan.")

# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 5

if ejercicio == 5:
    print("En geometria un vector es un segmento de recta orientado que va desde un punto A hasta un punto B. \nLos vectores en el plano se representan mediante un par ordenado de numeros reales (x, y) llamados \033[1mcomponentes\033[0m.")
    print("Para representarlos basta con unir el origen de coordenadas con el punto indicado en sus componentes.")
    print("Dos vectores son \033[1mortogonales\033[0m cuando son perpendiculares entre si. Para determinarlo basta con calcular su producto escalar y verificar si es igual a 0.")
    print("Ejemplo: A = (2, 3) y B = (-3, 2) ---> 2 * (-3) + 3 * 2 = -6 + 6 = 0 ---> Son ortogonales")
    print("Escribir una funcion que reciba dos vectores en forma de tuplas y devuelva un valor de verdad indicando si son ortogonales o no. Desarrollar tambien un programa que permita verificar el comportamiento de la funcion.")
    print()
    time.sleep(0)   

    def vectores_ortogonales(_vector1, _vector2):
        resultado = (_vector1[0] * vector2[0]) + (_vector1[1] * vector2[1])
        return True if resultado == 0 else False
    
    # Programa Principal
    try:
        numero1 = int(input("Ingresar coordenada x: "))
        numero2 = int(input("Ingresar coordenada y: "))
        vector1 = numero1, numero2
        print(f"VECTOR 1: {vector1}")
        numero1 = int(input("Ingresar coordenada x: "))
        numero2 = int(input("Ingresar coordenada y: "))
        vector2 = numero1, numero2
        print(f"VECTOR 2: {vector2}")
    except ValueError:
        print("Valor invalido.")
    else: 
        ortogonales = vectores_ortogonales(vector1, vector2)
        if ortogonales:
            print("Los vectores son ortogonales")
        else:
            print("Los vectores NO son ortogonales")

# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 6

if ejercicio == 6:
    print("Ingresar una frase desde el teclado y usar un conjunto para eliminar las palabras repetidas, dejando un solo ejemplar de cada una. Finalemnte mostrar las palabras ordenadas segun su longitud.")
    print()
    time.sleep(0)   

    frase = input("Ingresar frase: ")
    sin_repetidos = {palabras.lower().rstrip(",") for palabras in frase.split()}
    ordenados = sorted(sin_repetidos)
    for i in range(len(ordenados)):
        longitud = len(ordenados[i])
        print(ordenados[i], longitud)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 7

if ejercicio == 7:
    print("Definir un conjunto con numeros enteros entre 0 y 9. Luego solicitar valores al usuario y eliminarlos del conjunto mediante el metodo \033[1mremove\033[0m, mostrando el contenido del conjunto luego de cada eliminacion. \nFinalizar el proceso al ingresar -1. \nUtilizar manejo de excepciones para evitar errores al intentar quitar elementos inexistentes.")
    print()
    time.sleep(0)   

    conjunto = {random.randint(0,9) for x in range(random.randint(1,10))}
    print(conjunto)

    while True:
        try: 
            valor = int(input("Ingresar valor a eliminar: "))
            while valor != -1:
                conjunto.remove(valor)
                print(conjunto)
                valor = int(input("Ingresar valor a eliminar: "))
            break
        except ValueError:
            print("Dato invalido")
        except KeyError:
            print("Valor no encontrado")

# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 8

if ejercicio == 8:
    print("Generar e imprimir un diccionario donde las claves sean numeros enteros entre 1 y 20 (ambos incluidos) y los valores asociados sean el cuadrado de las claves.")
    print()
    time.sleep(0)   

    diccionario = {x: x**2 for x in range(1, 21)}
    print(diccionario)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 9

if ejercicio == 9:
    print("Escribir una funcion que reciba un numero entero N y devuelva un diccionario con la tabla de multiplicar de N del 1 al 12. Escribir tambien un programa para probar la funcion.")
    print()
    time.sleep(0)   

    def tabla_multiplicacion(_numero):
        _diccionario = {x: x * _numero for x in range(1, 13)}
        return _diccionario
    
    # Programa Principal
    numero = int(input("Ingresar numero entero: "))
    diccionario = tabla_multiplicacion(numero)
    print(diccionario)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 10

if ejercicio == 10:
    print("Desarrollar una funcion eliminarclaves() que reciba como parametros un diccionario y una lista de claves. La funcion debe eliminar del diccionario todas las claves contenidas en la lista, devolviendo el diccionario modificado y un valor de verdad que indique si la operacion fue exitosa. \nDesarrollar tambien un programa para verificar su comportamiento.")
    print()
    time.sleep(0)   

    def eliminarclaves(_diccionario, _lista_claves):
        try:
            for i in range(len(_lista_claves)):
                _eliminado = _diccionario.pop(lista_claves[i])
        except KeyError:
            return _diccionario, False
        else:
            return _diccionario, True
                
    
    # Programa Principal
    diccionario = {x: x**2 for x in range(1, 21)}
    lista_claves = []
    print(diccionario)

    clave = int(input("Ingresar clave a eliminar (-1 para terminar): "))
    while clave != -1:
        lista_claves.append(clave)
        clave = int(input("Ingresar clave a eliminar (-1 para terminar): "))

    diccionario, operacion_exitosa = eliminarclaves(diccionario, lista_claves)
    print(diccionario)
    if operacion_exitosa:
        print("Claves eliminadas con exito.")
    else:
        print("Error en la Operacion.")

# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 11

if ejercicio == 11:
    print('Crear una funcion contarvocales(), que reciba una palabra y cuentes cuantas letras "a" contiene, cuantas "e", cuantas "i", etc. Devolver un diccionario con los resultados.\nDesarrollar un programa para leer una frase e invocar a la funcion por cada palabra que contenga la misma. \nImprimir cada palabra y la cantidad de vocales hallada.')
    print()
    time.sleep(0)   

    def contarvocales(_palabra):
        _diccionario = {}
        _palabra = _palabra.lower().strip(',').strip('.').strip(';')
        _cantidad_a = _palabra.count('a')
        _cantidad_e = _palabra.count('e')
        _cantidad_i = _palabra.count('i')
        _cantidad_o = _palabra.count('o')
        _cantidad_u = _palabra.count('u')
        _diccionario['a'] = _cantidad_a
        _diccionario['e'] = _cantidad_e
        _diccionario['i'] = _cantidad_i
        _diccionario['o'] = _cantidad_o
        _diccionario['u'] = _cantidad_u
        return _diccionario

    # Programa Principal
    frase = input("Ingresar frase: ")
    palabras = frase.split()
    for palabra in palabras:
        
        diccionario = contarvocales(palabra)
        print(f"{palabra}:", diccionario)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 12

if ejercicio == 12:
    print('Una libreria almacena su lista de precios en un diccionario. \nDiseñar un programa para crearlo, incrementar los precios de los cuadernos en un 15%, imprimir un listado con todos los elementos de la lista de precios e indicar cual es el item mas costoso que venden en el comercio.')
    print()
    time.sleep(0)   

    diccionario = {}
    while True:
        try:
            producto = input("Ingresar nombre del producto (Vacio para terminar): ")
            while producto != "":
                precio = float(input("Ingrese precio del producto: "))
                diccionario[producto] = precio
                producto = input("Ingresar nombre del producto (Vacio para terminar): ")
            else:
                break
        except ValueError:
            print("Datos invalidos")
    
    print(diccionario)
# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 13

if ejercicio == 13:
    print('Escribir una funcion buscarclave() que reciba como parametros un diccionario y un valor, y devuelva una lista de claves que apunten ("mapeen") a ese valor en el diccionario. \nComprobar el comportamiento de la funcion medianto un programa apropiado.')
    print()
    time.sleep(0)   
    
    def buscarclave(_diccionario, _valor_objetivo):
        _lista_claves = []
        _claves = list(_diccionario.keys())
        _valores = list(_diccionario.values())
        for i in range(len(_valores)):
            if _valor_objetivo == _valores[i]:
                _lista_claves.append(_claves[i])
        return _lista_claves
    
    # Programa Principal
    diccionario = {}
    clave = input("Ingresar Clave (Vacio para terminar): ")
    while clave != "":
        valor = input(f"Ingresar Valor de '{clave}': ")
        diccionario[clave] = valor
        clave = input("Ingresar Clave (Vacio para terminar): ")
        
    print(diccionario)
    valor_objetivo = input("Ingresar Valor a buscar: ")
    clave_obtenida = buscarclave(diccionario, valor_objetivo)
    print(f"LISTA DE CLAVES QUE APUNTAN A '{valor_objetivo}':")
    print(clave_obtenida)
    
