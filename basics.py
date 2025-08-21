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
print("-------------------------------------------------------")
print("ENTRADA DE VALORES")
# campo = input("Introduce tu edad: ")
campo  = 23
campoint = int(campo)
c3 = CalculadoraUnario(campoint)
print(f"{campo} años es la mitad de {c3.suma()}")
print(type(campoint))
print(type(campo))
print("-------------------------------------------------------")
print("VALORES BOOLEANOS Y EJECUCIÓN DE CONDICIONALES")
#los valores true y false se escriben con Mayúscula al principio en Python
a = True
b = False
#retorna un booleano
c = a and b and True and True
d = a or b and False and False
print(type(c))
print(d)


# calif = int(input("Introduce la calificación: "))
calif = 85
print(type(calif))
if calif <= 100 and calif >=95:
    print("Excelencia académica")
elif calif < 95 and calif >= 85:
    print("Alumno ejemplar")
elif calif < 85 and calif >= 70:
    print("Alumno que pasó")
elif calif < 70:
    print("Alumno reprobado")
else:
    print("Valor incorrecto")
print("-------------------------------------------------------")
print("ESTRUCTURAS DE CONTROL")

n1 = 27
n2 = 29
#IF
if n1 > n2:
    print(f"{n1} es mayor a {n2}")
elif n1 < n2:
    print(f"{n1} es menor a {n2}")
else:
    print(f"{n1} es igual a {n2}")
# while
while n1 < n2:
    print(f"{n1} es menor a {n2}")
    n1 += 1
#for
for i in range(0,10):
    print(i)

#break, continue y else
#El break rompe cualquier ciclo de bucle for o while
for i in range(0,10,3):
    if i == 8:
        continue
    if i == 102:
        break
    print(i)

# COSA NUEVA
# La palabra else funciona con los bucles como lo que se va a ejecutar una vez terminado el ciclo:
for i in range(0,10,2):
    print(i)
else:
    print("Se termina de ejecutar el ciclo for. i = ", i)

print("-------------------------------------------------------")
print("FUNCIONES")
def saludar(nombre):
    print(f"Hola, {nombre}!")
saludar("Maximo")
# el n3 es opcional en este caso
def suma(n1, n2, n3 = 23):
    return n1 + n2 + n3
resultado_suma = suma(10,5, 0)
print(resultado_suma)
print("-------------------------------------------------------")
print("LISTAS")

lista1 = [1,2,3,4,5,6,7,8,9,10]

lista1.reverse()
lista2 = [1,2,3,4,5,6,7,8,9,10]
lista3 = [0] * len(lista2)  # inicializar con el mismo tamaño
print(lista3)
for i in range(len(lista2)):
    print(f"i: {i}")
    print(f"largo de la lista: {len(lista2)}")
    print(f"Indice de lista2: {lista2[i]}")
    lista3[len(lista2) - 1 - i] = lista2[i]
print(lista2)
print(lista3)
# para imprimir en reversa la lista, o sea el ultimo, penultimo y demás
print(lista2[-1])
print(lista2[-2])
#para imprimir el dato a partir de tal posición, digamos que queremos imprimir la lista a partir de la posición 5
print(lista2[4:])
lista4 = [24,13,23,32,23,51,100]
media = 0
contador = 0
for i in range(len(lista4)):
    contador += lista4[i]
    print("contador",contador)
else:
    media = contador / len(lista4)
print(f"La media es de:  {media}")
os.system("clear")
print("-------------------------------------------------------")
print("MANEJ0 DE EXCEPCIONES")
print("bye")
try:
    a1 = int(input("Ingrese un numero: "))
    print("Cuadrado de a: ", a1*a1)
except ValueError: ##Aqui pueden ir varias cosas https://docs.python.org/3/library/exceptions.html
    print("Numero invalido")

#Puedes hacer que cierto espacio busque ciertas excepciones, por ejemplo, buscar las excepçiones de archivo no encontrado y error de valor

try:
    a2 = input("Ingrese su palabra: ")
    a3 = a2
    l1 = list(a2)
    l1.reverse()
    reversed_word  = "".join(l1)
    if a3 == reversed_word:
        print("Su palabra es un palíndromo")
    else:
        print("Su palabra no es un palíndromo.")
except (ValueError, FileNotFoundError):
    print("Falló exitosamente.")















