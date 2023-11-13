import random
from colorama import Back, Style, init

def generar_numeros_ganadores(numeros_ganadores, cantidad):
    if len(numeros_ganadores) == cantidad:
        return numeros_ganadores
    nuevo_numero = random.randint(0, 41)
    if nuevo_numero not in numeros_ganadores:
        numeros_ganadores.add(nuevo_numero)
    return generar_numeros_ganadores(numeros_ganadores, cantidad)

def imprimir_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print("%14s" %elemento, end=" ")
        print()

def imprimir_resultados(titulo, datos):
    print('\n' + titulo)
    imprimir_matriz(datos)

# PROGRAMA PRINCIPAL 
init(autoreset = True)
numeros_ganadores = generar_numeros_ganadores(set(), 6)
    
apostadores_ganadores = []
lista_apostadores = []
maximo = 0
listado_agencias = {}

try:
    archivo = open("apuestas.txt", "rt")
    for linea in archivo:
        aciertos = 0
        linea = linea.rstrip('\n').split(';')
        numeros = linea[2:]
        
        for i in range (len(numeros)):
            if int(numeros[i]) in numeros_ganadores:
                aciertos += 1
        
        dni, codigo_agencia = linea[:2]
        apostador = (dni, codigo_agencia, aciertos)
        if aciertos > 0:
            lista_apostadores.append(apostador)

        if codigo_agencia in listado_agencias:
            listado_agencias[codigo_agencia] += 1
        else:
            listado_agencias[codigo_agencia] = 1

        if aciertos > maximo:
            maximo = aciertos
            
except FileNotFoundError as mensaje:
    print("ERROR:", mensaje)
except OSError as mensaje:
    print("ERROR:", mensaje)
except ValueError:
    print("ERROR: Archivo Vacio / Formato Invalido")
finally:
    try:
        archivo.close()
    except NameError:
        pass
        
print('\n' + Back.GREEN + "NUMEROS GANADORES:" + Style.RESET_ALL, str(numeros_ganadores).strip('{}').replace(',',' -'))
print('\n' + Back.YELLOW + "CANTIDAD MAXIMA DE ACIERTOS:" + Style.RESET_ALL, maximo)

for i in range(len(lista_apostadores)):
    if lista_apostadores[i][2] == maximo:
        apostadores_ganadores.append(lista_apostadores[i])
apostadores_ganadores = sorted(apostadores_ganadores, key = lambda x: (int(x[0]), int(x[1])))
matriz = [list(apostador[:2]) for apostador in apostadores_ganadores]
imprimir_resultados(Back.RED + " DNI DE GANADORES | CODIGO DE AGENCIA ", matriz)

agencias = sorted(listado_agencias.keys(), key = lambda x: listado_agencias[x], reverse=True)
matriz_agencias = [[codigo, listado_agencias[codigo]] for codigo in agencias]
imprimir_resultados(Back.LIGHTBLUE_EX + "AGENCIAS PARTICIPANTES | CANTIDAD DE APOSTADORES", matriz_agencias)
