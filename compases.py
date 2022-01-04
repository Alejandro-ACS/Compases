import math

notas = ["Redonda", "Blanca", "Negra", "Corchea", "Semicorchea", "Fusa", "Semifusa"]

numerador = int(input("Introduce el numerador: "))

denominador = int(input("Introduce el denominador: "))

# Método para sacar las U.T, U.P y U.C de los compases simples, compuestos y amalgama representados por fracciones propias (numerador menor o igual al denominador)

if numerador <= denominador:
  
  if numerador == 2 or numerador == 3 or numerador == 4:

    print("Unidad de tiempo: " + notas[int(math.log2(denominador))])

    if numerador%2 != 0:

      print("Unidad de compás: " + notas[int(math.log2(denominador)-1*int(numerador/2-0.5))] + " con puntillo")

    else:

      print("Unidad de compás: " + notas[int(math.log2(denominador)-1*int(numerador/2))])

  if numerador == 6 or numerador == 9 or numerador == 12:

    print("Unidad de parte: " + notas[int(math.log2(denominador))])

    print("Unidad de tiempo: " + notas[int(math.log2(denominador)-1)] + " con puntillo")

    if numerador%2 == 0:

      if numerador == 6:

        print("Unidad de compás: " + notas[int(math.log2(denominador)-1*int((numerador/2)/2)-0.5)] + " con puntillo")
        
      else:

        print("Unidad de compás: " + notas[int(math.log2(denominador)-1*int((numerador/2)/2))] + " con puntillo")
      
    else:

      print("Unidad de compás: " + notas[int(math.log2(denominador)-1*2)] + " con puntillo ligada a " + notas[int(math.log2(denominador)-1)].lower() + " con puntillo")

  if numerador == 5 or numerador == 7 or numerador == 11:

    print("Unidad de tiempo: " + notas[int(math.log2(denominador))])

    if numerador == 5:

      print("Unidad de compás: " + notas[int(math.log2(denominador)-1)] + " con puntillo ligada a " + notas[int(math.log2(denominador)-1)].lower())
    
    if numerador == 7:

      print("Unidad de compás: " + notas[int(math.log2(denominador)-2)] + " ligada a " + notas[int(math.log2(denominador)-1)].lower() + " con puntillo")
    
    if numerador == 11:

      print("Unidad de compás: " + notas[int(math.log2(denominador)-3)] + " ligada a " + notas[int(math.log2(denominador)-1)].lower() + " con puntillo")

# Método de "La cuenta de la vieja" para calcular los compases representados por fracciones impropias (numerador mayor al denominador)

if numerador > denominador:

  if numerador == 2 or numerador == 3 or numerador == 4:

    print("Unidad de tiempo: " + notas[int(math.log2(denominador))])

    if numerador == 2:

      print("Unidad de compás: Redonda ligada a redonda")
    
    if numerador == 3:

      if denominador == 1:

        print("Unidad de compás: Redonda con puntillo ligada a redonda con puntillo")
      
      if denominador == 2:

        print("Unidad de compás: Redonda con puntillo")
    
    if numerador == 4:

      if denominador == 1:

        print("Unidad de compás: Redonda con puntillo ligada a redonda con puntillo ligada a redonda")
      
      if denominador == 2:

        print("Unidad de compás: Redonda ligada a redonda")

  elif numerador == 6 or numerador == 9 or numerador == 12:

    print("Unidad de parte: " + notas[int(math.log2(denominador))])

    print("Unidad de tiempo: " + notas[int(math.log2(denominador)-1)] + " con puntillo")
  
    if numerador == 6:

      if denominador == 1:

        print("Unidad de compás: Redonda con puntillo ligada a redonda con puntillo ligada a redonda con puntillo ligada a redonda con puntillo")
      
      if denominador == 2:

        print("Unidad de compás: Redonda con puntillo ligada a redonda con puntillo")

      if denominador == 4:

        print("Unidad de compás: Redonda con puntillo")
    
    if numerador == 9:

      if denominador == 1:

        print("Unidad de compás: Redonda con puntillo ligada a redonda con puntillo ligada a redonda con puntillo ligada a redonda con puntillo ligada a redonda con puntillo ligada a redonda con puntillo")

      if denominador == 2:

        print("Unidad de compás: Redonda con puntillo ligada a redonda con puntillo ligada a redonda con puntillo")

      if denominador == 4:

        print("Unidad de compás: Redonda con puntillo ligada a blanca con puntillo")

      if denominador == 8:

        print("Unidad de compás: Blanca con puntillo ligada a negra con puntillo")

    if numerador == 12:

      if denominador == 1:

        print("Unidad de compás: Redonda con puntillo ligada a redonda con puntillo ligada a redonda con puntillo ligada a redonda con puntillo ligada a redonda con puntillo ligada a redonda con puntillo ligada a redonda con puntillo ligada a redonda con puntillo")

      if denominador == 2:

        print("Unidad de compás: Redonda con puntillo ligada a redonda con puntillo ligada a redonda con puntillo ligada a redonda con puntillo")

      if denominador == 4:

        print("Unidad de compás: Redonda con puntillo ligada a redonda con puntillo")

      if denominador == 8:

        print("Unidad de compás: Redonda con puntillo")
  
  elif numerador == 5 or numerador == 7 or numerador == 11:

    print("Unidad de tiempo: " + notas[int(math.log2(denominador))])

    if numerador == 5:

      if denominador == 1:

        print("Unidad de compás: Redonda con puntillo ligada a redonda con puntillo ligada a redonda ligada a redonda")
      
      if denominador == 2:

        print("Unidad de compás: Redonda con pun tillo ligaa a redonda")
      
      if denominador == 4:

        print("Unidad de compás: Blanca con puntillo ligada a blanca")
    
    if numerador == 7:

      if denomiandor == 1:

        print("Unidad de compás: Redonda con puntillo ligada a redonda con puntillo ligada a redonda ligada a redonda con puntillo ligada a redonda con puntillo")
      
      if denominador == 2:

        print("Unidad de compás: Redonda ligada a redonda ligada a redonda con puntillo")
      
      if denominador == 4:

        print("Unidad de compás: Redonda ligada a blanca con puntillo")
      
    if numerador == 11:

      if denominador == 1:

        print("Unidad de compás: Redonda con puntillo ligada a redonda con puntillo ligada a redonda ligada a redonda con puntillo ligada a redonda con puntillo ligada a redonda ligada a redonda con puntillo ligada a redonda con puntillo")
      
      if denominador == 2:

        print("Unidad de compás: Redonda ligada a redonda ligada a redonda ligada a redonda ligada a redonda con puntillo")
      
      if denominador == 4:

        print("Unidad de compás: Redonda ligada a redonda ligada a redonda con puntillo")
      
      if denominador == 8:

        print("Unidad de compás: Redonda ligada a negra con puntillo")
