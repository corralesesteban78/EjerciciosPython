salario = int(input("Ingrese su slario mensual: "))
deuda = input("Tienes alguna deuda si/no: ").lower()

if salario > 1000 and deuda == "no":
    print("Credito Aprovado")
else:
    print("Credito denegado")