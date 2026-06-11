# El programa tira un dado (1 al 6) N veces con la librería random, muestra cada tirada y va sumando. Al final da la suma, el promedio y un veredicto.
import random
n = int(input("¿Cuántos dados quieres tirar? :"))
suma = 0

for i in range(n):
    tiro = random.randint(1,6)
    print(f"Tirada {i + 1}: {tiro}")
    suma = suma + tiro
    promedio = suma/n

print(f"Suma total : {suma}")
print(f"{promedio}")
    
if promedio > 3.5:
    print("Buena racha!")
