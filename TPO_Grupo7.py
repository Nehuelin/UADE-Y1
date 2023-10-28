import random
from colorama import Fore, Back, Style, init
import time

def generar_numeros(): # <-- Podriamos aplicar recursividad aca?
    _numeros = set()
    while len(_numeros) <= 6:
        _numeros.add(random.randint(0, 41))
    return list(_numeros)

# def generar_numeros(unicos, cantidad):
#     if cantidad == 0:
#         return list(unicos)  # Cuando se alcanza la cantidad deseada, convertimos el conjunto en una lista y lo devolvemos.
#     else:
#         nuevo_numero = random.randint(0, 41)
#         while nuevo_numero in unicos:  # Asegurarse de que el número generado sea único.
#             nuevo_numero = random.randint(0, 41)
#         unicos.add(nuevo_numero)
#         return generar_numeros(unicos, cantidad - 1)

def generar_archivo(): # <-- La cantidad de registros afecta la velocidad de ejecucion (Cuantos mas registros tenga que hacer, mas va a tardar)
    registros = random.randint(10000, 50000)
    
    dni_apostadores = set()
    while len(dni_apostadores) <= registros:
        dni_apostadores.add(random.randint(1000000, 99999999))
    dni_apostadores = list(dni_apostadores)

    try:
        archivo = open("apuestas.txt", "wt")
        for i in range(registros):
            agencia = random.randint(100,105)
            numeros = generar_numeros()
            linea = str(dni_apostadores[i]) + ';' + str(agencia) + ";" +  str(numeros[0]) + ";" +  str(numeros[1]) + ";" +  str(numeros[2]) + ";" +  str(numeros[3]) + ";" +  str(numeros[4]) + ";" +  str(numeros[5]) + "\n"
            archivo.write(linea)
    except FileNotFoundError as mensaje:
        print(f"Error: {mensaje}")
    except OSError as mensaje:
        print(f"Error: {mensaje}")
    finally:      
        try:
            archivo.close()
        except NameError:
            pass 
    return

init(autoreset = True) # <-- Resetea los efectos de texto por linea (Asi no tenemos que usar Style.RESET_ALL todo el tiempo)
generar_archivo()
ganadores = {}
listado_agencias = {}
# racha_maxima = 0
# seis_aciertos = {}
# cinco_aciertos = {}
# cuatro_aciertos = {}
# tres_aciertos = {}
# dos_aciertos = {}
# un_aciertos = {}

numeros_ganadores = set()
while len(numeros_ganadores) < 6:
    numeros_ganadores.add(random.randint(0, 41))

try:
    archivo = open("apuestas.txt", "rt")
    for linea in archivo:
        aciertos = 0
        # racha_actual = 0
        linea = linea.rstrip("\n")
        linea = linea.split(';')
        numeros = linea[2:]
    
        for i in range(len(numeros)):
            if int(numeros[i]) in numeros_ganadores:
                aciertos += 1
                # racha_actual += 1
        if aciertos >= 5:
            ganadores[linea[0]] = linea[1]
        # if aciertos == 6:
        #        seis_aciertos[linea[0]] = linea[1]     
        # elif aciertos == 5:
        #        cinco_aciertos[linea[0]] = linea[1]     
        # elif aciertos == 4:
        #        cuatro_aciertos[linea[0]] = linea[1]     
        # elif aciertos == 3:
        #        tres_aciertos[linea[0]] = linea[1]     
        # elif aciertos == 2:
        #        dos_aciertos[linea[0]] = linea[1]     
        # elif aciertos == 1:
        #        un_aciertos[linea[0]] = linea[1]    
        # if racha_actual > racha_maxima:
        #     racha_maxima = racha_actual 
        if linea[1] not in listado_agencias:
            listado_agencias[linea[1]] = 1
        elif linea[1] in listado_agencias:
            listado_agencias[linea[1]] += 1  # <-- Esto funciona, pero no se va a notar al menos que el rango del random de los codigos sea entre pocos numeros
except FileNotFoundError as mensaje:
    print(f"Error: {mensaje}")
except OSError as mensaje:
    print(f"Error: {mensaje}")
finally:
    try:
        archivo.close()
    except NameError:
        pass

print("Numeros sorteados: " + Back.RED + f"{str(numeros_ganadores).strip('{}').replace(',',' -')}")

print(Style.BRIGHT + Fore.GREEN + "\nGANADORES (4 o mas acertados): ")
ganadores_ordenados = sorted(ganadores.keys())
for dni in ganadores_ordenados:
    agencia = ganadores[dni]
    print(Back.MAGENTA + f"DNI: {dni:2} ", f"CODIGO DE AGENCIA: {agencia}")
    
print(Fore.LIGHTBLUE_EX + Style.BRIGHT + "\nAGENCIAS PARTICIPANTES: ")
listado_agencias_ordenado = sorted(listado_agencias.keys(), key = lambda codigo: listado_agencias[codigo], reverse=True)
for codigo in listado_agencias_ordenado:
    cantidad = listado_agencias[codigo]
    print(f"CODIGO Nro: {codigo}, CANTIDAD DE APOSTADORES: {cantidad}")

# TESTING ONLY: 
dev_total_lines = list(listado_agencias.values())
print(f"\nDEV ONLY! Cantidad de registros: {sum(dev_total_lines)}")

# OBSERVACIONES:
# La cantidad de registros a generar afectan la velocidad de ejecucion
# El diccionario listado_agencias funciona, pero no se va a notar al menos que el rango de agencias generadas sea entre pocos numeros
# UN APOSTADOR PUEDE PARTICIPAR CON VARIAS AGENCIAS!!!!

# SUGERENCIAS
# Podriamos aplicar recursividad en alguna funcion u operacion basica
# Podriamos usar matriz en alguno de los dos listados
