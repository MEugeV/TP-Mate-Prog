""" Este programa sirve para simular compuertas AND, OR, NOT, NAND, NOR Y XOR """

# Definimos las funciones que usaremos para evaluar las funciones booleanas

# Esta función pide al usuario un valor boleano y retorna dicho valor. Valida que sea 0 o 1 y en caso contrario vuelve a a solicitarlo.


def pedir_valor_bool(mensaje):
    while True:
        valor = input(mensaje)
        if valor in ("0", "1"):
            return int(valor)
        else:
            print(
                "Valor incorrecto. Los valores booleanos son 1 o 0. Intente nuevamente: ")

# Esta función pide al usuario seleccionar la compuerta que desea evaluar y retorna dicha selección. Valida que sea un entero del 1 al 6 y en caso contrario vuelve a a solicitarlo.


def pedir_compuerta():
    message = "Elija que función desea analizar: \n 1- Funcion AND\n 2- Funcion OR\n 3- Funcion NOT\n 4- Funcion NAND\n 5- Funcion NOR \n 6- Funcion XOR\n Su eleccion: "
    while True:
        valor = input(message)
        if valor in ("1", "2", "3", "4", "5", "6"):
            return int(valor)
        else:
            print("El valor ingresado no es una función válida. Intente nuevamente: ")


def funcionAnd(x, y):
    if x == 1 and y == 1:
        return True
    else:
        return False


def funcionOr(x, y):
    if x == 1 or y == 1:
        return True
    else:
        return False


def funcionNot(x):
    if x == 1:
        return 0
    if x == 0:
        return 1


# Se pide al usuario ingresar valores binarios

valorA = pedir_valor_bool("Inserte un valor booleano: ")
print(f"El primer valor ingresado es: {valorA}")

valorB = pedir_valor_bool("Inserte otro valor booleano: ")
print(f"El segundo valor ingresado es: {valorB}")


# Creamos un pequeño menu para pedirle al usuario que funcion quiere usar

compuerta = pedir_compuerta()

# Segun lo introducido por el usuario se iniciara alguna de las funciones y se imprimira en pantalla el valor de verdad


# AND
if compuerta == 1:
    print("Funcion AND")
    print(f"Se evalua: {valorA}, {valorB}")
    if funcionAnd(valorA, valorB) == True:
        print("Verdadero")
    else:
        print("Falso")


# OR
elif compuerta == 2:
    print("Funcion OR")
    print(f"Se evalua: {valorA}, {valorB}")
    if funcionOr(valorA, valorB) == True:
        print("Verdadero")
    else:
        print("Falso")


# NOT
elif compuerta == 3:
    print("Funcion NOT")
    print(f"Se evalua: {valorA}, {valorB}")
    if funcionNot(valorA) == 0:
        print(f"{valorA} Falso")
    else:
        print(f"{valorA} Verdadero")
    if funcionNot(valorB) == 0:
        print(f"{valorB} Falso")
    else:
        print(f"{valorB} Verdadero")


# NAND
elif compuerta == 4:
    print("Funcion NAND")
    print(f"Se evalua: {valorA}, {valorB}")
    if funcionAnd(valorA, valorB) == True:
        print("Falso")
    else:
        print("Verdadero")


# NOR
elif compuerta == 5:
    print("Funcion NOR")
    print(f"Se evalua: {valorA}, {valorB}")
    if funcionOr(valorA, valorB) == True:
        print("Falso")
    else:
        print("Verdadero")

# XOR
elif compuerta == 6:
    print("Funcion XOR")
    print(f"Se evalua: {valorA}, {valorB}")
    if valorA != valorB:
        print("Verdadero")
    else:
        print("Falso")


else:
    print("El numero ingresado no es una opcion valida")
