# Ejercicio 1: Bucle for para números pares
for i in range(2, 21 ,2):
    print(i)

# Ejercicio 2: Bucle while con suma acumulativa
suma = 0
while suma <= 100:
    numero = int(input("Ingrese numeros: "))
    suma += numero
print(suma)

# Ejercicio 3: Filtrar palabras por letra inicial
lista = ["apple", "banana", "avocado", "orange", "apricot", "grape"]
for palabra in lista:
    if palabra.lower().startswith('a'):
        print(palabra)
        
# Ejercicio 4: Tabla de multiplicar del 7
for i in range(1,11):
    print(f"7 x {i} = {7 * i}")

# Ejercicio 5: Contador de vocales
cadena = input("Ingrese una palabra: ")
cont_v = 0
vocales = "aeiouAEIOU"
for letra in cadena:
    if letra in vocales:
        cont_v += 1
print(f"El texto contiene {cont_v} vocales.")

# Ejercicio 6: Números repetidos en una lista
list = [3, 1, 3, 5, 1]
repetidos = []
for num in list:
    if list.count(num) > 1 and num not in repetidos:
        repetidos.append(num)
print(repetidos)

# Ejercicio 7: FizzBuz
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")

# Ejercicio 8: Frecuencia de palabras
cadena = "hola hola mundo"
palabras = cadena.split()
cantidad = {}
for palabra in palabras:
    cantidad[palabra] = cantidad.get(palabra, 0) + 1
print(cantidad)

# 🗜 Ejercicio 9: Filtrar consonantes
cadena = "Hola Mundo"
vocales = "aeiouAEIOUáéíóúÁÉÍÓÚ"
consonantes = ''.join([letra for letra in cadena if letra.isalpha() and letra not in vocales])
print(consonantes) 

# Ejercicio 10: Números primos
def es_primo(numero):
    if numero < 2:
        return False
    for divisor in range(2, int(numero**0.5) + 1):
        if numero % divisor == 0:
            return False
    return True
limite = int(input("Ingrese un número entero positivo: "))
print(f"Números primos menores o iguales a {limite}:")
for numero in range(2, limite + 1):
    if es_primo(numero):
        print(numero, end=" ")