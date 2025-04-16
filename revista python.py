##.................. SEGUNDO TRABAJO ................... ##
## el director de una revista para adultos me contacta para realizar la interfas de bienvenida de su pagina web 
# lo primero que se le pregunta al usuario , lo segundo es su clave de no tener cuenta deberia de registrarse
# y la edad añadir condiccion que le diga al usuario y es menor de 18 chao pescao si es mayor de 18 se le da la bienvenida y se registra el usuario se valida la clave y usuario#

print("Bienvenido")
usuario = input("Usted se encuentra registrado (SI/NO): ").strip().lower()

if usuario == "no":
    nombre = input("Por favor, ingrese su usuario: ")
    contra = input("Por favor, ingrese su contraseña: ")
    edad1 = int(input("Por favor, ingrese su edad: "))
else:
    nombre = input("Ingrese su usuario: ")
    contra = input("Ingrese su contraseña: ")
    edad1 = int(input("Ingrese su edad: "))

if edad1 >= 18:
    print("Usted es mayor de edad")
    print(f"Hola {nombre}, ****🥵 ¡¡ Bienvenido a monascoxinas ¡¡ 🥵****")
else:
    print("Usted es menor de edad, no puede ingresar. Chao pescao.")