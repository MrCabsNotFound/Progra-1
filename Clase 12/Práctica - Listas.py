##Ejercicio 1
super = ["cocacola","pan","sopas","fresas","tomates"]
print("Tu primer producto en tu lista es: ", super[0])
print(f"La cantidad de cosas en tu lista es de: {len(super)}" )
print("Tu último producto en tu lista es: ", super[4])

# Ejercicio 2
numeros = [5, 25, 3, 19, 67]
for n in numeros:
    suma = 0
    suma = suma + n
promedio = (suma/len(numeros))
print(f"La suma de tus números es de: {suma}")
print(f"El promedio de tus números es de: {promedio}")

#Ejercicio 3
temperaturas = [28, 35, 19, 31, 22]
for i in temperaturas:
    if i >= 30:
        print(f"Las temperaturas mayores o iguales a 30 son: {i}")