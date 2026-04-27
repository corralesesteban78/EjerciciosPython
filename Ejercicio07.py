total_compra = int(input("Ingrese el total de tu compra: "))

if total_compra < 50:
    print ("No hay descuento")
elif total_compra >= 50 and total_compra <= 100:
    descuento = total_compra * 0.05
    print ("Tu total a pagar es:", total_compra - descuento)
else:
    descuento = total_compra * 0.10
    print ("Tu ytotal a pagar es:", total_compra - descuento)