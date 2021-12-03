""" 
Construye un programa que, al recibir como datos el peso, la altura 
y el género de N personas que pertenecen a un estado de un país, 
obtenga el promedio del peso y el promedio de la altura, tanto de la 
población masculina como de la femenina.
"""

print()
print("Bienvenido.")
print()


def capturarNumero(mensaje, entero=False):
    retorno = -1
    while True:
        try:
            if entero:
                retorno = int(input(mensaje))
            else:
                retorno = float(input(mensaje))
        except:
            print("El dato ingresado no es un número")
            continue
        if(retorno < 1):
            print("El número debe ser mayor a 0")
            continue
        break
    return retorno


sumatorias = {
    "Masculino": {
        "Peso": 0,
        "Altura": 0,
        "Poblacion": 0
    },
    "Femenino": {
        "Peso": 0,
        "Altura": 0,
        "Poblacion": 0
    }
}

cantidadPersonas = capturarNumero("Ingrese la cantidad de personas: ", True)

for i in range(cantidadPersonas):
    index = i+1
    altura = capturarNumero(
        "Ingrese la altura de la persona " + str(index) + ": "
    )
    peso = capturarNumero(
        "Ingrese la peso de la persona " + str(index) + ": "
    )
    genero = ""
    while genero != "m" and genero != "f":
        genero = input(
            "Ingrese el género de la persona " + str(index) + " (M o F): "
        ).lower()
    print()
    bancoSumatoria = None

    if(genero == "m"):
        bancoSumatoria = sumatorias["Masculino"]
    elif(genero == "f"):
        bancoSumatoria = sumatorias["Femenino"]

    bancoSumatoria["Peso"] += peso
    bancoSumatoria["Altura"] += altura
    bancoSumatoria["Poblacion"] += 1


bancoMasculino = sumatorias["Masculino"]
bancoFemenino = sumatorias["Femenino"]

print()
print("Resumenes")
print()
if(bancoMasculino["Poblacion"]):
    print("Datos Masculinos (", bancoMasculino["Poblacion"], ")")
    print(
        "Promedio Peso: ", bancoMasculino["Peso"]/bancoMasculino["Poblacion"]
    )
    print(
        "Promedio Altura: ", bancoMasculino["Altura"]/bancoMasculino["Poblacion"]
    )
    print()
if(bancoFemenino["Poblacion"]):
    print("Datos Femeninos (", bancoFemenino["Poblacion"], ")")
    print(
        "Promedio Peso: ", bancoFemenino["Peso"]/bancoFemenino["Poblacion"]
    )
    print(
        "Promedio Altura: ", bancoFemenino["Altura"]/bancoFemenino["Poblacion"]
    )
