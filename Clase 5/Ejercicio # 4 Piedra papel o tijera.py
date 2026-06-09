import random

jugada = input("Ingrese su jugada (piedra, papel o tijera): ")
print ("Tu jugada es: ", jugada)

pc = random.choice(["piedra", "papel", "tijera"])
print("La jugada de la computadora es: ", pc)
if jugada not in ["piedra", "papel", "tijera"]:
    print("Jugada no válida")
else:
    if jugada == "piedra" and pc == "tijera":
        print("Gana jugador")
    elif jugada == "papel" and pc == "piedra":
        print("Gana jugador")
    elif jugada == "tijera" and pc == "papel":
        print("Gana jugador")
    elif jugada == pc:
        print("Empate")
    else:
        print("Gana computadora")