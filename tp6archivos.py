import random 
import time

ejercicio = int(input("Que ejercicio queres probar? (NOW TESTING: ): "))
# 1 y 3

# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 1

if ejercicio == 1:
    print("Desarrollar un programa para eliminar todos los comentarios de un programa escrito en lenguaje Python. \nTener en cuenta que los comentarios comienzan con el signo # (siempre que este no se encuentre encerrado entre comillas simples o dobles) y que tambien se considera comentario a las cadenas de documentacion (docstrings).")
    print()
    time.sleep(0)

    try:
        entrada = open("datos.txt", "rt")
        salida = open("nuevo.txt", "wt")
        dentro_de_comentario = False  # Para rastrear si estamos dentro de un comentariog

        for linea in entrada:
            linea_sin_comentarios = ""
            i = 0
            longitud_linea = len(linea)
            while i < longitud_linea:
                if (not dentro_de_comentario and linea[i] == '#') or (not dentro_de_comentario and linea[i:i+3] == '"""'):
                    # Si encontramos un '#' y no estamos dentro de un comentario o docstring, ignoramos el resto de la línea
                    break
                elif linea[i] == '"':
                    # Si encontramos una comilla doble
                    linea_sin_comentarios += linea[i]
                    i += 1
                elif not dentro_de_comentario and linea[i] == "'":
                    # Si encontramos una comilla simple, avanzamos hasta la siguiente comilla simple
                    linea_sin_comentarios += linea[i]
                    i += 1
                    while i < longitud_linea and linea[i] != "'":
                        linea_sin_comentarios += linea[i]
                        i += 1
                    if i < longitud_linea:
                        linea_sin_comentarios += linea[i]
                        i += 1
                else:
                    # Copiamos el carácter normalmente
                    linea_sin_comentarios += linea[i]
                    i += 1
            
            renglon = linea_sin_comentarios.rfind('\n')
            if len(linea_sin_comentarios) > 0 and renglon == -1:
                linea_sin_comentarios += '\n'
                
            salida.write(linea_sin_comentarios)

        print(f'Comentarios y docstrings eliminados correctamente. Revisar archivo "nuevo.txt"')
    except FileNotFoundError as mensaje:
        print("No se pudo abrir el archivo:", mensaje)
        
        
    finally:
        try: 
            entrada.close()
            salida.close()
        except NameError:
            pass

# vvvvv COPIAR EN BLOCK DE NOTAS vvvvv      
# def calcular_area_triangulo(base, altura):
#     """ Esta función calcula el área de un triángulo dado su base y altura. """
#     area = (base * altura) / 2
#     return area

# # Solicitar al usuario la entrada de base y altura
# base = float(input("Ingrese la longitud de la base del triángulo: ")) # Solicitar al usuario la entrada de base y altura 
# altura = float(input("Ingrese la altura del triángulo: "))

# # Calcular el área del triángulo usando la función
# area_del_triangulo = calcular_area_triangulo(base, altura)

# # Mostrar el resultado
# print(f"El área del triángulo con base {base} y altura {altura} es: {area_del_triangulo}. ' # test' ")

# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 2

if ejercicio == 2:
    print("Escribir un programa que permita grabar en un archivo los datos de lluvia caida durante un año. Cada linea del archivo se grabara con el siguiente formato: \n<dia>;<mes>;<lluvia caida en mm> por ejemplo 25;5;319.")
    print("Los datos se generaran mediante numeros al azar, asegurandose que las fechas sean validas. La cantidad de registros tambien sera un numero al azar entre 50 y 200. \nPor ultimo se solicita leer el archivo generado e imprimir un informe en formato matricial donde cada columna representa a un mes y cada fila corresponda a los dias del mes.\nImprimir ademas el total de lluvia caida en todo el año.")
    print()
    time.sleep(16)
    
        #YEARS >= 1582, BISIESTO SI ES DIVISIBLE POR 4. PARA LOS años QUE SON DIVISIBLES POR 4 y 100, SI NO SON DIVISIBLES POR 400, NO SON BISIESTOS
        #MONTHS/DAYS: FEB --> 28d, 29d (BISIESTO); JAN, MAR, MAY, JUL, AUG, OCT, DEC --> 31d; FEB, APR, JUN, SEP, NOV --> 30d
    
    bisiesto = False
    try:
        arch = open("registrolluvia.txt", "wt")
        año = random.randint(1582, 2023)
        if (año % 4 == 0 and año % 100 != 0) or año % 400 == 0:
            bisiesto = True
        else: 
            bisiesto = False 
        print(f"Año: {año}")
        lineas = random.randint(50,250)
        for i in range(lineas):
            mes = random.randint(1,12)
            if mes == 2:
                if bisiesto == True:        
                    dia = random.randint(1,29)
                else:
                    dia = random.randint(1,28)
            elif mes in [4, 6, 9, 11]:
                dia = random.randint(1,30)
            else:
                dia = random.randint(1,31) 
            lluvia = random.randint(0,600)
            arch.write(str(dia)+";"+str(mes)+";"+str(lluvia)+'\n')
    except FileNotFoundError as mensaje:
        print("ERROR: El archivo no se pudo abrir:", mensaje)
    except OSError as mensaje:
        print("ERROR:", mensaje)
    finally:
        try:
            arch.close()
        except NameError:
            pass
        print("Archivo cerrado")
    
    try:
        arch = open("registrolluvia.txt", "rt")
        matriz = [[0] * 12 for i in range(31)] # 12 Meses, 31 Dias x Mes
        anual = 0
        for linea in arch:
            linea = linea.rstrip('\n')
            dia, mes, lluvia = linea.split(";")
            anual += int(lluvia)
            matriz[int(dia)-1][int(mes)-1] += int(lluvia)
        
        for fila in matriz:
            for elemento in fila:
                print(f"{elemento:^5}", end="")
            print()    
        
        print(f"Cantidad de lluvia caida en el año: {anual}mm")
        
    except FileNotFoundError as mensaje:
        print("ERROR: El archivo no se pudo abrir:", mensaje)
    except OSError as mensaje:
        print("ERROR:", mensaje)
    finally:
        try:
            arch.close()
        except NameError:
            pass
        print("Archivo cerrado")        

    
# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 3

if ejercicio == 3:
    print("Una institucion deportiva necesita clasificar a sus atletas para inscribirlos en los proximos Juegos Paramericanos. Para eso encargó la realización de un programa que incluya las siguientes funciones: ")
    print("\033[1m--> GrabarRangoAlturas()\033[0m: Graba en un archivo las alturas de los atletas de distintas disciplinas, los que se ingresan desde el teclado. Cada dato se debe grabar en una linea distinta.")
    print("\033[1m--> GrabarPromedio()\033[0m: Graba en un archivo los promedios de las alturas de los atletas presentes en el archivo generado en el paso anterior. La disciplina y el promedio deben grabarse en lineas diferentes.")
    print("\033[1m--> MostrarMasAltos()\033[0m: Muestra por pantalla las disciplinas deportivas cuyos atletas superan la estatura promedio general. Obtener los datos del segundo archivo.")
    print()
    time.sleep(0)

    def grabarrangoalturas():
        try:
            arch1 = open("alturas.txt", "wt")
            deporte = input("Ingresar Disciplina (Enter para terminar): ")
            while deporte != "":
                assert deporte.isalpha(), "Nombre invalido"
                arch1.write(deporte + "\n")
                altura = float(input("Ingresar altura del atleta (-1 para terminar): "))
                while altura != -1:
                    arch1.write(str(altura) + "\n")
                    altura = float(input("Ingresar altura del atleta (-1 para terminar): "))
                deporte = input("Ingresar Disciplina (Enter para terminar): ")
            else:
                arch1.write("...")
        except FileNotFoundError as mensaje:
            print(mensaje)
        except OSError as mensaje:
            print(mensaje)
        except AssertionError as mensaje:
            print(mensaje)
        finally:
            try:
                arch1.close()
            except NameError:
                pass
                    
    def grabarpromedio():
        skip = True
        suma = 0
        cantidad = 0        
        try:
            arch1 = open("alturas.txt", "rt")
            arch2 = open("promedio.txt", "wt")
            for linea in arch1:
                linea = linea.rstrip("\n")
                if skip == True:
                    arch2.write(linea + '\n')
                    skip = False  
                elif linea.isalpha() or linea == "...":
                    promedio = suma / cantidad
                    arch2.write(f"{promedio}" + '\n')
                    if linea != "...":
                        arch2.write(linea + "\n")
                    suma = 0
                    cantidad = 0
                else:
                    suma += float(linea)
                    cantidad += 1
                    
        except FileNotFoundError as mensaje:
            print(mensaje)
        except OSError as mensaje:
            print(mensaje)
        finally:
            try:
                arch1.close()
                arch2.close()
            except NameError:
                pass    
    
    def mostrarmasaltos():
        suma = 0
        cantidad = 0
        try:
            arch2 = open("promedio.txt", "rt")
            for linea in arch2:
                linea = linea.rstrip('\n')
                if not linea.isalpha():
                    suma += float(linea)
                    cantidad += 1
            promedio = suma / cantidad
            print(f"El promedio general es de {promedio}m")
            arch2.seek(0)
            for linea in arch2:
                linea = linea.rstrip('\n')
                if linea.isalpha():
                    deporte = linea
                else:
                    if float(linea) > promedio:
                        print(f"La disciplina {deporte} supera el promedio general.")
                                                
        except FileNotFoundError as mensaje:
            print(mensaje)
        except OSError as mensaje:
            print(mensaje)
        finally:
            try:
                arch2.close()
            except NameError:
                pass            
    
    # Programa Principal
    grabarrangoalturas()
    grabarpromedio()    
    mostrarmasaltos()
# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 4

if ejercicio == 4:
    print('Escribir un programa que lea un archivo de texto conteniendo un conjunto de apellidos y nombres en formato "Apellido, Nombre" y guarde en el archivo ARMENIA.TXT los nombres de aquellas personas cuyo apellido terminan con la cadena "IAN", en el archivo ITALIA.TXT los terminados en "INI" y en el archivo ESPAÑA.TXT los terminados en "EZ". Descartar el resto.')
    print("El archivo de entrada puede ser creado mediante el Block de Notas o el IDLE. NO escribir un programa para generarlo.")
    print()
    time.sleep(0)
    
    try:
        arch = open("datos.txt","rt")
        armenia = open("ARMENIA.TXT", "wt")
        italia = open("ITALIA.TXT", "wt")
        españa = open("ESPAÑA.TXT", "wt")
        for linea in arch:
            apellido, nombre = linea.split(", ")
            if apellido[-3:] == "ian":
                armenia.write(nombre)
            elif apellido[-3:] == "ini":
                italia.write(nombre)
            elif apellido[-2:] == "ez":
                españa.write(nombre)
    except FileNotFoundError as mensaje:
        print("Error: No se pudo abrir el archivo:", mensaje)
    except OSError as mensaje:
        print("No se puede cerrar el archivo:",mensaje)
    finally:
        try:
            arch.close()
            armenia.close()
            italia.close()
            españa.close()
        except NameError:
            pass
        print("Archivo cerrado")

# vvvvv COPIAR EN BLOCK DE NOTAS vvvvv
# Rodriguez, Juan
# Lopez, Maria
# Nortini, Carlos
# Perez, Sofia
# Martinez, Alejandro
# Hernandez, Isabella
# Silvian, Diego
# Torres, Ana
# Ramirez, Lucas
# Castro, Gabriela

# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 4

if ejercicio == 5:
    print("Se dispone de tres formatos diferentes de archivos de texto en los que se almacenan datos de empleados. Los formatos se indican en la Guia de Trabajos Practicos. \nDesarrollar un programa para cada uno de los formatos suministrados, que permitan leer cada uno de los archivos y grabar los datos en otro archivo de texto con formato CSV.")
    print()
    time.sleep(0)
    
    try:
        arch = open("datos.txt", "rt")
        nuevo = open("CSV.txt", "wt")
        for linea in arch:
            #CASO 1: LONGITUDES FIJAS
            # nombre = linea[:15]
            # numero = linea[15:23]
            # direccion = linea[23:]
            # nuevo.write(nombre.strip(" ") + ";" + numero.strip(" ") + ";" + direccion.strip(" ") + '\n')
            
            #CASO 2: SEPARACION CON #
            # nombre, numero, direccion = linea.split("#")
            # nuevo.write(nombre + ';' + numero + ';' + direccion + '\n')
            
            #CASO 3: INDICADOR DE LONGITUD
            cant = int(linea[:2])
            nombre = linea[2:2+cant]
            cant2 = int(linea[2+cant:4+cant])
            numero = linea[4+cant:4+cant+cant2]
            cant3 = int(linea[4+cant+cant2:6+cant+cant2])
            direccion = linea[6+cant+cant2:8+cant+cant2+cant3]
            nuevo.write(nombre + ';' + numero + ';' + direccion + '\n')
    except FileNotFoundError as mensaje:
        print("ERROR:",mensaje)
    except OSError as mensaje:
        print("ERROR:",mensaje) 
    finally:
        try:
            arch.close()
            nuevo.close()
        except NameError:
            pass
        print("Archivo Cerrado")

# vvvvv COPIAR EN BLOCK DE NOTAS vvvvv
# Perez Juan     20080211 Corrientes348
# Gonzales Ana M 20080115 Juan de Garay 1111 3er piso dto A

# vvvvv COPIAR EN BLOCK DE NOTAS vvvvv
# Perez Juan#20080211#Corrientes 348
# Gonzales Ana M#20080115#Juan de Garay 1111 3er piso dto A

# vvvvv COPIAR EN BLOCK DE NOTAS vvvvv
# 10Perez Juan082008021114Corrientes 348
# 14Gonzales Ana M082008011533Juan de Garay 1111 3er piso dto A
