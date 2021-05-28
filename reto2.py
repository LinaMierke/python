edad = int(input(" Ingrese edad del estudiante: "))
salario = float(input("Ingrese su numero de salarios: "))
puntaje = float(input("Ingrese el puntaje: "))
valor_matricula = int(input("Ingrese el valor de la matricula: "))
descuento_edad = 0
descuento_salario = 0
descuento_puntaje = 0


if edad >= 15 and edad <= 18:
    descuento_edad = 0.25
    print("El descuento por edad es 25%")

elif edad >= 19 and edad <= 21:
    descuento_edad = 0.15
    print("El descuento por edad es 15%")

elif edad >= 22 and edad <= 25:
    descuento_edad = 0.10
    print("El descuento por edad es 10%")

else:
    print("El descuento por edad es 0%")


if salario <= 1:
    descuento_salario = 0.3
    print("Descuento por salario sera del 30%")
elif salario > 1 and salario <= 2:
    descuento_salario = 0.2
    print("Descuento por salario sera del 20%")
elif salario > 2 and salario <= 3:
    descuento_salario = 0.1
    print("Descuento por salario sera del 10%")
else:
    print("El descuento por salario es 0%")


if puntaje >= 80 and puntaje <= 85:
    descuento_puntaje = 0.3
    print("El descuento por puntaje es 30%")

elif puntaje >= 86 and puntaje <= 91:
    descuento_puntaje = 0.35
    print("El descuento por puntaje es 35%")

elif puntaje >= 92 and puntaje <= 95:
    descuento_puntaje = 0.4
    print("El descuento por puntaje es 40%")
elif puntaje >= 96:
    descuento_puntaje = 0.45
    print("El descuento por puntaje es 45%")
else:
    print("El descuento por puntaje es 0%")
