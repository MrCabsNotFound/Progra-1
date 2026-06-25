seguir = True

print("Bienvenido a la tabla de multiplicar che.")

while seguir:
    n = int(input("\nIngresá un número: "))

    print(f"\nTabla de: {n}")
    i = 1
    suma = 0
    while i <= 10:
        resultado = n * i
        suma = suma + resultado
        print(f"{n} x {i} = {resultado}")
        i = i + 1

    print(f"Suma de todos los resultados: {suma}")

    otra = input("\n¿otra tabla? (s/n): ")
    if otra == "n":
        seguir = False
        print("¡Listo che! Ya sos un maestro de la multiplicación.")
