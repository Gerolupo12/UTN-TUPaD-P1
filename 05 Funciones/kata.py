# Ejercicio 1: Tabla de multiplicar
def tabla_multiplicar(numero):
    tabla = []
    for i in range(1, 11):
        tabla.append(numero * i)
    return tabla

# Programa Principal
numero = int(input("Ingrese un número entero positivo: "))
print(f"La tabla de multiplicar de {numero} es: {tabla_multiplicar(numero)}")

# Ejercicio 2: Suma de números pares
def suma_pares(lista):
    suma = 0
    for i in lista:
        if i % 2 == 0:
            suma += i
    return suma

# Programa Principal
lista = [1,2,3,4,5,6,7,8,8]
print(suma_pares(lista))

# Ejercicio 3: Área y perímetro de un rectángulo
#       Objetivo: Calcular múltiples valores en una función.
#          Instrucciones:
# 1. Crea una función rectángulo que reciba longitud y anchura.
# 2. Retorna una tupla con el área y el perímetro.
# o Fórmulas:
# ▪ Área = longitud * anchura.
# # ▪ Perímetro = 2 * (longitud + anchura).
def rectangulo(longitud, ancho):
    """Retorna area y perimetro"""
    area = longitud * ancho
    perimetro = 2 * (longitud + ancho)
    return area, perimetro

print(rectangulo(4,2))

# Ejercicio 4: Conversión de temperatura
def convertir_temperatura(temp):
    unidad = input("Ingrese en que tipo de unidad quiere ver la temperatura: ")
    if unidad == 'F':
        f = temp * 9/5 + 32
        return (f"La temperatura en Fahrenheit es: {f}")
    elif unidad == 'K':
        k = temp + 273.15
        return (f"La temperatura en Kelvin es: {k}")

temp = int(input("Ingrese temperatura a convertir: "))
print(convertir_temperatura(temp))

# Ejercicio 5: Verificador de números primos
def es_primo(entero):
    cd = 0
    for i in range(1, entero + 1):
        if entero % i == 0:
            cd += 1
    if cd <= 2:
        return True
    else:
        return False

# Ejercicio 6: Promedio de calificaciones
def promedio_calificaciones(lista):
    suma = 0
    cant = 0
    for i in lista:
        suma += i
        cant += 1
    if not lista:
        return 0
    return suma / cant

lista = [8.5, 9.0, 7.5, 8.0]
print(promedio_calificaciones(lista))

# Ejercicio 7: Factorial con validación
def validar_entrada(numero):
    while numero < 0:
        numero = int(input("Ingrese un numero positivo: "))
    print("El numero ingresado es positivo.")
    return (f"El factorial de dicho numero es: {factorial(numero)}")
    
def factorial(num):
        acu = 1
        for i in range(1, num+1):
            acu *= i
        return acu

print(validar_entrada(int(input("Ingrese un numero: "))))

# Ejercicio 8: Números primos con funciones auxiliares
def es_divisible(num1, num2):
    """Determina si n es divisible por divisor"""
    return num1 % num2 == 0

def es_primo(num):
    """Determina si un número es primo usando la función es_divisible"""
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if es_divisible(num, i):
            return False
    return True

# # Programa Principal
print(es_primo(int(input("Ingrese un numero: "))))

# Ejercicio 9: Conversor de temperatura con menú
def menu_conversion(temp):
    print("""
    Para convertir a Fahrenheit ingrese la F
    Para convertir a Kelvin ingrese la K
    """)
    letra_temp = input("Ingrese la letra correspondiente: ")
    if letra_temp == "F" or "f":
        print("La temperatura es: ", convertir_a_fahrenheit(temp))

def convertir_a_fahrenheit(temp):
        return temp * 9/5 + 32

def convertir_a_kelvin(temp):
    return temp + 273.15

# Programa Principal
temp_celsius = int(input("Ingrese temperatura en celsius: "))
print(menu_conversion(temp_celsius))

# Ejercicio 10: Rectángulo con validación
def validar_dimensiones(longi, anchura):
    while longi < 1:
        longi = int(input("Ingrese la longitud positiva: "))
    while anchura < 1:
        anchura = int(input("Ingrese la anchura positiva: "))
    print(calcular_area(longi, anchura))
    print(calcular_perimetro(longi, anchura))

def calcular_area(largo, anchos):
    area = largo * anchos
    return area

def calcular_perimetro(largo, anchos):
    perimetro = 2 * (largo + anchos)
    return perimetro

# Programa Principal
longitud = int(input("Ingrese la longitud: "))
ancho = int(input("Ingrese el ancho: "))
print(validar_dimensiones(longitud, ancho))