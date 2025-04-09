import math

# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.

def imprimir_hola_mundo():
    print("Hola Mundo!") 

# Programa Principal
imprimir_hola_mundo()

# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

# Programa Principal
saludar_usuario(input("Ingrese nombre: "))

# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
    

# Programa principal
informacion_personal(input("Ingrese nombre: "), input("Ingrese apellido: "), input("Ingrese edad: "), input("Ingrese residencia: "))

# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

def calcular_area_circulo(radio):
    return math.pi * math.pow(radio, 2)

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# Programa Principal 
radio = int(input('Ingrese radio: '))
print("El area de un circulo es", round(calcular_area_circulo(radio), 2))
print("El perimetro de un circulo es", round(calcular_perimetro_circulo(radio), 2))

# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    hora = segundos // 3600
    return print(f"La cantidad de horas equivalentes son: {hora}")

# Programa Principal
segundos = int(input("Ingrese segundos: "))
segundos_a_horas(segundos)

# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    return print(f"""
    1  x {numero} = {1 * numero}
    2  x {numero} = {2 * numero}
    3  x {numero} = {3 * numero}
    4  x {numero} = {4 * numero}
    5  x {numero} = {5 * numero}
    6  x {numero} = {6 * numero}
    7  x {numero} = {7 * numero}
    8  x {numero} = {8 * numero}
    9  x {numero} = {9 * numero}
    10 x {numero} = {10 * numero} 
""")

# Programa Principal
numero = int(input("Ingrese numero: "))
tabla_multiplicar(numero)

# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b 
    multi = a * b
    div = a / b
    return [f"La suma de {a} + {b} = {suma}. La resta de {a} - {b} = {resta}. La multiplicacion de {a} * {b} = {multi}. La division de {a} / {b} = {div}"]

# Programa Principal
num1 = int(input("Ingrese numero 1: "))
num2 = int(input("Ingrese numero 2: "))
print(operaciones_basicas(num1, num2))

# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    return peso / altura ** altura

# Programa Principal
peso = float(input("Ingrese peso en kg: "))
altura = float(input("Ingrese altura en metros: "))
redondeo = round(calcular_imc(peso, altura), 2)
print(redondeo)

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Programa Principal
c = int(input("Ingrese temperatura en Celsius: "))
print(celsius_a_fahrenheit(c))

# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# Programa Principal
a = int(input("Ingrese numero 1: "))
b = int(input("Ingrese numero 2: "))
c = int(input("Ingrese numero 3: "))
print(round(calcular_promedio(a, b, c), 2))