import random 
import time

ejercicio = int(input("Que ejercicio queres probar? (EJERCICIOS DISPONIBLES: 1 a 9): "))

# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 1

if ejercicio == 1:
    print("\nDesarrollar una funcion que reciba tres numeros positivos y devuelva el mayor de los tres, solo si este es unico (mayor estricto). \nEn caso de no existir el mayor estricto devolver -1. \nNo utilizar operadores logicos (and, or, not). \nDesarrollar tambien un programa para ingresar los tres valores, invocar a la funcion y mostrar el maximo hallado, o un mensaje informative si este no existe.")
    print()
    time.sleep(4)
    
    # NO USAR and, not, or
    
    def cualesmayor(x,y,z):
        mayor = x
        if x < y:
            mayor = y
            if y < z:
                mayor = z
            elif y == z:
                mayor = -1
        elif x < z:
            mayor = z
        elif x == y:
            mayor = -1
        elif x == z:
            mayor = -1    
        return mayor
        
    # MAIN
    
    a = int(input("Ingresar primer numero positivo: "))
    while a < 1:
        print("ERROR, numero ingresado no es positivo")
        a = int(input("Ingresar primer numero positivo: "))
    
    b = int(input("Ingresar segundo numero positivo: "))
    while b < 1:
        print("ERROR, numero ingresado no es positivo")
        b = int(input("Ingresar segundo numero positivo: "))
    
    c = int(input("Ingresar tercer numero positivo: "))
    while c < 1:
        print("ERROR, numero ingresado no es positivo")
        c = int(input("Ingresar tercer numero positivo: "))
        
    numeromayor = cualesmayor(a,b,c)

    if numeromayor == -1:
        print("-1")
    else:
        print("El numero mayor es:", numeromayor)
    
# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 2

if ejercicio == 2:
    print("\nDesarrollar una funcion que reciba tres numeros enteros positivos y verifique si corresponden a una fecha valida (dia, mes, ano). \nDevolver True o False segun la fecha sea correcta o no. \nRealizar tambien un programa para verificar el comportamiento de la funcion.")
    print()
    time.sleep(4)
    
    #YEARS >= 1582, BISIESTO SI ES DIVISIBLE POR 4. PARA LOS años QUE SON DIVISIBLES POR 4 y 100, SI NO SON DIVISIBLES POR 400, NO SON BISIESTOS
    #MONTHS/DAYS: FEB --> 28d, 29d (BISIESTO); JAN, MAR, MAY, JUL, AUG, OCT, DEC --> 31d; FEB, APR, JUN, SEP, NOV --> 30d
 
    
    def esfechavalida(x,y,z):
        
        if z < 1582:
            return False
        else:
            if z % 4 == 0:
                if z % 100 != 0:
                    bisiesto = True
                else: 
                    if z % 400 != 0:
                        bisiesto = False
                    else: 
                        bisiesto = True   
            else:
                bisiesto = False
        
        if y > 12:
            return False
        else:
            if y == 2:
                if bisiesto:
                    if x > 29:
                        return False
                    else:
                        return True 
                else:
                    if x > 28:
                        return False
                    else:
                        return True 
            elif y == 1 or y == 3 or y == 5 or y == 7 or y == 8 or y == 10 or y == 12:
                if x > 31:
                    return False
                else:
                    return True
            else:
                if x > 30:
                    return False
                else:
                    return True 
                
                                               
    
    # MAIN
    
    a = int(input("Ingresar primer numero positivo: "))
    while a < 1:
        print("ERROR, numero ingresado no es positivo")
        a = int(input("Ingresar primer numero positivo: "))
    
    b = int(input("Ingresar segundo numero positivo: "))
    while b < 1:
        print("ERROR, numero ingresado no es positivo")
        b = int(input("Ingresar segundo numero positivo: "))
    
    c = int(input("Ingresar tercer numero positivo: "))
    while c < 1:
        print("ERROR, numero ingresado no es positivo")
        c = int(input("Ingresar tercer numero positivo: "))    
    
    fechaverificada = esfechavalida(a,b,c)
    
    if fechaverificada:
        print("La fecha es Valida")
    else:
        print("La fecha es Invalida")

# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 3

if ejercicio == 3:
    print("\nUna persona desea llevar el control de los gastos realizados al viajar en el subterraneo dentro de un mes. \nSabiendo que dicho medio de transporte utiliza un esquema de tarifas decrecientes (detalladas en la tabla de abajo) se solicita desarrollar una funcion que reciba como parametro la cantidad de viajes realizados en un determinado mes y devuelva el total gastado en viajes. \nRealizar tambien un programa para verificar el comportamiento de la funcion.")
    print()
    time.sleep(4)
    
    def averiguargastos(x):
        valor = 500
        if x > 20 and x <= 30:
            valor = valor * 0.80 
        elif x > 30 and x <= 40:
            valor = valor * 0.70
        elif x > 40:
            valor = valor * 0.60
            
        valorfinal = x * valor
        
        return valorfinal    
            
    # MAIN
    viajes = int(input("Ingresar cantidad de viajes realizados en el ultimo mes: "))
    while viajes < 0:
        print("ERROR: numero invalido")
        viajes = int(input("Ingresar cantidad de viajes realizados en el ultimo mes: "))
    
    if viajes == 0:
        print("Usted no realizo ningun viaje este mes")
    else:
        gastofinal = averiguargastos(viajes)
    
        print("Gasto Final:")
        print(gastofinal,"$", sep="")

# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 4

if ejercicio == 4:
    print("\nUn comercio de electrodomesticos necesita para su linea de cajas un programa que le indique al cajero el cambio que debe entregarle al cliente. \nPara eso se ingresan dos numeros enteros, correspondientes al total de la compra y al dinero recibido. \nInformar cuantos billetes de cada denominacion deben ser entregados al cliente como vuelto, de tal forma que se minimice la cantidad de billetes. \nConsiderar que existen billetes de $500, $100, $50, $20, $10, $5 y $1.\nEmitir un mensaje de error si el dinero recibido fuera insuficiente. \nEjemplo: Si la compra es de $317 y se abona con $500, el vuelto debe contener 1 billete de $100, 1 billete de $50, 1 billete de $20, 1 billete de $10 y 3 billetes de $1.")
    print()
    time.sleep(4)
    
    
    totalcompra = int(input("Ingresar monto total de compra: "))
    dinerorecibido = int(input("Ingresar dinero recibido: "))
    
    if dinerorecibido < totalcompra:
        print("El dinero recibido es insuficiente para completar la compra")
    else:
        vuelto = totalcompra - dinerorecibido
        vuelto = -vuelto
        print("El vuelto deberia ser de",vuelto,"$")
    
    vueltoinicial = vuelto
         
    billetequinientos = 0
    billetecien = 0
    billetecincuenta = 0
    billeteveinte = 0
    billetediez = 0
    billetecinco = 0
    billeteuno = 0


    while vuelto > 0:
        if vuelto >= 500:
            billetequinientos = vuelto // 500
            vuelto = vuelto % 500
        elif vuelto < 500 and vuelto >= 100:
            billetecien = vuelto // 100
            vuelto = vuelto % 100
        elif vuelto < 100 and vuelto >= 50:
            billetecincuenta = vuelto // 50
            vuelto = vuelto % 50
        elif vuelto < 50 and vuelto >= 20:
            billeteveinte = vuelto // 20
            vuelto = vuelto % 20
        elif vuelto < 20 and vuelto >= 10:
            billetediez = vuelto // 10
            vuelto = vuelto % 10
        elif vuelto < 10 and vuelto >= 5:
            billetecinco = vuelto // 5
            vuelto = vuelto % 5
        elif vuelto < 5 and vuelto >= 1:
            billeteuno = vuelto // 1
            vuelto = vuelto % 1
            
    print("Le debe",billetequinientos,"billetes de $500,",billetecien,"billetes de $100,",billetecincuenta,"billetes de $50,", billeteveinte,"billetes de $20,", billetediez,"billetes de $10,",billetecinco,"billetes de $5 y",billeteuno,"billetes de $1.")
        
# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 5

if ejercicio == 5:
    print("\nEscribir dos funciones separadas para imprimir por pantalla los siguientes patrones de asteriscos, donde la cantidad de filas se recibe como parametro: ")
    print("*********                  **")
    print("*********                  ****")
    print("*********                  ******")
    print("*********                  ********")
    print("*********                  **********")
    print()
    time.sleep(4)
    
    def constante(numero):
        for i in range (numero):
            print("*********")
    
    def acumulativo(numero):
        asteriscos = "**"
        for i in range(numero):
            print(asteriscos)
            asteriscos += "**"
    
    #MAIN
    n = int(input("Ingresar cantidad de filas: "))
    
    constante(n)   
    print()
    acumulativo(n)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 6

if ejercicio == 6:
    print("\nDesarrollar una funcion que reciba como parametros dos numeros enteros positivos y devuelva el numero que resulte de concatenar ambos valores. \nPor ejemplo, si recibe 1234 y 567 debe devolver 1234567.")
    print()
    time.sleep(4)
    
    def unirnumeros(numerouno, numerodos):
        contador = 0
        copia = numerodos
        while copia > 0:
            copia = copia // 10
            contador = contador + 1
        ceros = 10 * (10 ** contador)
        ceros = ceros // 10
        union = numerouno * ceros + numerodos
        return union
    
    #MAIN
    primernumero = int(input("Ingresar primer numero entero: "))
    segundonumero = int(input("Ingresar segundo numero entero: "))
    
    numerofinal = unirnumeros(primernumero,segundonumero)
    
    print(numerofinal)
    
# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 7

if ejercicio == 7:
    print("\nEscribir una funcion diasiguiente(...) que reciba como parametro una fecha cualquiera expresada por tres enteros (correspondiente al dia, mes y año) y calcule y devuelva tres enteros correspondientes al dia siguiente al dado.")
    print("Utilizando esta funcion, desarrollar programas que permitan: \na) Sumar N dias a una fecha \nb) Calcular la cantidad de dias existentes entre dos fechas cualquiera")
    print()
    time.sleep(0)    

    def diasiguiente(di, me, añ, nums):
        while nums > 0:
            di += + 1
            if me == 1 or me == 3 or me == 5 or me == 7 or me == 8 or me == 10 or me == 12:
                dias = 31
                if di > dias:
                    di = 1
                    me += 1
                    if me > 12:
                        añ += 1
                        me = 1
                nums -= 1
            elif me == 4 or me == 6 or me == 9 or me == 11:
                dias = 30
                if di > dias:
                    di = 1
                    me += 1
                    if me > 12:
                        añ += 1
                        me = 1
                nums -= 1
            elif me == 2 and añ % 4 == 0 and (añ % 100 != 0 or añ % 400 == 0):
                dias = 29
                if di > dias:
                    di = 1
                    me += 1
                    if me > 12:
                        añ += 1
                        me = 1
                nums -= 1
            elif me == 2:
                dias = 28
                if di > dias:
                    di = 1
                    me += 1
                    if me > 12:
                        añ += 1
                        me = 1
                nums -= 1
        return di, me, añ
            
        
    def verificarfecha(d, m, a):
        dv = False
        mv = False
        if a >= 0:
            if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
                if 0 < d <= 31:
                    return True 
            elif m == 4 or m == 6 or m == 9 or m == 11:
                if 0 < d <= 30:
                    return True 
            elif m == 2 and a % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
                if 0 < d <= 29:
                    return True
            elif m == 2:
                if 0 < d <= 28:
                    return True
        return False 
        
    def sepmeses(d1, m1, a1, d2, m2, a2):
        sep = 0
        while d1:
            d1 += 1
            sep += 1
            if m1 == 4 or m1 == 6 or m1 == 9 or m1 == 11:
                dias = 30
                if d1 > dias:
                    d1 = 1
                    m1 += 1
                    if m1 > 12:
                        a1 += 1
                        m1 = 1
            elif m1 == 2 and a1 % 4 == 0 and (a1 % 100 != 0 or a1 % 400 == 0):
                dias = 29
                if d1 > dias:
                    d1 = 1
                    m1 += 1
                    if m1 > 12:
                        a1 += 1
                        m1 = 1
            elif m1 == 2:
                dias = 28
                if d1 > dias:
                    d1 = 1
                    m1 += 1
                    if m1 > 12:
                        a1 += 1
                        m1 = 1
            else:
                dias = 31
                if d1 > dias:
                    d1 = 1
                    m1 += 1
                    if m1 > 12:
                        a1 += 1
                        m1 = 1
            if d1 == d2 and m1 == m2 and a1 == a2:
                break
        return sep

    # Programa Principal
    dia = int(input("Ingrese un dia: "))
    mes = int(input("Ingrese un mes: "))
    año = int(input("Ingrese un año: "))

    val = verificarfecha(dia, mes, año)
    while val == False:
        dia = int(input("Ingrese un nuevo dia: "))
        mes = int(input("Ingrese un nuevo mes: "))
        año = int(input("Ingrese un nuevo año: "))
        
        val = verificarfecha(dia, mes, año)

    cual = int(input("Ingrese 1 para sumar dias, ingrese 2 para ver separacion entre fechas: "))

    if cual == 1:    
        n = int(input("Ingrese cuantos dias desea sumar: "))
        
        dsig, msig, asig = diasiguiente(dia, mes, año, n)
        
        print("Sumando ", n," dias a la fecha ingresada resultaria en la fecha", dsig,"/", msig,"/", asig, sep=" ")
    else:
        dia2 = int(input("Ingrese el segundo dia: "))
        mes2 = int(input("Ingrese el segundo mes: "))
        año2 = int(input("Ingrese el segundo año: "))
        
        val = verificarfecha(dia2, mes2, año2)
        while val == False:
            dia2 = int(input("Ingrese un nuevo dia: "))
            mes2 = int(input("Ingrese un nuevo mes: "))
            año2 = int(input("Ingrese un nuevo año: "))
            val = verificarfecha(dia, mes, año)
            
        msep = sepmeses(dia, mes, año, dia2, mes2, año2)
        print("La separacion entre las dos fechas es de", msep, "dias")

# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 8

if ejercicio == 8:
    print("\nLa siguiente funcion permite averiguar el dia de la semana para una fecha determinada. \nLa fecha se suministra en forma de tres parametros enteros y la funcion devuleve 0 para domingo, 1 para lunes, 2 para martes, etc. ")
    print("Escribir un programa para imprimir por pantalla el calendario de un mes completo, correspondiente a un mes un y año cualquiera basandose en la funcion suministrada.\nConsiderar que la semana empieza en domingo")
    print()
    time.sleep(0)          
    
    def diadelasemana(dia,mes,año):
        if mes < 3:
            mes = mes + 10
            año = año - 1
        else: 
            mes = mes - 2
        siglo = año // 100
        año2 = año % 100
        diasem = (((26 * mes - 2) // 10) + dia + año2 + (año2 // 4) + (siglo // 4) - (2 * siglo)) % 7
        if diasem < 0:
            diasem = diasem + 7
        return diasem

    # MAIN

    y = int(input("Ingresar mes: "))
    z = int(input("Ingresar año: "))
    x = 1
    
    limite = 0
    
    invalido = False
    if z < 1582:
        invalido = True
    else:
        if z % 4 == 0:
            if z % 100 != 0:
                bisiesto = True
            else: 
                if z % 400 != 0:
                    bisiesto = False
                else: 
                    bisiesto = True   
        else:
            bisiesto = False
    if y > 12:
        invalido = True
    else:
        if y == 2:
            if bisiesto:
                if x > 29:
                    invalido = True
                else: 
                    limite = 29
            else:
                if x > 28:
                    invalido = True
                else:
                    limite = 28
        elif y == 1 or y == 3 or y == 5 or y == 7 or y == 8 or y == 10 or y == 12:
            if x > 31:
                invalido = True
            else:
                limite = 31
        else:
            if x > 30:
                invalido = True
            else:
                limite = 30 
    
    if invalido:
        print("Fecha Invalida")
    else:
        print("Dom", "Lun", "Mar", "Mie", "Jue", "Vie", "Sab")
        day = diadelasemana(x,y,z)
        
        for i in range(day):
            print("   ", end=" ")        
        
        while x <= limite:
            print("%3d" %x, end=" ")
            x += 1
            day += 1
            if day == 7:
                print()
                day = 0
            
    
    
    
# ---------------------------------------------------------------------------------------------------------------------------------------------------------- 
#EJERCICIO 9
# ñ
if ejercicio == 9:
    print("\nResover el siguiente problema diseñando y utilizando funciones: ")
    print("Un productor frutihorticola desea contabilizar sus cajones de naranjas segun el peso para poder cargar el camion de reparto. \nLa empresa cuenta con N camiones, y cada uno puede transportar hasta media tonelada (500kg).")
    print("En un cajon caben 100 naranjas con un peso entre 200 y 300 gramos cada una. \nSi el peso de alguna naranja se encuentra fuera del rango indicado, se clasifica para procesar como jugo.")
    print("Se solicia desarrollar un programa para ingresar la cantidad de naranjas cosechadas e informar cuantos cajones se pueden llenar, cuantas naranjas son para jugo y si hay algun sobrante de naranjas que deba considerarse para el siguiente reparto.")
    print("Simular el peso de cada unidad generando un numero al azar entre 150 y 300. \nAdemas, se desea saber cuantos camiones se necesitan para transportar la cosecha. considerando que la ocupacion del camion no debe ser inferior al 80%; en caso contrario el camion no sera despachado por su alto costo.")
    print()
    time.sleep(0)            
    
    def contarcajones(naranjas):
        contador = 0
        jugo = 0
        pesototal = 0
        for i in range(naranjas):    
            naranja = random.randint(150, 350)
            if naranja >= 200 and naranja <= 300:
                contador += 1
                pesototal += naranja
            else: 
                jugo += 1
        cajon = contador // 100
        resto = contador % 100
        return cajon, jugo, resto, pesototal
    

    
    cantidadnaranjas = int(input("Ingresar cantidad de naranjas: "))
    
    cajones, procesadas, restantes, peso = contarcajones(cantidadnaranjas)
    
    print("Cantidad de cajones:", cajones, "\nCantidad de naranjas procesadas para jugo:",procesadas, "\nCantidad de naranjas restantes:", restantes, "\nPeso total en cajones:", peso)
    
    n = 0
    while peso > 400000:
            if peso >= 500000:
                n = n + peso // 500000
                peso = peso % 500000
            else:  
                n = n + peso // 400000
                peso = peso % 400000
                
    
    print("Cantidad de camiones:",n)
        