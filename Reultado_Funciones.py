
#----------------SUMA--------------
def suma():
    a = float(input("Ingrese el primer valor: "))
    b = float(input("Ingrese el segundo valor: "))
    print(f"La suma de {a} y {b} es: {a + b}")

#----------------RESTA--------------
def resta():
    a = float(input("Ingrese el primer valor: "))
    b = float(input("Ingrese el segundo valor: "))
    print(f"La resta de {a} y {b} es: {a - b}")

#----------------MULTIPLICACION--------------
def multiplicacion():
    a = float(input("Ingrese el primer valor: "))
    b = float(input("Ingrese el segundo valor: "))
    print(f"La multiplicacion de {a} y {b} es: {a * b}")

#----------------DIVISION--------------
def division():
    a = float(input("Ingrese el primer valor: "))
    b = float(input("Ingrese el segundo valor: "))
    if b != 0:
        print(f"La division de {a} y {b} es: {a / b}")
    else:
        print("No se puede dividir por cero.")

#----------------FACTORIAL--------------
def factorial_calculo(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_calculo(n - 1)

def factorial():
    n = int(input("Ingrese un número entero positivo: "))
    if n < 0:
        print("Error: El número debe ser positivo")
    else:
        print(f"Resultado: {factorial_calculo(n)}")

#----------------POTENCIA--------------
def potencia_calculo(base, exp):
    if exp == 0:
        return 1
    elif exp < 0:
        return 1 / potencia_calculo(base, -exp)
    return base * potencia_calculo(base, exp - 1)

def potencia():
    base = float(input("Ingrese la base: "))
    exp = int(input("Ingrese el exponente (entero): "))
    print(f"Resultado: {potencia_calculo(base, exp)}")

#----------------CALCULADORA--------------
def calculadora():
    while True:
        print("""
╔══════════════════════════════════╗
║           CALCULADORA            ║
╠══════════════════════════════════╣
║ ╔══════════════════════════════╗ ║
║ ║                              ║ ║
║ ╚══════════════════════════════╝ ║
╠══════════════════════════════════╣
║ ┌────┬────┬────┬────┐           ║
║ │  7 │  8 │  9 │  ÷ │           ║
║ ├────┼────┼────┼────┤           ║
║ │  4 │  5 │  6 │  × │           ║
║ ├────┼────┼────┼────┤           ║
║ │  1 │  2 │  3 │  − │           ║
║ ├────┼────┼────┼────┤           ║
║ │  0 │  F │  ^ │  + │           ║
║ └────┴────┴────┴────┘           ║
║                                  ║
║   F → Factorial                  ║
║   ^ → Potencia                   ║
║                                  ║
║        [  S  ]  Apagar           ║
╚══════════════════════════════════╝
""")

        op = input("Seleccione una operación (+, -, *, /, F, ^, S): ").lower()

        if op == "+":
            suma()
        elif op == "-":
            resta()
        elif op == "*":
            multiplicacion()
        elif op == "/":
            division()
        elif op == "f":
            factorial()
        elif op == "^":
            potencia()
        elif op == "s":
            print("Apagando calculadora...")
            break
        else:
            print("Opción inválida")

#----------------EJECUTAR--------------
calculadora()