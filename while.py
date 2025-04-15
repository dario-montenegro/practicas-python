def ejemplo_1 ():
  while True:
    numero = int(input("Introduce un número mayor que 10: "))
    if numero > 10:
      break

    print("El número no es mayor que 10. Intenta de nuevo.")

  print(f"Has introducido el número {numero}, que es mayor que 10.")

def ejemplo_2 ():
  numeros = [10, 20, 30, 40, 42, 50, 60, 70, 80, 90, 100]
  encontrado = False
  numero_a_buscar=42
  for numero in numeros:
    if numero == numero_a_buscar:
      encontrado = True
      break # Sale del bucle tan pronto se encuentra el número 42
  print(f'Número 42 encontrado: {encontrado}')

def ejemplo_3():

  for i in range(1, 11):
    for j in range(1, 11):
      resultado = i * j
      print(f"{i} x {j} = {resultado}")
  print()

"""
1. Escribe un programa que genere un número aleatorio entre 1 y 100 y
permita al usuario adivinar el número. El programa debe brindar pistas
(ej. el número secreto es mayor) y debe continuar pidiendo al usuario
 que adivine hasta que acierte. Al finalizar, debe mostrar el número de
intentos.
"""
"""
1- generar numero aleartorio entre 1 y 100
2- recibir un imput con un numero
3- imprimir si el numero aleartorio es mayor o menor al ingresado
4- mostrar numero de intentos
"""
import random
def ejercicio_5():
  numero_aleartorio = random.randint(1,100)
  numero_intentos = 0
  while True:
    nuemero_recibido = int(input("escribe un numero del 1 al 100: "))
    numero_intentos += 1
    if nuemero_recibido > numero_aleartorio:
      print("el numero ingresado es mayor que el aleartorio")
    elif nuemero_recibido < numero_aleartorio:
      print("el numero ingresado es menor que el aleartorio")
    else:
      print("el numero ingresado es correcto")
      print(f"cantidad de intentos: {numero_intentos}")
      break
ejercicio_5()
