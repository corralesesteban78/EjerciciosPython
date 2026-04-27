print ("\nEjercicio 20: Sucesión de Fibonacci")
n = int(input("¿Cuántos términos de la sucesión de Fibonacci quieres ver? "))
a = 0
b = 1
print("Sucesión de Fibonacci:")
for i in range(n):
    print(a, end=" ")
    
    suma = a + b
    a = b
    b = sum
