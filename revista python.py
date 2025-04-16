##.................. SEGUNDO TRABAJO ................... ##
## el director de una revista para adultos me contacta para realizar la interfas de bienvenida de su pagina web 
# lo primero que se le pregunta al usuario , lo segundo es su clave de no tener cuenta deberia de registrarse
# y la edad añadir condiccion que le diga al usuario y es menor de 18 chao pescao si es mayor de 18 se le da la bienvenida y se registra el usuario se valida la clave y usuario#

print("Bienvenido")
usuario=input("Usted se encuentra registrado (SI/NO)")

if usuario == "no":
    nombre=input("Por favor , Ingrese su usuario:  ") 
    contra=input("Por favor , Ingrese su contraseña:  ")
    edad1=input("Por favor , Ingrese su edad :")

else:
    nombre=input("Ingrese su usuario: ")
    contra=input("Ingrese su contraseña: ")
    edad1=input("Ingrese su edad: ")



edad1=18

if edad1 >= 18:
    print("Usted es mayor de edad")
else:
    print("Usted es menor de edad , no puede Ingresar")





print("Hola",nombre,"****🥵 ¡¡ Bienvenido a monascoxinas ¡¡ 🥵**** : ")