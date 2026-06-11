# Un cliente compra N productos. Por cada uno el programa pide el precio (en quetzales) y los va sumando. Al finalmuestra el total, y si supera Q500 aplica un 10% de descuento.
n = int(input("¿Cuántos productos compro? "))
total = 0
mas_caro = 0
for i in range(n):
    precio = float(input(f"Precio del producto {i + 1}: "))
    total = total + precio
    if precio > mas_caro:
        mas_caro = precio

if total > 500:
    descuento = round(total * 0.1,2)
    total_a_pagar= round(total * 0.9,2)
    print(f"Total: {total}")
    print(f"Descuento: {descuento}")
    print(f"Total a pagar: {total_a_pagar}")
else:
    print(f"Total a pagar: {total}")

print(f"Producto más caro: {mas_caro}") 
          