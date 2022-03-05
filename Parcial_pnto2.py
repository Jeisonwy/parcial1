import msvcrt

print("****CALCULADORA DE INTERSECCION DE RECTA****")
n=1
pendientes = []
cortes = []

while n < 3 and n>=0:
    print("****** Recta ",n,"******")
    pendiente = float(input("Ingrese la pendiente recta "))
    corte = float(input("Ingrese el punto corte de recta "))

    
    pendientes.append(pendiente)
    cortes.append(corte)
    n=n+1

if pendientes[0] == pendientes[1]:
    print("Estas rectas no se interceptan")
else:
    operacion1 = pendientes[0] + pendientes[1]*-1
    operacion2 = cortes[1] + cortes[0]*-1
    operacion3 = operacion2/operacion1
    operacion4 = pendientes[0]*operacion3+cortes[0]


    print("El punto de intersección de las rectas X,Y es (",operacion3,",",operacion4,")\n\n")



msvcrt.getch
