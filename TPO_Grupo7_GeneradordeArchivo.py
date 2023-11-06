import random
import time

def generar_numeros():
    _numeros = set()
    while len(_numeros) <= 6:
        _numeros.add(random.randint(0, 41))
    return list(_numeros)

# Programa Principal
inicio = time.time()  
registros = random.randint(10000, 50000)

dni_apostadores = set()
while len(dni_apostadores) <= registros:
    dni_apostadores.add(random.randint(1000000, 99999999))
dni_apostadores = list(dni_apostadores)

try:
    archivo = open("apuestas.txt", "wt")
    for i in range(registros):
        agencia = random.randint(49900,49999)
        numeros = generar_numeros()
        linea = str(dni_apostadores[i]) + ';' + str(agencia) + ";" +  str(numeros[0]) + ";" +  str(numeros[1]) + ";" +  str(numeros[2]) + ";" +  str(numeros[3]) + ";" +  str(numeros[4]) + ";" +  str(numeros[5]) + "\n"
        archivo.write(linea)
except FileNotFoundError as mensaje:
    print(f"Error: {mensaje}")
except OSError as mensaje:
    print(f"Error: {mensaje}")
finally:
    fin = time.time()
    print(f"TIEMPO DE EJECUCION: {fin-inicio:.2f}s")   
    try:
        archivo.close()
    except NameError:
        pass
