#conjunto (llaves)
colores = {"verde", "amarillo", "rojo"}
colores.add("azul")
#print(colores)
colores.pop()
#print(colores)


#lista (corchetes)

numeros = [10, "verde", True, colores]
#print(numeros)
numeros.append("perro")
#print(numeros)

#tuplas (parentesis)

vocales = ("a", "a", "a", "o", "u")
num_vocales = vocales.count("a") 

#print(num_vocales, vocales)


#conjuntos inmutables frozenset ( parentesis y corchetes)

dias = frozenset(["lunes", "martes", "miercoles"])
#print(dias)


#diccionario (entre llaves clave: valor)

persona1 = {
  "nombre": "dario",
  "apellido": "montenegro",
  "edad": 30
  }

#print(persona1)
persona1["edad"] = 31 
#print(persona1["edad"])


#1. Escribe un programa que pida al usuario el radio de un círculo y
# calcule el área.

PI = 3.1416
radio = 5
area = PI * radio**2
#print(area)

area_int = int(area)
#print(area_int)

#2. Escribe un programa que convierta una temperatura dada en grados Celsius a grados Fahrenheit.
# (temp_c × 9/5) + 32 =  temp_f


temp_c = 20
temp_f = (temp_c * 9/5) + 32
#print(temp_f)
import math
#Escribe un programa que pida al usuario los dos catetos de un triángulo rectángulo y calcule la hipotenusa.
#a²+b²= c².
cateto_1 = 30
cateto_2 = 10
hipotenusa = math.sqrt(cateto_1**2 + cateto_2**2)
#print(hipotenusa)

"""
Escribe un programa que pida al usuario su año de nacimiento,
calcule su edad y genere un mensaje de saludo personalizado que
incluya su nombre y la edad calculada.
"""

nacimiento = 1998
nombre = "agustin"
anio_actual = 2025
edad = anio_actual - nacimiento
#print(edad)
#print( "hola", nombre, edad, "años")

es_mayor_edad = True if edad >= 18 else False
#print(es_mayor_edad)

#print (nombre, edad, es_mayor_edad)

persona2 = {
"Nombre" : nombre,
"Edad" : edad,
"Es mayor de edad" : es_mayor_edad
}

#print(persona2)




