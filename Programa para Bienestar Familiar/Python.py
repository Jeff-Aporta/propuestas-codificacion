""" 
Crear un programa para el bienestar familiar, que permita evaluar la estatura 
de n niños en centímetros, no debe permitir por obvias razones un valor negativo. 

El programa debe mostrar lo siguiente: 
1) Promedio de estatura en cm de todo el grupo
2) la estatura más alta del salón
3) si el promedio es mayor a 150 cm debe salir un mensaje
   "Son aptos para participar en basket"
"""

print("Bienvenido al programa para el bienestar familiar")
print()
cantidad_niños = 0

while True:
    try:
        cantidad_niños = int(input("Ingrese la cantidad de niños: "))
    except:
        print("el dato ingresado no es un entero")
        continue
    if(cantidad_niños <= 0):
        print("ingrese una cantidad natural (no nula) de niños")
        continue
    break

sumaEstatura = 0
estatura_max = 0
for i in range(cantidad_niños):
    estatura = 0
    while True:
        try:
            estatura = int(
                input("Ingrese una altura para el niño " + str(i+1) + " (en cm): ")
            )
        except:
            print("el dato ingresado no es un entero")
            continue
        if(estatura <= 0):
            print("ingrese una cantidad natural (no nula) para la altura (en cm)")
            continue
        break
    sumaEstatura += estatura
    if(estatura > estatura_max):
        estatura_max = estatura

promedio_estatura = sumaEstatura/cantidad_niños
print()
print("1) Promedio de estaturas del grupo: ", promedio_estatura,"cm")
print("2) estatura máxima en el grupo: ", estatura_max,"cm")
print()
if(promedio_estatura>150):
    print("3) Son aptos para participar en basket")
else:
    print("3) No son aptos para participar en basket")
print()
