def crear(nombre):
    file = open(nombre, 'w')
    file.close()


def agregar(archivo):
    print("Digite la información del beneficiario a agregar:")


n_a = input()
ced = input()
cel = input()
file = open(archivo, 'r')
lista = file.readlines()
file.close()
if ced+'\n' in lista:
    print("La cédula digitada ya se encuentra registrada")
else:
    file = open(archivo, 'a')
file.write(n_a+'\n')
file.write(ced+'\n')
file.write(cel+'\n')
file.close()
print("El beneficiario ha sido agregado")


def buscar_cel(archivo):
    print("Digite el nombre y apellido del beneficiario a buscar:")
    nom_ap = input().title()
    file = open(archivo, 'r')
    lista = file.readlines()
    file.close()
    lista2 = [i.title() for i in lista]
    if nom_ap+'\n' in lista2:
        print(lista[lista.index(nom_ap+'\n')+0].strip())
        print(lista[lista.index(nom_ap+'\n')+1].strip())
        print(lista[lista.index(nom_ap+'\n')+2].strip())
    else:
        print("el nombre digitado no se encuentra registrado")


def borrar(archivo):
    print("Digite la cedula del beneficiario a borrar:")
    ced = input()
    file = open(archivo, 'r')
    lista = file.readlines()
    file.close()
    if ced+'\n' in lista:
        pos = lista.index(ced+'\n')-1
        for i in range(3):
            lista.pop(pos)
        file = open(archivo, 'w')
        for i in lista:
        file.write(i)
        file.close()
        print("El usuario ha sido eliminado del listado")
    else:
        print("La cedula digitada no esta registrada")


def mostrar_total(archivo):
    print("Listado de beneficiarios")
    file = open(archivo, 'r')
    lista = file.readlines()
    file.close()
    for i in lista:
        print(i.strip())


def mostrarxletra(archivo):
    letra = input(
        "Digite la letra por la que empiezan los beneficiarios:").title()
    file = open(archivo, 'r')


lista = file.readlines()
file.close()
print("Listado filtrado de beneficiarios:")
for i in lista:
    if i.title().startswith(letra):
        print(i.strip())
        print(lista[lista.index(i)+1].strip())
        print(lista[lista.index(i)+2].strip())


a = "lina_create.txt" crear(a)
