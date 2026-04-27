peso = float(input("Ingrese tu peso en Kg: "))
altura = float(input("Ingrese tu altura en metros: "))

IMC = peso / (altura ** 2)

if IMC < 18.5:
    print("Bajo peso")
elif IMC >= 18.5 and IMC <= 24.9:
    print("Peso Normal")
elif IMC >= 25 and IMC <= 29.9:
    print("Sobrepeso")
else:
    print("Obesidad")