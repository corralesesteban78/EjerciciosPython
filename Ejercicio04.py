primer_valor = int(input("Ingrese el primer valor: "))
segundo_valor = int(input("Ingrese el segundo valor: "))

if primer_valor > segundo_valor:
    print ("El primer valor:",primer_valor,"Es mayor")
elif primer_valor == segundo_valor:
    print ("Los 2 valores son iguales")
else:
    print ("El segundo valor:",segundo_valor,"Es mayor")