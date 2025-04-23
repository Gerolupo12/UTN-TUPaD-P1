import math
#Ejercicio 1: Cálculo del área y el perímetro de un rectángulo
ancho = float(input("Ingrese el ancho: "))
alto = float(input("Ingrese el alto: "))
f = ancho * alto
p = (ancho * 2) + (alto * 2)
print(f)
print(p)

# Ejercicio 2: Conversión de grados Celsius a Fahrenheit
t = float(input("Ingrese temperatura en celsius: "))
f = (t * 9/5) + 32
k = t + 273.15
print(f)
print(k)

# Ejercicio 3: Uso de booleanos
a = True
b = False
print(a and b)
print(a or b)
print(not a)
print(not b)

# Ejercicio 4: Prueba de escritorio
a = 5
b = 3
c = a + b
a = 2
print(c)

# Ejercicio 5: Diagrama de flujo – Cuadrado de un número
n = input("Ingrese numero: ")
c = n ** 2
print(c)

# Ejercicio 6: Intercambio de variables
x = 10
y = 20
print(x)
print(y)
x = x + y
y = x - y
x = x - y
print(x)
print(y)


# Ejercicio 7: Cálculo del IMC (Índice de Masa Corporal)
p = float(input("Ingrese el peso en kg: "))
a = float(input("Ingrese la altura en metros: "))
imc = p / (a ** 2)
print(f"Tu IMC es: {imc}")


# Ejercicio 8: Contador de caracteres en un nombre
nombrec = input("Ingrese su nombre completo: ")
t = len(nombrec.replace(" ", ""))
l = nombrec[:3]
resultado = "".join(
    letra.upper() if i % 2 == 0 else letra.lower()
    for i, letra in enumerate(nombrec)
)
print("Texto alternado:", resultado)
print(t)
print(l)

# Ejercicio 9: Operaciones con números flotantes
a = 7.5
b = 3.2
suma = (a + b)
r = round(a / b, 2) 
p = math.pow(a, b)
print(suma)
print(r)
print(p)

# Ejercicio 10: Descuento sobre precio original
precio = int(input("Ingrese precio original: "))
descuento = int(input("Ingrese descuento: "))
precio_final = precio * (1 - (descuento / 100))
print(precio_final)