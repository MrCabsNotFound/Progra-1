import random

print("¡Bienvenido al juego de adivinanza!")
print("Intenta adivinar el número que pensé entre el 1 y el 100.")

secreto = random.randint(1,100) # Esto genera un número aleatorio entre el 1 y el 100.
adivinando = False # Esta variable interrumpe el ciclo

while not adivinando: # Repite mientras NO haya adivinado
    intento = int(input("Ingresa tu intento: "))
    if intento not in range(1, 101):
        print("Número, inválido, ingresa otro número")
    else:
        if intento == secreto:
            print("¡Felicidades, adivinaste el número")
            adivinando = True # Esto hace que el ciclo se detenga
        elif intento > secreto:
            print("El número secreto es más pequeño")
        elif intento < secreto:
            print("El número secreto es más grande")


