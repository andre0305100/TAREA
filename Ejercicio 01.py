def estCondicional02():
  #Definir variables y otros
  print("Ejercicio 02 Est. Condicional")
  montoP=0
  #Datos de entrada
  cantidadX=int(input("Ingrese la cantidad personas invitadas:"))
  #Proceso
  if cantidadX<200:
    montoP=cantidadX*95
  elif cantidadX>200 and cantidadX<=300:
    montoP=cantidadX*85
  else:
    montoP=cantidadX*75
  #Datos de salida
  print("La cantidad a pagar es:", montoP)
def votoElecciones():
  print ("Como saber si puedes votar por tu edad")
  mensaje=""
  edadP=int(input("ingrese la edad que tiene:"))
  if edadP>=18:
    mensaje="Usted tiene la edad necesaria para votar"
  else:
    mensaje="Usted no cumple con la edad minima para votar"
  print(mensaje) 
