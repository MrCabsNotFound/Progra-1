print("¡Bienvenido a la mejor casa de apuestas del mundo!") # El dueño de la casa de apuestas me da la bienvenida a su establecimiento
edad = int(input("¿Cuántos años tienes? ")) # El dueño de la casa de apuestas me pregunta mi edad para verificar que soy mayor de edad
if edad < 18:
    print("Lo siento, no puedes apostar aquí.") # El dueño de la casa de apuestas me dice que no puedo apostar porque soy menor de edad
else:
   print("¿Eres administrador? (1, SI/0, NO)") # El dueño de la casa de apuestas me pregunta si soy administrador para darme acceso a las funciones de administración
   admin = int(input("Introduce 1 para sí, 0 para no: "))
if admin == 1:
    print("Bienvenido administrador puedes entrar")
else:
    contraseña = int(input("Escribe la contraseña para entrar:")) # El dueño de la casa de apuestas me pide que introduzca la contraseña para entrar a la sección de apuestas
if contraseña == 1234:
        print("Acceso concedido puedes apostar") # El dueño de la casa de apuestas me dice que la contraseña es incorrecta y no puedo entrar a la sección de apuestas
else:
        print("Contraseña incorrecta, no puedes entrar") # El dueño de la casa de apuestas me dice que la contraseña es incorrecta y no puedo entrar a la sección de apuestas
        