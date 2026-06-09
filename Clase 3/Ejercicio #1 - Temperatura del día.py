# ejercicio que mida la temperatura del día.
temperatura = float(input("Ingresa la temperatura del día en grados Celsius: ")) # Esto es una variable con un float input para que el usuario ingrese la temperatura del día.
Registro_de_temperaturas = "Temperatura registrada: " + str(temperatura) + " Celsius"
print(Registro_de_temperaturas)
if temperatura > 30 and temperatura <= 50:
    print("Hace calor. Toma agua")
elif temperatura >= 15 and temperatura <= 30:
    print("Clima agradable.")
elif temperatura < 15 and temperatura >= 0:
    print("Hace frío. Abrígate.")
elif temperatura < 0:
    print("Hace mucho frío. Quédate en casa.")
else: 
    print("El hueso manito, estas en el infierno xd.")