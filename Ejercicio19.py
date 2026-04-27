
total = 0
print("--- Caja Registradora ---")
print("Introduce los precios de los productos (Escribe 0 para terminar):")
while True:
    precio = float(input("Precio del producto: $"))
    if precio == 0:
        break
    total += precio
if total > 100:
    descuento = total * 0.10
    total_final = total - descuento
    print(f"\nSubtotal: ${total:.2f}")
    print(f"Descuento aplicado (10%): -${descuento:.2f}")
else:
    total_final = total
    print(f"\nSubtotal: ${total:.2f}")
    print("No se aplicó descuento (compra menor o igual a $100).")
print(f"Total a pagar: ${total_final:.2f}")