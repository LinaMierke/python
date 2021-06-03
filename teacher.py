respuesta = "si"
while respuesta == "si":
    input("Ingrese el nombre del docente: ")
    horas = int(input("Ingrese las horas trabajadas: "))
    precio_hora = float(input("Ingrese el valor de horas: "))

    def horas_extra():
        if horas > 40:
            horas_extras = horas-40
        return horas_extras

    def sueldo_bruto():
        salbruto = (precio_hora*(horas-horas_extra())) + \
            (horas_extra()*(precio_hora*1.5))
        return salbruto

    def parafiscales():
        parafiscales2 = (sueldo_bruto()*9)/100
        return parafiscales2

    def primaYcesantias():
        pim_cesan = (sueldo_bruto()*8.33)/100
        return pim_cesan

    def interes_cesantias():
        inte_cesant = (primaYcesantias())/100
        return inte_cesant

    def vacaciones():
        vacas = (sueldo_bruto()*4.17)/100
        return vacas

    salud_pension = (sueldo_bruto()*4)/100

    def descuento():
        desc = (salud_pension*2) + parafiscales()
        return desc

    def provisiones():
        prov = (2*primaYcesantias())+vacaciones()+interes_cesantias()
        return prov

    def salario_neto():
        sal_net = sueldo_bruto()-descuento()
        return sal_net

    print("Horas extra: ", horas_extra())
    print("Salario bruto: ", sueldo_bruto())
    print("Parafiscales: ", parafiscales())
    print("Prima: ", primaYcesantias())
    print("Cesantias: ", primaYcesantias())
    print("Interes de cesantias: ", interes_cesantias())
    print("Vacaciones: ", vacaciones())
    print("Salud: ", salud_pension)
    print("Pension: ", salud_pension)
    print("Descuento: ", descuento())
    print("Provisiones: ", provisiones())
    print("Salario Neto a Pagar: ", salario_neto())
    respuesta = str(input("Desea ingresaro datos de docente? si o no: "))
