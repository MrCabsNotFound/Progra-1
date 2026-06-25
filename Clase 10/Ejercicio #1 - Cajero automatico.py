saldo = 1000  # arrancamos con Q1000, no te emociones tanto
seguir = True

print("Bienvenido al cajero. Tratá de no quedarte sin plata manito.")

while seguir:
    print("\nCajero Automático")
    print("1. Ver saldo")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Salir")

    opcion = input("Elegí una opción: ")

    if opcion == "1":
        print("Tu saldo es: Q", saldo, ". Mejor que nada supongo.")
    elif opcion == "2":
        cantidad = int(input("¿Cuánto querés depositar? Q"))
        saldo = saldo + cantidad
        print("Depósito exitoso broder. Nuevo saldo: Q", saldo)
    elif opcion == "3":
        cantidad = int(input("¿Cuánto querés retirar? Q"))
        if cantidad > saldo:
            print("Ey manito, no tenés tanta plata. Tu saldo es solo Q", saldo)
        else:
            saldo = saldo - cantidad
            print("Retiro exitoso. Nuevo saldo: Q", saldo, ". Ya gastaste :(")
    elif opcion == "4":
        seguir = False
        print("¡Hasta luego! Guardá tus centavos.")
    else:
        print("Esa opción no existe talego, intentá de nuevo.")
