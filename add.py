n = int(input("ingrese cuantos numeros sumara?"))
total = n
suma = 0
while total > 0:
    numero = int(input("ingrese numero a sumar: "))
    suma = suma + numero
    total = total - 1
print("la suma de los ", str(n), "numero es: ", str(suma))
