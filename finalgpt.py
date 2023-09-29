stock = {}

# Variables para calcular el resultado del ejercicio para el año 2009
total_ventas_2009 = 0
total_compras_2009 = 0

# Abre el archivo de texto
try:
    archivo = open("testeo.txt", "rt")
    for linea in archivo:
        partes = linea.split()

        # Comprueba si la línea tiene el formato correcto (longitud mínima)
        if len(partes) >= 6:
            dia = partes[0]
            mes = partes[1]
            anio = partes[2]
            cantidad = int(partes[-2])
            precio = float(partes[-1])

            # Identifica si es una compra o una venta
            if "Compra" in linea:
                producto = " ".join(partes[3:-2])  # Nombre del producto
                total_compras_2009 += cantidad * precio

                if producto in stock:
                    stock[producto] += cantidad
                else:
                    stock[producto] = cantidad
            elif "Venta" in linea:
                producto = " ".join(partes[3:-2])  # Nombre del producto
                total_ventas_2009 += cantidad * precio

                if producto in stock:
                    stock[producto] -= cantidad
except (FileNotFoundError, OSError):
    print("LMAO")

# Ordena el stock en orden descendente por cantidad
stock_ordenado = sorted(stock.items(), key=lambda x: x[1], reverse=True)

# Imprime el listado ordenado
print("Listado de stock por producto:")
for producto, cantidad in stock_ordenado:
    print(f"{producto}: {cantidad}")

# Calcula el resultado del ejercicio para el año 2009
resultado_ejercicio_2009 = total_ventas_2009 - total_compras_2009
print("\nResultado del ejercicio para el año 2009:")
print(f"Total de ventas 2009: {total_ventas_2009}")
print(f"Total de compras 2009: {total_compras_2009}")
print(f"Resultado para el año 2009: {resultado_ejercicio_2009}")


# COPIAR EN EL ARCHIVO DE TEXTO PARA PROBAR --> 
# Compra de mercaderías 01 02 2009 RESMA PAPEL OBRA 70G 50 101.15
# Venta de mercaderías 12 03 2009 RESMA PAPEL OBRA 70G 20 110.00
# Compra de mercaderías 05 04 2009 LAPICERO NEGRO 100 2.50
# Venta de mercaderías 10 05 2009 RESMA PAPEL OBRA 70G 10 105.00
# Compra de mercaderías 15 06 2009 TIJERA ESCOLAR PLAST 150 1.99
# Venta de mercaderías 20 07 2009 LAPICERO NEGRO 50 2.50
