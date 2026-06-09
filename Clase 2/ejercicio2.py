nombre = input("¿Cómo te llamas? ")
print("Esta función es para mayores de edad") #El bouncer me mira raro
edad = int(input("¿Cuántos años tienes? ")) # El bounce no me cree que soy mayor de edad
print("¿Tienes boleto? (1/0)") # El bouncer me pregunta si tengo boleto, pero no me cree que tengo boleto
tiene_boleto = int(input("1, Sí, 0, No: "))
puede_entrar = edad >= 18 and tiene_boleto == 1
if puede_entrar == 0:
    print("Lo siento", nombre, ", no puedes entrar.") # Decido suicidarme porque el bouncer no me deja entrar

else:
    print("Hola", nombre, ", puedes entrar:") # Me pongo muy feliz porque el bouncer me deja entrar, y me voy a la fiesta a bailar toda la noche