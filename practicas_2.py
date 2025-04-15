"""
si el usuario es mayor de edad y tiene saldo en la cuenta entonces puede comprar alcohol
"""

nombre = input("ingresa tu nombre:")
edad = int(input("ingresa tu edad:"))
tiene_dinero = True
tiene_billetera = True
usuario_puede_comprar = "usuario puede comprar" if edad >= 18 or tiene_dinero and tiene_billetera else "usuario no puede comprar"
print(usuario_puede_comprar)

usuario_menor_edad = True if not(edad >= 18) else False
print(usuario_menor_edad)