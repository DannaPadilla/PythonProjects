#ejercicio 4
saldo=2000
print ("1. ingresar de dinero")
print ("2. retirar de dinero")
print ("3. mostrar de dinero")
print ("4. salir")

seleccion = int (input("seleccione una opcion: "))

if seleccion==1:
    valornuevo=float (input("digite el valor a ingresar: "))
    saldo= saldo+valornuevo
    print (f"nuevo saldo: {saldo}")
elif seleccion==2:
    valorretirar=float (input("digite el valor a retirar: "))
    if valorretirar>saldo:
        print("saldo insuficiente")
    else: 
        saldo=saldo-valorretirar
        print(f"nuevo saldo disponible: {saldo}")
elif seleccion==3:
    print(f"saldo disponible: {saldo}")
elif seleccion==4:
    print("fin")
else:
    print("error de entrada de datos")