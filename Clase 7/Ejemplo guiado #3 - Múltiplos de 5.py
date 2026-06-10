# Camino A: usar el paso
print("Camino A: usar el paso")
for i in range (0, 50, 5):
    print(f"{i}")

# Camino B: preguntar con %
print("Camino B: preguntar con %")
n = 50
for i in range(n):
    if i % 5 == 0:
        print(f"{i}")

