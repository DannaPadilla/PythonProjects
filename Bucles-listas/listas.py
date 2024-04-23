#introduccion a listas
array= ["futbol", "pc","pc", 18.6,18, [6,7,8,10.4],True,False]
print(array[2:7]) 
#funciones en listas

#funcion para ver la cantidad de datos en la lista
print(len(array))

#funcion para agregar un dato a la lista por codigo, se ubica por defecto al final de la lista
array.append(66)
array.append(True)

#funcion para insertar datos y elegir la posicion(posicion, dato)
array.insert(1,88)

#funcion para agregar datos al final de la lista en bloque
array.extend([1,88,True,100])

print(array) 

#concatenar listas
array1=["futbol", "pc", 18.6,18, [6,7,8,10.4],True,False]
array2=[200,250,"hola"]
array3=array1+array2
print(array3) 

#buscar un valor determinado dentro de la lista (true si se encuentra, false si no esta)
print("pc" in array)
#para saber la ubicacion del dato buscado
print(array.index("pc"))

#cantidad de veces que se repite un dato en la lista
print (array.count(True))

#eliminar datos de la lista
array.remove(True)

#clear para limpiar

#cambiar la posicion de los datos
array.reverse()

#ordenar los datos de forma ascendente
array=[1,2,8,-11,5]
array.sort()

#ordenar de forma descendente
array.sort(reverse=True)
print(array)


