def imprimir_biblioteca(_biblioteca):
    _titulos = sorted(list(_biblioteca.keys()), key = lambda _titulos: _titulos)
    for i in range(len(_titulos)):
        print(f"\nTítulo: {_titulos[i]}")
        print(f"Autor: {_biblioteca[_titulos[i]][0]}")
        print(f"Género: {_biblioteca[_titulos[i]][1]}")
        print(f"Cantidad disponible: {_biblioteca[_titulos[i]][2]}")


#PROGRAMA PRINCIPAL
biblioteca = {}
prestados = {}

try:
    archivo = open("biblioteca.txt", "rt", encoding='UTF8')
    for linea in archivo:
        linea = linea.rstrip('\n').split(';')
        biblioteca[linea[0]] = (linea[1:])
except FileNotFoundError as mensaje:
    print(mensaje)
except OSError as mensaje:
    print(mensaje)
finally:
    try:
        archivo.close()
    except NameError:
        pass

print("\nBienvenido!")
ejecutar = input("\nIngrese cualquier valor para comenzar ")
while True:
    print('''\nMENU DE OPCIONES:
          1. Mostrar catalogo de libros
          2. Buscar Libro
          3. Prestar Libro
          4. Devolver Libro
          5. Salir''')
    try:
        menu = int(input("Ingrese una Opcion: "))
    except ValueError:
        print("ERROR: Valor invalido")
        continue
    
    if menu == 1:
        print("\nCATALOGO: ")
        imprimir_biblioteca(biblioteca)
        
    elif menu == 2:
        print("\nBUSCAR LIBRO")
        titulo = input("Ingresar titulo del libro: ")
        try:
            libro = biblioteca[titulo]
            print("DATOS:")
            print(f"Autor: {biblioteca[titulo][0]}")
            print(f"Género: {biblioteca[titulo][1]}")
            print(f"Cantidad disponible: {biblioteca[titulo][2]}")
        except KeyError:
            print("ERROR: No se encontro resultados")
            
    elif menu == 3:
        print("\nPRESTAR LIBRO")
        titulo = input("Ingresar titulo del libro a prestar: ")
        try:
            cantidad = int(biblioteca[titulo][2])
            if cantidad == 0:
                print("ERROR: No hay stock para prestar el libro")
            else: 
                biblioteca[titulo][2] = cantidad - 1
                if titulo in prestados:
                    prestados[titulo] += 1
                else:
                    prestados[titulo] = 1
        except KeyError:
            print("ERROR: No se encontro resultados")
            
    elif menu == 4:
        print("\nDEVOLVER LIBRO")
        titulo = input("Ingresar titulo del libro a devolver: ")
        try:
            cantidad = int(prestados[titulo])
            if cantidad == 0:
                print("ERROR: No se registraron ejemplares prestados de este libro")
            else:
                prestados[titulo] -= 1
                biblioteca[titulo][2] += 1
        except KeyError:
            print("ERROR: No se encontro resultados")
            
    elif menu == 5:
        final = " FINALIZANDO PROGRAMA "
        final = final.center(100, '-')
        print(f"\n{final}\n")
        break


# print('''    Gestión de la biblioteca:
#         Crear un diccionario llamado biblioteca para almacenar la información de los libros. Cada clave del diccionario será el título del libro, y el valor asociado será otro diccionario con la información del libro (autor, género, cantidad disponible).
#         Inicialmente, la biblioteca tendrá al menos 5 libros.

#     Menú de opciones:
#         Implementar un bucle que presente un menú de opciones al usuario:
#             1. Mostrar todos los libros: Mostrar la información de todos los libros en la biblioteca.
#             2. Buscar un libro: Permitir al usuario buscar un libro por título y mostrar su información.
#             3. Prestar un libro: Permitir al usuario prestar un libro. Actualizar la cantidad disponible del libro prestado.
#             4. Devolver un libro: Permitir al usuario devolver un libro. Actualizar la cantidad disponible del libro devuelto.
#             5. Salir: Salir del programa.

#     Validación de entrada:
#         Implementar validaciones para asegurarse de que el usuario ingrese opciones válidas en el menú (números del 1 al 5) y que los títulos ingresados en las búsquedas, préstamos y devoluciones existan en la biblioteca.

#     Mostrar información ordenada:
#         Cuando se muestre la información de los libros, asegurarse de que esté ordenada alfabéticamente por título.

#     Manejo de préstamos y devoluciones:
#         Al prestar un libro, verificar que haya ejemplares disponibles antes de realizar el préstamo. No permitir préstamos si no hay ejemplares disponibles.
#         Al devolver un libro, verificar que el libro haya sido prestado previamente y actualizar la cantidad disponible.

#     Guardar información al salir:
#         Implementar una opción para guardar la información de la biblioteca en un archivo al salir del programa. Esto permitirá que la información persista entre ejecuciones del programa.''')
