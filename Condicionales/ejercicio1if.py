#ejercicio 1
n1= int (input("ingrese numero 1: "))
n2 = int (input("ingrese numero 2: "))

if n1%2==0 and n2%2==0:
    print("ambos son pares")
elif n1%2==0 and n2%2!=0:
    print(f" {n1} es par ")
elif n1%2!=0 and n2%2==0:
    print(f"{n2} es par")
else:
    print (f"ninguno de los dos numeros es par")

