correcta = "python123"  # esta es la clave, no se la digas a nadie
intentos = 1

print("Sistema de acceso. Tenés 3 intentos, no la cagues.")

clave = input("Ingresá la contraseña: ")

while clave != correcta and intentos < 3:
    print("Contraseña incorrecta manito, intentá de nuevo antes de que te bloquee.")
    clave = input("Ingresá la contraseña: ")
    intentos = intentos + 1

if clave == correcta:
    print("¡Bienvenido! Lo lograste en el intento", intentos, ":)")
else:
    print("Cuenta bloqueada. Perdiste talego, adiós :(")
