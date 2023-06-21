datos=open('datos.csv','r')
total=0
años={}
_=datos.readline()
menor=0
mayor=0
cont=0
for linea in datos.readlines():
    totalaño=0
    promedios=[]
    lista=[]
    datos_separados = linea.split(";")
    for x in datos_separados:
        num=int(x)
        lista.append(num)
    año,tr1,tr2,tr3,tr4=lista
    if año>=mayor:
        mayor=año
    else:
        menor=año
    totalaño=tr1+tr2+tr3+tr4
    promedios=[totalaño,totalaño/4]
    años[año]=promedios
    total+=(tr1+tr2+tr3+tr4)
    cont+=1
while True:
    print("Menu opciones: ")
    print("1--> Mostrar la lista completa")
    print("2--> Mostrar la lista total/promedio completa")
    print("3--> Buscar un año en la lista")
    print("4--> Mostrar el total")
    print("5--> SALIR\n")
    opcion=int(input("Ingrese la opcion: "))
    if opcion==1:
        datos=open('datos.csv','r')
        texto=datos.read()
        print(f'{texto}\n')
        datos.close()
    elif opcion==2:
        print(f'Año-Total-Promedio')
        for x,y in años.items():
            print(f'{x}: {y}')
        print("\n")
    elif opcion==3:
        datos=open('datos.csv','r')
        busaño=input("Ingrese el año: ")
        busañoint=int(busaño)
        c=0
        for x in datos.readlines():
            if busaño in x:
                c+=1
                linea=x.split(";")
                listatmp=años[busañoint]
                print(f'Año: {linea[0]}')
                print(f'Trimestre 1: {linea[1]}')
                print(f'Trimestre 2: {linea[2]}')
                print(f'Trimestre 3: {linea[3]}')
                print(f'Trimestre 4: {linea[4]}')
                print(f'Total: {listatmp[0]}')
                print(f'Promedio: {listatmp[1]}')
        if c==0:
            print(f'El año {busaño} no se encuentra registrado en la lista')
        datos.close()
        print("\n")
    elif opcion==4:
        print(f'El total desde {menor} hasta {mayor} es: {total}\n')
        print(f'El promedio por año desde {menor} hasta {mayor} es: {total/cont}\n')
    elif opcion==5:
        break
    else:
        print("Opcion incorrecta\n")
datos.close()