import random
from colorama import Fore, Back, Style, init
import time

# USAR FUNCION RECURSIVA PARA GENERAR NUMEROS GANADORES 
# def generar_numeros(unicos, cantidad):
#     if cantidad == 0:
#         return list(unicos)  # Cuando se alcanza la cantidad deseada, convertimos el conjunto en una lista y lo devolvemos.
#     else:
#         nuevo_numero = random.randint(0, 6)
#         while nuevo_numero in unicos:  # Asegurarse de que el número generado sea único.
#             nuevo_numero = random.randint(0, 6)
#         unicos.add(nuevo_numero)
#         return generar_numeros(unicos, cantidad - 1)

init(autoreset = True) # <-- Resetea los efectos de texto por linea (Asi no tenemos que usar Style.RESET_ALL todo el tiempo)
ganadores = []
listado_agencias = {}
racha_maxima = 0
ganadores_finales = []

numeros_ganadores = set()
while len(numeros_ganadores) < 6:
    numeros_ganadores.add(random.randint(0, 41))

try:
    archivo = open("apuestas.txt", "rt")
    for linea in archivo:
        racha_actual = 0
        aciertos = 0
        linea = linea.rstrip("\n")
        linea = linea.split(';')
        numeros = linea[2:]
        for i in range(len(numeros)):
            if int(numeros[i]) in numeros_ganadores:
                aciertos += 1
                racha_actual += 1
        if aciertos >= 1:
            datos = linea[0], linea[1], aciertos
            ganadores.append(datos)   
        if racha_actual > racha_maxima:
            racha_maxima = racha_actual 
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

print(f"RACHA MAXIMA: {racha_maxima}")

print(Style.BRIGHT + Fore.GREEN + "\nGANADORES: ")
for i in range(len(ganadores)):
    if ganadores[i][2] == racha_maxima:
        ganadores_finales.append(ganadores[i])  # FUNCIONA ENCONTRAR GANADORES DE X VICTORIAS
print(ganadores_finales) # <--- Para verificar que funciona
ganadores_ordenados = sorted(ganadores_finales, key = lambda x: (int(x[0]), int(x[1]))) # FUNCIONA ORDENAMIENTO (AMBAS CLAVES)
for i in range(len(ganadores_ordenados)):
    print(Back.MAGENTA + f"DNI: {ganadores_ordenados[i][0]:2} ", f"CODIGO DE AGENCIA: {ganadores_ordenados[i][1]}")
    
print(Fore.LIGHTBLUE_EX + Style.BRIGHT + "\nAGENCIAS PARTICIPANTES: ")
listado_agencias_ordenado = sorted(listado_agencias.keys(), key = lambda codigo: listado_agencias[codigo], reverse=True)
for codigo in listado_agencias_ordenado:
    cantidad = listado_agencias[codigo]
    print(f"CODIGO Nro: {codigo}, CANTIDAD DE APOSTADORES: {cantidad}")

# TESTING ONLY: 
dev_total_lines = list(listado_agencias.values())
print(f"\nDEV ONLY! Cantidad de registros: {sum(dev_total_lines)}")
