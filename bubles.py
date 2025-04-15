def bucle_for ():
  dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes",
"sábado", "domingo"]
  print(dias_semana)
  for dia in dias_semana:
   print(f"{dia}")
  for i in range(2, 11,2 ):
    print(i)
  colores = ['rojo', 'verde', 'azul']
  for índice, color in enumerate(colores):
    print(índice, color)
    
  dias_semana = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
  for indice, dia in enumerate(dias_semana):
    print(indice, dia)

  nombres = ['Ana', 'Luis', 'Juan']
  edades = [25, 30, 35, 50]
  for nombre, edad in zip(nombres, edades):
    print(f'{nombre} tiene {edad} años')

  bucle_for()

  diccionario = {'a': 1, 'b': 2, 'c': 3}
  for clave, valor in diccionario.items():
    print(clave, valor) # Imprime pares clave-valor

  for clave in diccionario:
    print(clave) # Imprime claves

  for valor in diccionario.values():
    print(valor) # Imprime valor

  contador = 0
  for i in range(1, 11,1 ):
      print(i)
      contador= contador +i
  print(contador)

  """. Escribe un programa que sume todos los números de una lista y
  luego responde ¿Qué tipo de variable utilizamos para resolver?"""
  acumulador= 0
  lista_numeros = [1, 22, 333, 4, 25, 76]
  for numero in lista_numeros:
    acumulador = acumulador + numero
  print(acumulador)
    
  """
  2. Escribe un programa que imprima el cuadrado de los números del 1
  al 10.
  """

  for indice in range(2, 11, 2):
    print(indice **2)

  """
  3. Escribe un programa que cuente los caracteres de una cadena de
  texto proporcionada por el usuario utilizando el for.
  """
  caracteres = input("estriba un texto aqui ")
  contador = 0
  for c in caracteres :
    if c != " " :
      contador  = contador + 1

  print(" la palabra que ingresaste tiene" ,contador ,"letras")

