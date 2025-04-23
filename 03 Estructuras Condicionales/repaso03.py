# Ejercicio 1: Validación de contraseña
contrasena_correcta = "programacion1" and "PROGRAMACION1"
contrasena_usuario = input("Introduce la contraseña: ")
if contrasena_usuario == contrasena_correcta:
    print("Contraseña correcta. Bienvenido.")
else:
    print("Contraseña incorrecta. Intenta de nuevo.")

# Ejercicio 2: Identificador de vocales
letra = input("Ingrese una letra: ")
if letra == "a" or "e" or "i" or "o" or "u" or "A" or "E" or "I" or "O" or "U" :
    print("La letra ingresada es una vocal")
else:
    print("La letra ingresada no es una vocal")

# Ejercicio 3: Clasificador de números
numero = int(input("Ingrese Numero: "))
if numero > 0:
    print("El número es positivo")
elif numero < 0:
    print("El número es negativo")
else:
    print("El número es cero")

# Ejercicio 4: Comparador de números
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
if num1 > num2:
    print("El primer número ingresado es mayor")
elif num1 < num2:
    print("El primer número ingresado es menor")
else:
    print("Los números ingresados son iguales")

# # Ejercicio 5: Clima según temperatura
c = int(input("Ingrese temperatura en celsius: "))
if c <= 10:
    print("Hace frío")
elif c <= 25:
    print("Está templado")
else:
    print("Hace calor")

# Ejercicio 6: Detector de años bisiestos
anio = int(input("Ingrese un anio: "))
if anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0:
    print("Se ingresó un año bisiesto")
else:
    print("Se ingresó un año no bisiesto")

# Ejercicio 7: Ajustador de frases
palabra = input("Ingrese una palabra: ")
if palabra and not palabra.endswith('.'):
    entrada_ajustada = palabra + '.'
else:
    entrada_ajustada = palabra
print(entrada_ajustada)

# Ejercicio 8: Validador de contraseña segura 
# Ejercicio 9: Mejorando mensajes de error
passw = input("Crea una Password: ")
if (8 <= len(passw) <= 20 and any(c.isupper() for c in passw) and any(c.isdigit() for c in passw)):
    print("¡Felicitaciones! Creaste tu contraseña.") 
else:
    print("La contraseña no es segura.")
    if len(passw) < 8 or len(passw) > 20:
        print("Longitud incorrecta (8-20 caracteres)")
    if not any(c.isupper() for c in passw):
        print("Falta letra mayúscula")
    if not any(c.isdigit() for c in passw):
        print("Falta número")

# Ejercicio 10: Piedra, papel o tijera
jug1 = input("Coloca tu jugada JUGADOR 1(piedra, papel, tijera): ")
jug2 = input("Coloca tu jugada JUGADOR 2(piedra, papel, tijera): ")
if jug1 == jug2:
    print("EMPATE")
elif jug1 == "piedra" and jug2 == "papel" or jug1 == "papel" and jug2 == "tijera" or jug1 == "tijera" and jug2 == "piedra":
    print("GANA JUGADOR 2")
elif jug1 == "piedra" and jug2 == "tijera" or jug1 == "papel" and jug2 == "piedra" or jug1 == "tijera" and jug2 == "papel":
    print("GANA JUGADOR 1")
