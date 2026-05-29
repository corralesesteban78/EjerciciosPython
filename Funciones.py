def mostrar_mensaje():
    print("Bienvenido a la funcion de bienvenida" )
    print("Por favor, seleccione una opcion:")
    print("1. Opcion 1")
    print("2. Opcion 2")    
    print("3. Opcion 3")
    print("4.Salir")

mostrar_mensaje()

def saludar(nombre, edad):
    print(f"Hola, {nombre}! Tienes {edad} años.")

saludar("Esteban", 17)

def tirar_dado():
    import random
    resultado = random.randint(1, 6)
    print(f"Has tirado un dado y el resultado es: {resultado}")

tirar_dado()

def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area

mi_area = calcular_area_rectangulo(5, 3)
print(f"El area del rectangulo es: {mi_area}")