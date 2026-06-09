print("Bienvenido al juego del adivinador de números.")
print("El juego consiste en adivinar el número secreto.")
print("Si lo adivinas, perfecto, si no, MUERES.")
secreto = 67 #Este es el número secreto que el jugador tiene que adivinar"
intento = int(input("Adivina el número: "))
if intento == secreto:
    print("Felicidades, sobreviviste, el número secreto era", secreto)
elif intento > secreto:
    print("¡El hueso manito, te pasaste talego, intenta con un número más pequeño!")
    print("Tu intento:", intento, "te doy una pista, la diferencia de tu número con el número secreto es de", abs(intento - secreto))
elif intento < secreto:
    print("Como así broder, te quedaste corto, intenta con un número más grande")
    print("Tu intento:", intento, "te doy una pista, la diferencia de tu número con el número secreto es de", abs(intento - secreto))  
print("Tu intento: ", intento)