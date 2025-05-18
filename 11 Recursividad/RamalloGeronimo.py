# Ejercicio 1
def factorial(num):
     if num == 0:
         return 1
     else:
         return num * factorial(num - 1)

num = int(input("Ingrese el numero para hacerle el factorial: "))
print(f"El factorial de {num} es {factorial(num)}")

# Ejercicio 2
def fibonacci(numero):
    if numero == 0:
       return 0
    elif numero == 1:
        return 1
    else:
        return fibonacci(numero - 1) + fibonacci(numero - 2)

num = int(input("Ingrese el numero hasta donde se desee contar el fibonacci: "))
print(fibonacci(num))

# Ejercicio 3
def potencia(a, b):
    if b == 0:
        return 1
    else:
        return a * potencia(a, b - 1)

num = int(input("Ingrese el numero a elevar: "))
exp = int(input("Ingrese el exponente: "))
print(potencia(num, exp))

# Ejercicio 4
def num_entero(num):
    if num <= 1:
        return str(num)
    else:
        return num_entero(num // 2) + str(num % 2)


numero = int(input("Ingrese numero: "))
print(num_entero(numero))

# Ejercicio 5
def es_palindromo(cadena):
     if len(cadena) <= 1:
         return True
     if cadena[0] != cadena[-1]:
         return False
     return es_palindromo(cadena[1:-1])

texto = input("Ingrese cadena: ")
print(es_palindromo(texto))

# Ejercicio 6
def suma_digitos(n):
    if n == 0:
        return n
    else:
        return suma_digitos(n // 10) + (n % 10)

num = int(input("Ingrese el numero: "))
print(suma_digitos(num))

# Ejercicio 7
def contar_bloques(num):
    if num == 1:
        return 1
    else:
        return contar_bloques(num - 1) + num

bloque = int(input("Ingrese el bloque menor: "))
print(contar_bloques(bloque))

# Ejercicio 8
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    ult_digito = numero % 10
    if ult_digito == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return 0 + contar_digito(numero // 10, digito)

num = int(input("Ingrese numero: "))
digito = int(input("Ingrese digito a contar: "))
print(contar_digito(num, digito))