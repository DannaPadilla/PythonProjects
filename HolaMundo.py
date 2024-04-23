#operadores aritmeticos
'''
suma +
resta -
negacion -
multiplicacion *
potencia **
division /
division entera //
modulo %
'''
n1=7
n2=2
r=(5+9/3)**2
print(r)

#operadores relacionales
'''
== igual que
!= distinto que
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que
'''
r=(100>=100)
print (r)

#operadores logicos
'''
and  se cumple a y b
or  se cumple a o b
not  No a
'''
a=30
b=40
c=50
r= not ((a>b)or(b<c))
print (r)


#operadores de asignacion
'''
c+=1
'''
c=0
c+=10
c-=5
c*=3
c/=5
c**=3
c%=3
print (c)

#salida de datos
app= "flutter"
proyecto= "ComFlu"
print(f"Se hará en {app} se llamara {proyecto}")

#entrada de datos
cadena =float(input("¿Qué version es?:  "))
print (f"tu proyecto se llama {cadena+1}")
