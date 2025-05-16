
#  Ejercicio 1: Tabla de multiplicar 
#       Objetivo: Generar una tabla de multiplicar usando funciones. 
#          Instrucciones: 
# 1. Crea una función tabla_multiplicar que reciba un número entero positivo. 
# 2. Devuelve una lista con su tabla de multiplicar del 1 al 10. 
# o Ejemplo: Para 3 → [3, 6, 9, ..., 30]. 
# def tabla_multiplicar(numero):
#     tabla = []
#     for i in range(1, 11):
#         tabla.append(numero * i)
#     return tabla
# # Programa Principal
# numero = int(input("Ingrese un número entero positivo: "))
# print(f"La tabla de multiplicar de {numero} es: {tabla_multiplicar(numero)}")

#    Ejercicio 2: Suma de números pares 
#       Objetivo: Sumar elementos pares de una lista con una función. 
#          Instrucciones: 
# 1. Define una función suma_pares que reciba una lista de enteros. 
# 2. Retorna la suma de los números pares. 
# o Ejemplo: Para [1, 2, 3, 4, 5, 6] → 12. 
# def suma_pares(lista):
#     suma = 0
#     for i in lista:
#         if i % 2 == 0:
#             suma += i
#     return suma

# lista = [1,2,3,4,5,6,7,8,8]
# print(suma_pares(lista))


#     Ejercicio 3: Área y perímetro de un rectángulo 
#       Objetivo: Calcular múltiples valores en una función. 
#          Instrucciones: 
# 1. Crea una función rectángulo que reciba longitud y anchura. 
# 2. Retorna una tupla con el área y el perímetro. 
# o Fórmulas: 
# ▪ Área = longitud * anchura. 
# # ▪ Perímetro = 2 * (longitud + anchura). 
# def rectangulo(longitud, ancho):
#     """Retorna area y perimetro"""
#     area = longitud * ancho
#     perimetro = 2 * (longitud + ancho)
#     return print(f"El area es {area} y la longitud es {perimetro}")

# print(rectangulo(4,2))

#      Ejercicio 4: Conversión de temperatura 
#       Objetivo: Convertir temperaturas con condiciones. 
#          Instrucciones: 
# 1. Define una función convertir_temperatura que reciba: 
# o Temperatura en Celsius. 
# o Unidad de destino ("F" o "K"). 
# 2. Retorna la temperatura convertida usando: 
# o Fahrenheit: F = C * 9/5 + 32. 
# o Kelvin: K = C + 273.15. 
# def convertir_temperatura(temp):
#     unidad = input("Ingrese en que tipo de unidad quiere ver la temperatura: ")
#     if unidad == 'F':
#         f = temp * 9/5 + 32
#         return (f"La temperatura en Fahrenheit es: {f}")
#     elif unidad == 'K':
#         k = temp + 273.15
#         return (f"La temperatura en Kelvin es: {k}")

# print(convertir_temperatura(24))

#     Ejercicio 5: Verificador de números primos 
#       Objetivo: Implementar una función para detectar primos. 
#          Instrucciones: 
# 1. Crea una función es_primo que reciba un entero positivo. 
# 2. Retorna True si es primo (solo divisible por 1 y sí mismo), False en caso 
# contrario. 
# o Ejemplo: 7 → True, 8 → False. 
# def es_primo(entero):
#     cd = 0 
#     for i in range(1, entero + 1):
#         if entero % i == 0:
#             cd += 1
#     if cd <= 2:
#         return True
#     else:
#         return False

#        Ejercicio 6: Promedio de calificaciones 
#       Objetivo: Calcular promedios con funciones. 
#          Instrucciones: 
# 1. Define una función promedio_calificaciones que reciba una lista de notas 
# (0 a 10). 
# 2. Retorna el promedio. Si la lista está vacía, retorna 0. 
# o Ejemplo: [8.5, 9.0, 7.5, 8.0] → 8.25. 
#     suma = 0
#     cant = 0
#     for i in lista:
#         suma += i
#         cant += 1
#     return suma/cant


#     Ejercicio 7: Factorial con validación 
#       Objetivo: Combinar funciones para validar y calcular. 
#          Instrucciones: 
# 1. Usa dos funciones: 
# o validar_entrada: Verifica si un número es entero no negativo. 
# o factorial: Calcula el factorial (ej: 5! = 120). 
# 2. El programa principal debe: 
# o Pedir un número al usuario. 
# o Validarlo y mostrar el factorial o un error. 
# def validar_entrada(numero):
#     while numero < 0:
#         numero = int(input("Ingrese un numero positivo: "))
#     print("El numero ingresado es positivo.")
#     return (f"El factorial de dicho numero es: {factorial(numero)}")
    
# def factorial(num):
#         acu = 1 
#         for i in range(1, num+1):
#             acu *= i
#         return acu

# print(validar_entrada(int(input("Ingrese un numero: "))))
# Ejercicio 8: Números primos con funciones auxiliares
# Objetivo: Modularizar la lógica de primos.
# Instrucciones:
# 1. Usa dos funciones: 
# es_divisible: Retorna True si un número divide a otro.
# es_primo: Usa es_divisible para verificar si es primo.
# 2. El programa principal pide un número y muestra si es primo. 
# def es_divisible(num1, num2):
#     """Determina si n es divisible por divisor"""
#     return num1 % num2 == 0
#
# def es_primo(num):
#     """Determina si un número es primo usando la función es_divisible"""
#     if num <= 1:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if es_divisible(num, i):
#             return False
#     return True
#
# # Programa Principal
# print(es_primo(int(input("Ingrese un numero: "))))

# Ejercicio 9: Conversor de temperatura con menú
# Objetivo: Integrar funciones con interacción de usuario.
# Instrucciones:
# 1. Usa tres funciones: 
# o convertir_a_fahrenheit: Convierte Celsius a Fahrenheit. 
# o convertir_a_kelvin: Convierte Celsius a Kelvin. 
# o menu_conversion: Muestra un menú para elegir la unidad. 
# 2. El programa principal: 
# o Pide la temperatura en Celsius. 
# o Muestra el resultado según la unidad elegida.
# Fahrenheit: F = C * 9/5 + 32.
# o Kelvin: K = C + 273.15.
# def menu_conversion(temp):
#     print("""
#     Para convertir a Fahrenheit ingrese la F
#     Para convertir a Kelvin ingrese la K
#     """)
#     letra_temp = input("Ingrese la letra correspondiente: ")
#     if letra_temp == "F" or "f":
#         print("La temperatura es: ", convertir_a_fahrenheit(temp))
#
#
# def convertir_a_fahrenheit(temp):
#         return temp * 9/5 + 32
#
# def convertir_a_kelvin(temp):
#     return temp + 273.15
#
# # Programa Principal
# temp_celsius = int(input("Ingrese temperatura en celsius: "))
# print(menu_conversion(temp_celsius))

# Ejercicio 10: Rectángulo con validación 
# Objetivo: Validar entradas antes de calcular. 
# Instrucciones: 
# 1. Usa tres funciones: 
# o validar_dimensiones: Verifica que longitud y anchura sean positivas. 
# o calcular_area: Retorna el área del rectángulo. 
# o calcular_perimetro: Retorna el perímetro. 
# 2. El programa principal: 
# o Pide las dimensiones al usuario. 
# o Valida y muestra resultados o un error. 
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