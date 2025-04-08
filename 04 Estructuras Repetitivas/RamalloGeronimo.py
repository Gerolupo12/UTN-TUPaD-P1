import math
import random

# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
for i in range(101):
    print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.
nume = int(input("Ingrese un numero: "))
dig = 0

if nume == 0:
    dig += 1
else:
    while nume > 0:
        dig += 1
        nume = math.trunc(nume / 10) 

print(f"La cantidad de digitos es {dig}")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.
num1 = int(input('Ingrese un primer numero: '))
num2 = int(input('Ingrese un segundo numero: '))
acu = 0

if num1 > num2:
    mayor = num1
    menor = num2
else:
    mayor = num2
    menor = num1
    
for i in range(menor+1, mayor, 1):
    acu += i

print(acu)

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.
suma = 0
numm = int(input("Ingrese numeros para sumarlos, ponga 0 para cortar la secuencia: "))

while numm != 0:
    suma += numm
    numm = int(input("Ingrese numeros para sumarlos, ponga 0 para cortar la secuencia: "))

print(f'El total acumulado es: {suma}')

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
rand = random.randint(0, 9)
numer = int(input('Adivine el numero que esta entre 0 y 9: ')) 
inte = 1

while numer != rand:
    inte += 1
    numer = int(input('Adivine el numero que esta entre 0 y 9: ')) 

print(f'La cantidad de intentos fue: {inte}')

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.
for x in range(100, 0, -2):
    print(x)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.
number = int(input('Ingrese numero: '))
acum = 0

for j in range(1, number):
    acum += j
    
print(acum)

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).
pos = 0
neg = 0
par = 0
imp = 0

for p in range(1,101):
    num = int(input('Ingrese numero: '))
    if num % 2 == 0:
        par += 1
    else:
        imp += 1
    if num > 0:
        pos += 1
    else:
        neg += 1

print(f'La cantidad de positivos son: {pos}')
print(f'La cantidad de negativos son: {neg}')
print(f'La cantidad de pares son: {par}')
print(f'La cantidad de impares son: {imp}')

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).
acumu = 0
cont = 0

for h in range(1, 5):
    n = int(input('Ingrese numero: '))
    acumu += n
    cont += 1

prom = acumu / cont
print(f'El promedio de los numeros ingresados es: {prom}')

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
numbers = int(input('Ingrese numero: '))
i = 0
while numbers > 0:
	digito = numbers % 10
	i = (i * 10) + digito
	numbers = math.trunc(numbers / 10)

print(f"El numero al reves queda asi {i}") 