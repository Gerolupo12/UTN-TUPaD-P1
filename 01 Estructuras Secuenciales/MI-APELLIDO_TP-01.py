# Ejercicio 1
print("Hola Mundo") 
print("\n")

# Ejercicio 2
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")
print("\n")

# Ejercicio 3
nombre1 = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
lugar = input("Ingrese su residencia: ")
print(f"Soy {nombre1} {apellido}, tengo {edad} años y vivo en {lugar}")
print("\n")

# Ejercicio 4
pi = 3.14
radio = int(input("Ingrese radio de un circulo: "))
area = pi * radio * radio 
perimetro = pi * 2 * radio
print(f"El area de un circulo es: {round(area, 2)}")
print(f"El perimetro de un circulo es: {perimetro}")
print("\n")

# Ejercicio 5
seg = int(input("Ingrese cantidad de segundos: "))
hora = seg // 3600
print(f"La cantidad de horas son: {hora}")
print("\n")

# Ejercicio 6
num = int(input("Ingrese numero: "))
print(f"""
    {num} x 1 = {num * 1}
    {num} x 2 = {num * 2}
    {num} x 3 = {num * 3}
    {num} x 4 = {num * 4}
    {num} x 5 = {num * 5}
    {num} x 6 = {num * 6}
    {num} x 7 = {num * 7}
    {num} x 8 = {num * 8}
    {num} x 9 = {num * 9}
""")
print("\n")

# Ejercicio 7
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
print(a + b, a / b, a * b, a - b)
print("\n")

# Ejercicio 8
a = int(input("Ingrese altura en metros: "))
p = int(input("Ingrese peso: "))
imc = p / a ** 2
print(f"El indice de masa corporal es: {imc}")
print("\n")

# Ejercicio 9
c = int(input("Ingrese temperatura en Celsius: "))
f = ((9 / 5) * c) + 32
print(f"La temperatura en Fahrenheit es: {f}")
print("\n")

# Ejercicio 10
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
c = int(input("Ingrese el tercer numero: "))
p = (a + b + c) / 3
print(f"El promedio de los tres numeros es: {p}")

