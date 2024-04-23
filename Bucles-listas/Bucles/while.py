#while (mientras que)
import math
numero=int (input("escriba un numero: "))
while numero<0:
    print("por favor ingrese un numero positivo")
    numero=int (input("escriba un numero: "))
print(f"el resultado de la raiz cuadrada es: {math.sqrt(numero):.2f}")