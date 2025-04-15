"""
1. Escribe un programa que a partir de un número entero positivo,
muestre por pantalla si es par o impar.
2. Escribe un programa que a partir de un número entero positivo,
muestre por pantalla si es primo o no.
3. Escribe un programa que permita realizar la división de dos
números siempre y cuando el denominador no sea 0.
"""

def ejercicio_1():
  numero = int(input("ingresar un numero entero positivo: "))
  if numero >= 0:
    if numero % 2 == 0 :
      print("el numero es par")
    else:
      print("el numero es impar")
  else:
    print("el numero es incorrecto")

def ejercicio_3():
  numero_1 = 10
  numero_2 = 0
  if numero_2 != 0:
    resultado = numero_1 / numero_2
    print(resultado) 
  else:
    print("nunero no valido")

"""
Desafío
Modifica el siguiente código (que identifica el mayor de dos números) a
fin de encontrar ahora el mayor de 3 números.
"""
def ejercicio_4():
  numero_1 = 12
  numero_2 = -5
  numero_3 = 25
  if numero_1 > numero_2 and numero_1 > numero_3:
    print(f"El mayor de los tres números es: {numero_1}")
  elif numero_2 > numero_3 and numero_2 > numero_1:
    print(f"el mayor de los tres numero es: {numero_2}")
  else:
    print(f"El mayor de los dos números es: {numero_3}")


"""
1. Escribe un programa que solicite tres lados de un triángulo e indique
si es equilátero, isósceles o escaleno.
"""
def ejercicio_5():
  lado_a = int(input("ingrese valor lado a: "))
  lado_b = int(input("ingrese valor lado b: "))
  lado_c = int(input("ingrese valor lado c: "))
  if (lado_a == lado_b) and (lado_a == lado_c):
    print("el triangulo es equilatero")
  elif (lado_a != lado_b) and (lado_a != lado_c) and (lado_b != lado_c):
    print("el triangulo es escaleno")
  else:
    print("el triangulo es isosceles")

"""
2. Escribe un programa que solicite al usuario que ingrese una
contraseña y confirme la contraseña. El programa debe verificar si
ambas contraseñas coinciden y no están vacías.
"""
def ejercicio_5():
  contrasena = input("escriba contraseña: ")
  confirme_contrasena = input("confirme contraseña: ")
  if (contrasena == confirme_contrasena) and (contrasena != ""):
    print("contraseñas coinciden")
  else:
    print("su contraseña no coincide")


"""4. Escribe un programa que solicite al usuario su nombre, edad y
número de teléfono. Verifica que ninguno de estos datos esté vacío
o sea un valor falso (por ejemplo, 0)."""

def ejercicio_6():
  nombre =  input("escriba tu nombre: ")
  print(type (nombre))
  if nombre == "":
    print("dato no invalido")
  edad = int(input ("escriba su edad: "))
  if edad == "" or edad == 0 :
    print("dato no valido")
  telefono = int(input("escriba su numero de telefono: "))
  if telefono == "" or telefono == 0:
    print("dato no valido")
  if nombre and edad and telefono != True:
    print("todos los datos ingresados son correctos")
  
ejercicio_6()


"""
3. Escribe un programa que solicite al usuario el precio y la cantidad de
un producto. Clasifique el producto como "caro" si el precio es
mayor de $100 o si la cantidad es menor que 10 y el precio es
mayor de $50. De lo contrario, clasifíquelo como "barato". 
Incluye condiciones para manejar valores falsos (0 o vacío).
"""
def funcion_7():
  precio_producto  = int(input("precio de producto"))
  cantidad_producto = int(input("cantidad de producto"))
  if (precio_producto > 100) or (cantidad_producto < 10 and precio_producto > 50):
    print("el producto es caro")
  else:
    print("el producto es barato")
   
