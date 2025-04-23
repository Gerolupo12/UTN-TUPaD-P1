import math

# 1) Dado el diccionario precios_frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print(precios_frutas)

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print(precios_frutas)

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
# precios.
lista = [precios_frutas.keys()]
print(lista[0])

# 4) Crear una clase llamada Persona que contenga un método __init__ con los atributos
# nombre, pais y edad y el método saludar. El método saludar debe imprimir por pantalla un
# mensaje de salud que siga la estructura "¡Hola! Soy [nombre], vivo en [pais] y tengo [edad]
# años."

class Persona:
    def __init__(self, nombre, pais, edad):
        self.nombre = nombre
        self.pais = pais
        self.edad = edad

    def saludar(self):
        print(f"¡Hola! Soy {self.nombre}, vivo en {self.pais} y tengo {self.edad} años.")

user1 = Persona('Geronimo', 'Argentina', 21)
user1.saludar()

# 5) Crear una clase llamada Circulo que contenga el atributo radio y los métodos calcular_area y
# calcular_perimetro. Dichos métodos deben calcular el parámetro correspondiente.
# Ayuda: el módulo math puede ser de utilidad para usar la constante 𝜋.

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        area = 2 * math.pi * self.radio
        print(f"El area va a ser: {area}")

    def calcular_perimetro(self):
        peri = math.pi * self.radio + self.radio
        print(f"El perimetro va a ser: {peri}")

circulo = Circulo(3)
circulo.calcular_area()
circulo.calcular_perimetro()
# 6) Dado un string con paréntesis "()", "{}", "[]", verifica si están correctamente
# balanceados usando una pila.
class Pila:
    def __init__(self):
        self.simbolo = {')': '(', '}': '{', ']': '['}
    
    def balanceo(self, cadena: str) -> bool:
        pila = []
        for caracter in cadena:
            if caracter in self.simbolo.values():  # Si es apertura
                pila.append(caracter)
            elif caracter in self.simbolo:  # Si es cierre
                if not pila or pila.pop() != self.simbolo[caracter]:
                    return False
        return not pila

# Ejemplo de uso
balanceador = Pila()

print(balanceador.balanceo(""))  # True

# 7) Usa una cola para simular un sistema de turnos en un banco. La cola debe permitir:
# ● Agregar clientes (encolar).
# ● Atender clientes (desencolar).
# ● Mostrar el siguiente cliente en la fila.
# 8) Crea una lista enlazada que permita insertar nodos al inicio y recorrer la lista para mostrar
# los valores almacenados.
# w