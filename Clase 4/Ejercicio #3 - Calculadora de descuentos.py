cliente = input("¿Que tipo de cliente eres? (VIP/Estudiante/Regular) ") #Asignamos
monto = float(input("Ingresa el monto de tu compra (Q):"))
if cliente == "VIP":
    descuento = monto * 0.20
    total = monto - descuento
    print("Tu descuento es de: Q", descuento, "y tu total a pagar por ser cliente VIP es de: Q", total)
elif cliente == "Estudiante":
    descuento = monto * 0.15
    total = monto - descuento
    print("Tu descuento es de: Q", descuento, "y tu total a pagar ser estudiante es de: Q", total)
elif cliente == "Regular":
    descuento = monto * 0.05
    total = monto - descuento
    print("Tu descuento es de: Q", descuento, "y Tu total a pagar por ser cliente regular es de: Q", total)
else:
    descuento = 0
    print("No tienes descuento :(, tu total a pagar es de: Q", monto)
print("Gracias por tu compra")