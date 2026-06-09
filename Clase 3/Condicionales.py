#sistema de acceso para una persona que si tiene más de 18 años puede ingresar, si tiene entre 15 y 17 años puede ingresar con un adulto, y si tiene menos de 15 años no puede ingresar.
# Si es mayor de 18 años, puede ingresar.
edad = int(input("Ingresa tu edad: ")) # Esto es una variable con un int input para que el usuario ingrese su edadue el usuario ingrese su edad.
nombre = input("Ingresa tu nombre: ") # Esto es una variable con un input para que el usuario ingrese su nombre.

if edad >= 18:
    print("Hola :)", nombre + "," "puedes entrar al establecimiento.") # esto se va a ejecutar media vez la persona sea mayor de 18 años.
elif edad >= 15 and edad < 18: # esto es una condicional elif para que la persona pueda entrar con sus papás o con un adulto.
    print("Hola :)", nombre + "," "puedes entrar al establecimiento pero acompañado de un adulto.") # esto se va a ejecutar media vez la persona sea mayor de 15 años y menor de 18 años.
else: # esto es una condicional else para que la persona no pueda entrar al establecimiento.
    print("Hola :)", nombre + "," "lo lamento mucho :(, no puedes entrar al establecimiento.") # esto se va a ejecutar media vez la persona sea menor de 15 años.
