#conjuntos
A={1,2,3,4}
B={2,3,5,6}
C={3,4,6,7}

#igualar los conjuntos, arroja true o false, sin importar el orden
print(A==B)
#union de conjuntos (no muestra los datos repetidos)
print(A|B)
print(A|C)
#interseccion de conjuntos (para mirar que numeros tienen en comun los conjuntos)
print(A&B)
print(A&C)
print(B&C)
#diferencia de conjuntos (que valores tiene a que no tiene b)
print(A-B)
#diferencia simétrica (elementos que pertenezcan a ambos pero con la interseccion fuera)
print(A^B)
print(B^C)
