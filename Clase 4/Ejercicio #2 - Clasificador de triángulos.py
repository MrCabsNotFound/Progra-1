# Luis Roberto Ardón 20250081 y Santiago Cabarrús 20250411
print("Bienvenido al clasificador de triángulos.")
a = int(input("Ingresa el valor del primer lado del triángulos: "))
b = int(input("Ingresa el valor del segundo lado del triangulo: "))
c = int(input("Ingresa el valor del tercer lado del triángulo: "))

if a == b and b == c:
    print("El tríangulo es equilátero.")
elif a == b or b == c or a == c:
    print("El triángulo es isósceles:")
else:
    print("El triángulo es escaleno.")
print("Gracias por usar el clasificador de triángulos.")