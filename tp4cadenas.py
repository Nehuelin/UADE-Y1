import random 
import time
ejercicio = int(input("Que ejercicio queres probar? (NOW TESTING: 13): "))

# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 1

if ejercicio == 1:
    print("Desarrollar una funcion que determine si una cadena de caracteres es capicua, sin utilizar cadenas auxiliares ni rebanadas. \nEscribir ademas un programa que permita verificar su funcionamiento.")
    print()
    time.sleep(4)
    
    def es_capicua(cadena):
        cadena = cadena.replace(" ", "")
        longitud = len(cadena)
        for i in range(longitud // 2):
            if cadena[i] != cadena[longitud - 1 - i]:
                return False
        return True
    
    #PROGRAMA PRINCIPAL
    cad = input("Ingresar cadena de caracteres: ")
    palindromo = es_capicua(cad)
    if palindromo:
        print("Es palindromo")
    else:
        print("No es palindromo")

# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 2

if ejercicio == 2:
    print("Leer una cadena de caracteres e imprimirla centrada en pantalla. Suponer que la misma tiene 80 columnas.")
    print()
    time.sleep(4)

    def centrar_en_pantalla(cadena):
        ancho_pantalla = 80
        espacios = (ancho_pantalla - len(cadena)) // 2
        cadena_centralizada = ' ' * espacios + cadena
        print(cadena_centralizada)

    cad = input("Ingrese una cadena: ")
    centrar_en_pantalla(cad)
    

# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 3

if ejercicio == 3:
    print('Los numeros de claves de dos cajas fuertes estan intercalados dentro de un numero entero llamado "Clave Maestra", cuya longitud no se conoce. \nRealizar un programa para obtener ambas claves, donde la primera se construye con los digitos ubicados en las posiciones impares de la clave maestra y la segunda con los \ndigitos ubicados en posiciones pares. \nLos digitos se numeran desde la izquierda. Ejemplo: si la clave maestra fuera 18293, la clave 1 seria 123 y la clave 2 seria 89')
    print()
    time.sleep(4)

    def obtener_claves(clavetotal):
        claveimpar = clavetotal[1::2]  # Dígitos en posiciones impares
        clavepar = clavetotal[::2]   # Dígitos en posiciones pares
        return claveimpar, clavepar

    clave_maestra = str(random.randint(1,9))
    for i in range(random.randint(0,9)):
        clave_maestra += str(random.randint(0,9))
        
    print("Clave Maestra:",clave_maestra)

    clave1, clave2 = obtener_claves(clave_maestra)

    print("Clave 1:",clave1)
    print("Clave 2:",clave2)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 4

if ejercicio == 4:
    print("Escribir una funcion que reciba como parametro un numero entero entre 0 y 3999 y lo convierta en un numero romano, devolviendolo en una cadena de caracteres.")
    print()
    time.sleep(4)

    def int_a_romano(numero):
        valores = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        simbolos = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']  # Esto sirve para numeros grandes. Si se reduce el rango, se eliminan las letras mas grandes
        resultado = ''

        i = 0
        while numero > 0:
            while numero >= valores[i]:
                resultado += simbolos[i]
                numero -= valores[i]
            i += 1
        return resultado
    
    #PROGRAMA PRINCIPAL
    numero_entero = int(input("Ingrese un número entre 0 y 3999: "))
    if 0 <= numero_entero <= 3999:
        numero_romano = int_a_romano(numero_entero)
        print("El número romano correspondiente es:", numero_romano)
    else:
        print("El número ingresado está fuera del rango válido.")
        
# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 5

if ejercicio == 5:
    print("Escribir una funcion filtrar_palabras() que reciba una cadena de caracteres conteniendo una frase y un entero N, y devuelva otra cadena con las palabras que tengan N o mas \ncaracteres de la cadena original. Escribir tambien un programa para verificar el comportamiento de la misma. \nHacer tres versiones de la funcion, para cada uno de los siguientes casos: ")
    print("a- Utilizando solo ciclos normales.")
    print("b- Utilizando listas por comprension.")
    print("c- Utilizando la funcion filter.")
    print()
    time.sleep(4)
    
    def filtrar_palabras1(cadena, numero):
        lista = cadena.split()
        nueva = []
        for i in range(len(lista)):
            if len(lista[i]) >= numero:
                nueva.append(lista[i])
        nueva = " / ".join(nueva)
        return nueva
    
    def filtrar_palabras2(cadena, numero):
        lista = cadena.split()
        nueva = [lista[i] for i in range(len(lista)) if len(lista[i]) >= numero]
        nueva = " / ".join(nueva)
        return nueva       

    def filtrar_palabras3(cadena, numero):
        lista = cadena.split()
        nueva = " / ".join(filter(lambda palabra: len(palabra) >= numero, lista)) #palabra es cada elemento de la lista: si palabra es mayor o igual que numero, se agrega a nueva.
        return nueva  

    #PROGRAMA PRINCIPAL
    cad = "Tener confianza en uno mismo, o fingir que la tienes, es necesario para aprovechar las oportunidades. Es un cliché, pero las oportunidades rara vez vienen servidas en bandeja, tienes que ir por ellas."
    print(cad)
    n = int(input("Ingresar numero: "))
    reducido = filtrar_palabras1(cad, n)
    print(reducido)
    reducido = filtrar_palabras2(cad, n)
    print(reducido)
    reducido = filtrar_palabras3(cad, n)
    print(reducido)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 6

if ejercicio == 6:
    print('Desarrollar una funcion que extraiga una subcadena de una cadena de caracteres, indicando la posicion y la cantidad de caracteres deseada. \nDevolver la subcadena como valor de retorno. Escribir tambien un programa para verificar el comportamiento de la misma. ')
    print('Ejemplo, dada la cadena "El numero de telefono es 4356-7890" extraer la subcadena que comienza en la posicion 25 y tiene 9 caracteres, resultando la subcadena "4356-7890".')
    print("Escribir una funcion para cada uno de los siguientes casos: ")
    print("a- Utilizando rebanadas")
    print("b- Sin utilizar rebanadas")
    print()
    time.sleep(4)
    
    def extraer_subcadena1(cadena, pos, cant):
        sub = cadena[pos : pos + cant]
        return sub
    
    def extraer_subcadena2(cadena, pos, cant):
        sub = ""
        for i in range(pos, pos + cant):
            if i < len(cadena):
                sub += cadena[i]
        return sub
    
    #PROGRAMA PRINCIPAL
    cad = "El sol brillaba en el cielo azul mientras las hojas caían lentamente de los árboles en otoño."
    print(cad)
    posicion = int(input("Ingresar posicion de inicio (base 0): "))
    cantidad = int(input("Ingresar cantidad de caracteres deseados: "))
    subcadena = extraer_subcadena1(cad, posicion, cantidad)
    print(subcadena)
    subcadena = extraer_subcadena2(cad, posicion, cantidad)
    print(subcadena)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 7

if ejercicio == 7:
    print("Escribir una funcion para eliminar una subcadena de una cadena de caracteres, a partir de una posicion y la cantidad de caracteres dadas, devolviendo la cadena resultante. Escribir tambien un programa para verificar el comportamiento de la misma. \nEscribir una funcion para cada uno de los siguientes casos: ")
    print("a- Utilizando rebanadas")
    print("b- Sin utilizar rebanadas")
    print()
    time.sleep(4)
    
    def eliminar_subcadena1(cadena, pos, cant):
        inicio = cadena[:pos]
        fin = cadena[pos + cant:]
        resultado = inicio + fin
        return resultado

    def eliminar_subcadena2(cadena, pos, cant):
        resultado = ""
        for i in range(len(cadena)):
            if i < pos or i >= pos + cant:
                resultado += cadena[i]
        return resultado
    
    #PROGRAMA PRINCIPAL
    cad = "La música es el lenguaje del alma y puede expresar lo que las palabras a veces no pueden"
    print(cad)
    posicion = int(input("Ingresar posicion de inicio: "))
    cantidad = int(input("Ingresar cantidad de caracteres deseados: "))
    subcadena = eliminar_subcadena1(cad, posicion, cantidad)
    print(subcadena)
    subcadena = eliminar_subcadena2(cad, posicion, cantidad)
    print(subcadena)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 8

if ejercicio == 8:
    print("Escribir una fucnion que reciba como parametro una cadena de caracteres en la que las palabras se encuentran separadas por un o mas espacios. \nDevolver otra cadena con las palabras ordenadas alfabeticamente, dejando un espacio entre cada una.")
    print()
    time.sleep(4)
    
    def ordenar_cadena_espaciada(cadena):
        lista = cadena.split(" ")
        lista.sort()
        resultado = " ".join(lista)
        return resultado
    
    #PROGRAMA PRINCIPAL
    cad = "la aventura está en cada rincón del mundo, solo tienes que buscarla"
    print(cad)
    ordenada = ordenar_cadena_espaciada(cad)
    print(ordenada)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 9

if ejercicio == 9:
    print("Desarrollar una funcion que devuelva una subcadena con los ultimos N caracteres de una cadena dada. La cadena y el valor de N se pasan como parametros.")
    print()
    time.sleep(4)
    
    def ultimos_caracteres(cadena, numero):
        sub = cadena[len(cadena)-numero:]
        return sub
    
    #PROGRAMA PRINCIPAL
    cad = '"El conocimiento es el tesoro más valioso, y la sabiduría es la llave que lo desbloquea"'
    print(cad)
    n = int(input("Ingresar la ultima cantidad de caracteres deseadas: "))
    subcadena = ultimos_caracteres(cad, n)
    print(subcadena)
    
# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 10

if ejercicio == 10:
    print("Desarrollar una funcion para reemplazar todas las apariciones de una palabra por otra en una cadena de caracteres y devolver la cadena obtenida y un entero con la cantidad de \nreemplazos realizados. \nTener en cuenta que solo deben reemplazarse palabras completas, y no fragmentos de palabras. \nEscribir tambien un programa para verificar el comportamiento de la funcion.")
    print()
    time.sleep(4)    
    
    def reemplazar(cadena):
        palabra = 'la'
        reemplazo = 'oso' 
        cantidad = 0 # Crear las variables parametro. Dividimos la cadena e investigamos con bucle para encontrar las palabras a reemplazar.
        lista = cadena.split() 
        for i in range(len(lista)):
            if lista[i] == palabra:
                lista[i] = reemplazo #Si la palabra de la cadena coincide con el parametro, la cambiamos por la nueva, y sumamos 1 al contador
                cantidad += 1
        nueva = ' '.join(lista) # Finalizamos y volvemos a unir la cadena
        return nueva, cantidad
    
    #PROGRAMA PRINCIPAL
    cad1 = '''La complejidad del universo se manifiesta en la interconexión de innumerables fenómenos y la intrincada danza de partículas elementales que conforman la materia, 
mientras que la mente humana, dotada de la capacidad de indagar en los misterios de la naturaleza, 
continúa explorando los límites del conocimiento y la comprensión en su eterna búsqueda de respuestas y significado'''
    print(cad1)
    
    cad2, n = reemplazar(cad1)
    print(cad2)
    print(f"\nSe reemplazaron {n} palabras")
    
# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 11

if ejercicio == 11:
    print("Escribir un programa que cuente cuantas veces se encuentra una subcadena dentro de otra cadena, sin diferenciar mayusculas y minusculas. \nTener en cuenta que los caracteres de la subcadena no necesariamente deben estar en forma consecutiva dentro de la cadena, pero si respetando el orden de los mismos.")
    print()
    time.sleep(4) 
    
    def encontrar_subcadena(cadena, subcadena):
        cadena = cadena.lower()
        subcadena = subcadena.lower()   # Uso .lower() para no diferenciar Mayus y Minus
        contador = 0
        inicio = 0
        while inicio < len(cadena):
            posicion = cadena.find(subcadena[0], inicio) #BUCLE: 
            if posicion == -1:
                break
            encontrado = True
            for i in range(1, len(subcadena)):
                siguiente_caracter = cadena.find(subcadena[i], posicion + 1)
                if siguiente_caracter == -1:
                    encontrado = False
                    break
                posicion = siguiente_caracter
            if encontrado:
                contador += 1
            inicio = posicion + 1
        return contador
                
    #PROGRAMA PRINCIPAL
    cad1 = "El viaje hacia el conocimiento es un camino lleno de desafíos y descubrimientos que nos enriquecen y nos ayudan a crecer como seres humanos"
    print(cad1)
    sub = input("Ingresar subcadena a encontrar: ")
    cant = encontrar_subcadena(cad1, sub)    
    print(f"La subcadena '{sub}' se encontro {cant} veces")
    
# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 12

if ejercicio == 12:
    print("")
    print()
    time.sleep(0)    
    
    tipos = ["Oros", "Espadas", "Bastos", "Copas"]
    lista = []
    j = 0
    while j < 4:
        lista += [str(i) + " " + tipos[j] for i in range(1, 13)]
        j += 1
    print(lista)        
    
# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 13

if ejercicio == 13:
    print("Muchas aplicaciones financieras requieren que los numeros sean expresados tambien en letras. \nPor ejemplo, el numero 2153 puede escribirse como 'dos mil ciento cincuenta y tres'. ")
    print("Escribir un programa que utilice una funcion para convertir un numero entero entre 0 y 1.000.000.000.000 (un billon) a letras.")
    print()
    time.sleep(0)    

    def convertir_a_letras(numero):
        pass    
        
        
    
    #PROGRAMA PRINCIPAL
    n = int(input("Ingresar numero: "))
    expresion = convertir_a_letras(str(n))
    
# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 14

if ejercicio == 14:
    print("")
    print()
    time.sleep(0)  
      
    
    
    
    
    
    
    
    
##   
