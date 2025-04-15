"""
1- Devuelve la posición (el index, un número) del amigo “Matías”.
2- Devuelve la misma lista pero añadiendo los amigos de la infancia
“Ivana” y “Andrés” como otra lista.
3- Agrega un nuevo amigo “María” y devuelve el nro de amigos.
4- Elimina el último elemento amigo y devuelve el nombre del amigo
eliminado.
5- Devuelve un arreglo ordenado alfabéticamente.
"""
def ejercicio_1(): #lista

  amigos = ['Ana', 'Monica', 'José', 'Camila', 'Raquel','Matías']
  indice_matias = amigos.index("Matías")
  print(indice_matias)
  amigos_infancia = ["Ivana", "Andrés"] 
  total_amigos = amigos + amigos_infancia
  print(total_amigos)
  total_amigos.append("María")
  cantidad_amigos = 0
  for i in total_amigos:
    cantidad_amigos += 1
  print(cantidad_amigos)
  print(len(total_amigos))
  total_amigos.sort()
  print(total_amigos)


"""
¡Pongámonos a prueba!
1. Crea una lista de números desordenados y ordénala en orden
ascendente y descendente.
2. Crea una lista de números que cuente el número de veces que
aparece el número ingresado por el usuario.
3. Crea una tupla con tus tres colores favoritos e imprime sólo el
segundo color.
4. Crea una tupla de números y verifica si el número ingresado por el
usuario existe.
"""

def ejercicio_2(): #lista
  lista_numeros = [3, 5, 7, 2, 8, 6, 3, 2, 2, 2]
  lista_numeros.sort()
  print(lista_numeros)
  lista_numeros.reverse()
  print(lista_numeros)
  num_ingresado = int(input(" ingrese un numero: "))
  cantidad_coincidencia = lista_numeros.count(num_ingresado)
  print(f"el numero {num_ingresado} esta {cantidad_coincidencia} veces")


def ejercicio_3():
  colores_fav = ("violeta" ,"negro", "blanco")
  print(colores_fav[1])

def ejercicio_4():
  numeros = (1, 2, 3, 4, 5)
  numero_usuario = int(input("escriba un numero"))
  numero_existe = False
  for i in numeros:
    if i == numero_usuario:
      numero_existe = True
  if numero_existe:
    print("el numero existe")
  else:
    print("el numero no existe")


def ejercicio_5():
  numeros = (1, 2, 3, 4, 5)
  numero_usuario = int(input("escriba un numero"))
  for i in numeros:
    if i == numero_usuario:
      print("el numero existe")
      break
  else:
    print("el numero no existe")

    
"""
1. Escribe un programa que administre el inventario de una tienda.
El programa debe permitir agregar nuevos productos, actualizar
las cantidades de los productos existentes, y mostrar el
inventario actual."""
"""2. Escribe un programa que permita llevar un registro de las
calificaciones de varios estudiantes. El programa debe permitir
agregar estudiantes con sus calificaciones, actualizar las
calificaciones de un estudiante existente y mostrar el promedio
de calificaciones de un estudiante específico.
"""
def ejercicio_7():
  inventario_tienda = { "guantes" : 20 ,
                       "aplicadores": 15, 
                        "pinceles" : 8,
                         "cepillos" : 9 }
  inventario_tienda["perfumes"] = 16
  inventario_tienda["guantes"] = 18
  pares = inventario_tienda.items()
  
  print(pares)

def ejercicio_8():

  dario = {"matermatica" : 9,
           "lengua" : 6,
           "geografia": 7,
           "ingles": 2}
  mica = {"matermatica": 8,
          "lengua" : 9,
          "geografia " : 8,
          "ingles" : 8 }
  alma = {"matematica" : 9,
          "lengua" : 8 ,
          "geografia": 7 ,
          "ingles": 6
          }
  lista_estudiantes = (dario, mica, alma)
  print(lista_estudiantes)
ejercicio_8()