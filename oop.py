import os

#ENTEROS
a = 34
print (10)
print (a)
#FLOTANTES
print (30.54)
print (30.)

#BOOLEANOS
print(True)
print(False)

#CADENAS
print("Maximo Gutierrez")
print('Maximo Gutierrez')

#OCTAL SON VALORES NUMERICOS
print(0o123)

#HEXADECIMAL
print(0x123)

# Listas ordenadas, mutables
fruits = [ "apple", "banana", "cherry" ]
fruits.append("mango")
print(fruits)

# lista Ordenada innmutable
coords = (8, 20)

# Conjuntos (set) no ordenados, únicos
unique_numbers = { 1,2,3,4,5}

#Diccionarios (clave-valor)
person = {
"name": "Maximo",
"age": 18
}

class Person:
    def __init__(self, name, age):  # constructor
        self.name = name
        self.age = age
        self.nacionality = "Mexicano"

    def greet(self):
        return f"Hola, soy {self.name} y tengo {self.age} años"
# Crear objeto
p1 = Person("Ana", 25)
print(p1.greet())
print("-------------------------------------------------------")
print("CALCULADORA DE OPERADORES ARITMÉTICOS BINARIOS")

nmbr1 = 100
nmbr2 = 20
class Calculadora:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def get_a(self):
        return self.a
    def get_b(self):
        return self.b
    # + suma
    def suma(self):
        return self.a + self.b
    # - resta
    def resta(self):
        return self.a - self.b
    # * multiplicación
    def multiplicacion(self):
        return self.a * self.b
    # * división
    def division(self):
        return self.a / self.b

    def division_enteros(self):
        return self.a // self.b
    def potenciar(self):
        return self.a ** self.b
    def residuo(self):
        return self.a % self.b

c1 = Calculadora(nmbr1, nmbr2)
print(c1.suma())
print(c1.resta())
print(c1.multiplicacion())
print(c1.division())
print(f"Division de números enteros de {c1.get_a()} entre {c1.get_b()}: {c1.division_enteros()}")
print(f"Residuo de {c1.get_a()} entre {c1.get_b()}: {c1.residuo()}")
print(f"Potencia de {c1.get_a()} por {c1.get_b()}: {c1.potenciar()}")
print("-------------------------------------------------------")
print("CALCULADORA DE OPERADORES ARITMÉTICOS UNARIOS")
class CalculadoraUnario:
    def __init__(self, a):
        self.a = a

    # + suma
    def suma(self):
        resultado = self.a
        resultado += self.a
        return resultado

    # - resta
    def resta(self):
        resultado = self.a
        resultado -= self.a
        return resultado

    # * multiplicación
    def multiplicacion(self):
        resultado = self.a
        resultado *= self.a
        return resultado

    # / división
    def division(self):
        resultado = self.a
        resultado /= self.a
        return resultado

    # // división entera
    def division_enteros(self):
        resultado = self.a
        resultado //= self.a
        return resultado

    # ** potencia
    def potenciar(self):
        resultado = self.a
        resultado **= self.a
        return resultado

    # % residuo
    def residuo(self):
        resultado = self.a
        resultado %= self.a
        return resultado
    def is_pair(self):
        residuo = self.a
        residuo %= self.a
        if(residuo == 0):
            print(f"El numero: {self.a} es par")
        else: print(f"El numero: {self.a} es impar")

c2 = CalculadoraUnario(9)
print(c2.suma())
print(c2.resta())
print(c2.multiplicacion())
print(c2.division())
print(c2.division_enteros())
print(c2.potenciar())
print(c2.residuo())
c2.is_pair()
os.system("clear")
print("-------------------------------------------------------")
print("ENTRADA DE VALORES")
campo = input("Introduce tu edad: ")
campoint = int(campo)
c3 = CalculadoraUnario(campoint)
print(f"{campo} años es la mitad de {c3.suma()}")
print(type(campoint))
print(type(campo))
