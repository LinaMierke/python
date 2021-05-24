a = int(input("ingrese el primer numero: "))
b = int(input("ingrese el segundo numero: "))
print("Estas son las opciones son: 1 suma, 2 resta, 3 division, 4 multiplicacion, 5 residuo, 6 elevado ")
option = int(input(" Elija una de las opciones: "))
suma = a + b
resta = a - b
division = a / b
multiplicacion = a * b
residuo = a % b
elevado = a ** b

while option == 1:
    print("La suma es: ", suma)
    break
while option == 2:
    print("La resta es: ", resta)
    break
while option == 3:
    print("La division es: ", division)
    break
while option == 4:
    print("La multiplicacion es: ", multiplicacion)
    break
while option == 5:
    print("El residuo es: ", residuo)
    break
while option == 6:
    print("El resultado de exponente es: ", elevado)
    break

pregunta = input("Desea ingresar otra option? si o no ")
