print("Cajero Automático Básico")
saldo = 1000
while True:

    print("   MENÚ DEL CAJERO AUTOMÁTICO")
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Ingresar dinero")
    print("4. Salir")
    opcion = input("Elige una opción (1, 2, 3 o 4): ")
    
    if opcion == "1":
        print(f"Tu saldo actual es: ${saldo:.2f}")
    elif opcion == "2":
        cantidad = float(input("¿Cuánto dinero deseas retirar? $"))
        if cantidad <= saldo:
            saldo -= cantidad
            print(f"Has retirado ${cantidad:.2f}. Tu nuevo saldo es: ${saldo:.2f}")
        else:
            print("Saldo insuficiente para realizar el retiro.")
    elif opcion == "3":
        cantidad = float(input("¿Cuánto dinero deseas ingresar? $"))
        saldo += cantidad
        print(f"Has ingresado ${cantidad:.2f}. Tu nuevo saldo es: ${saldo:.2f}")
    elif opcion == "4":     
        print("Gracias por usar el cajero. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elige 1, 2, 3 o 4.")