lista = []

#Crear lista, ingresar cantidad de elementos Y elementos
cant = int(input("Ingresar cantidad de elementos: "))
for i in range(cant): #Bucle que continuara hasta que se cumpla la cantidad asignada
    elemento = input("Ingresar elemento: ")
    lista.append(elemento)

#Imprimir lista, corroborar que no este vacia
if len(lista) > 0:
    print(lista)
else:
    print("La lista esta vacia")

#Insertar un elemento al principio de la fila
elemento = input("Ingresar elemento: ")
lista.insert(0, elemento) #.insert() inserta un elemento en la lista. Primer valor en el parentesis es la posicion (base0), segundo valor es el elemento a agregar
print(lista)

#Insertar un elemento al final de la fila
elemento = input("Ingresar elemento: ")
lista.insert(len(lista), elemento) #Aca uso len(lista) para que se agregue al final
print(lista)

#Insertar un elemento despues de uno indicado por el usuario
referencia = input("Ingresar elemento de referencia: ")
if referencia in lista: #Si el elemento esta en la lista...
    indice = lista.index(referencia) #Uso .index() para guardar la posicion del elemento
    elemento = input("Ingresar elemento: ")
    lista.insert(indice + 1, elemento) 
print(lista)

#Insertar un elemento antes de uno indicado por el usuario
referencia = input("Ingresar elemento de referencia: ")
if referencia in lista:
    indice = lista.index(referencia)
    elemento = input("Ingresar elemento: ")
    lista.insert(indice, elemento)
print(lista)

#Insertar un elemento en una posicion especifica
posicion = int(input("Ingresar posicion (base 0): "))
elemento = input("Ingresar elemento: ")
lista.insert(posicion, elemento)
print(lista)

#Contar los elementos de una lista
total = len(lista) #Con usar len(lista), es decir la longitud, ya se conocen la cantidad de elementos
print("Hay",total,"elementos en la lista")

#Buscar un elemento de la lista
referencia = input("Ingresar elemento a buscar: ")
if referencia in lista:
    print(referencia,"esta en la lista")

#Eliminar un elemento desde el principio de la lista
lista.pop(len(lista)-len(lista)) #Queda igual a 0, es decir la primera posicion. .pop() elimina un elemento de la lista, en base a su posicion
print(lista)

#Eliminar un elemento del final de la lista
lista.pop(len(lista) - 1) #Como funciona en base0, hay que restar 1
print(lista)

#Eliminar un elemento segun el valor ingresado
referencia = input("Ingresar elemento a buscar: ")
if referencia in lista:
    lista.remove(referencia) #.remove funciona igual que pop, pero en vez de usar una posicion, se pone el elemento a eliminar
print(lista)
