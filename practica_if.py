metodo_pago = input("como vas a pagar: ")
if metodo_pago == "efectivo":
  print("paga con efectivo")

elif metodo_pago == "tarjeta":
  tipo_tarjeta = input("tipo de tarjeta :")
  if tipo_tarjeta == "debito":
    print("paga con debito")
  elif tipo_tarjeta == "credito":
    print("paga con credito")
  else:
    print("no se reconoce el tipo de tarjeta")

elif metodo_pago == "transferencia":
  print("paga con transferencia")

else:
  print("metodo de pago no reconocido")
