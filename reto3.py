dias = int(input("Cuantos dias duro la salida? "))
temperatura_maxima = []
temperatura_minima = []
temperatura_error = []
while dias > 0:
    tmax = float(input("ingrese temperatura maxima: "))
    tmin = float(input("ingrese la temperatura minima: "))
    if tmax == 0 and tmin == 0:
        break
    # if (tmax < 35 and tmin < 35) or (tmin > 5 and tmax > 5):
    #   temperatura_maxima.append(tmax)
    #   temperatura_minima.append(tmin)
    # else:
    #   temperatura_error.append([tmax,tmin,dias])

    if tmax > 35 or tmax < 5:
        temperatura_error.append([dias, tmax])
    else:
        temperatura_maxima.append(tmax)
    if tmin < 5 or tmin > 35:
        temperatura_error.append([dias, tmin])
    else:
        temperatura_minima.append(tmin)

    if (tmax > 35 or tmin < 35) or (tmin < 5 or tmax < 5):
        temperatura_error.append([dias, tmin])
    else:
        print("hi")
    dias = dias - 1
print("temperatura maxima ", temperatura_maxima)
print("temperatura minima ", temperatura_minima)
print("temperatura error ", temperatura_error)
if tmax != 0 and tmin != 0:
    print("El promedio de la temperatura maxima es: ",
          sum(temperatura_maxima)/len(temperatura_maxima))
    print("El promedio de la temperatura minima es: ",
          sum(temperatura_minima)/len(temperatura_minima))
