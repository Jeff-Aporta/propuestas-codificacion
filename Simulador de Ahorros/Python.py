""" 
Crear un simulador de ahorros para un banco, el cuál permite ingresar
mensualmente un monto por año (12 meses).

No debe permitir ingresar cantidades negativas

El programa debe mostrar:
1) El valor total ahorrado
2) El promedio de ahorro por mes
3) Si ahorra más de 12 millones al año, se le da una utilidad de 1%
"""

print("Hola, bienvenido al simulador de ahorros")
print()
totalAhorrado = 0
for m in range(12):
    monto = 0
    while True:
        try:
            monto = float(
                input("Ingrese el monto del mes " + str(m+1) + ": ")
            )
        except:
            print("La cantidad ingresada no es un número, vuelva a intentarlo")
            continue
        if(monto < 0):
            print("Los montos no pueden ser negativos")
            continue
        break
    totalAhorrado += monto

utilidadExtra = 0
if(totalAhorrado > 12000000):
    utilidadExtra = 0.01*totalAhorrado
print()
print("1) Total ahorrado: ", totalAhorrado)
print("2) Promedio mensual ahorrado: ", totalAhorrado/12)
print("3) Utilidad extra: ", utilidadExtra)
print("4) Total: ", totalAhorrado + utilidadExtra)
print()

""" 
Jeff Aporta (2021 - Colombia)
Video solución
https://youtu.be/s3TKA8c6Yh4

Aquí les dejo
mi canal de YouTube
https://www.youtube.com/c/JeffAportaa
Mi canal de Telegram
https://t.me/canalAporta

Cualquier pregunta, no dudes en escribirme
Whatsapp:
https://wa.link/1tmqmt
Telegram:
https://t.me/jeffAporta
"""
