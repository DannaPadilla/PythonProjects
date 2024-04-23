#concatenar cadenas de caracteres
# queremos crear una cadena que diga: aprende a programar con 
'''
organizacion="FreeCodeCamp"
print ("aprende a progranar con "+ organizacion)
print ("aprende a programar con {}".format(organizacion))
print (f"aprende a programar con {organizacion}")
'''
adj= input("Adjetivo: ")
verbo1= input("Verbo: ")
verbo2= input("Verbo: ")
sustantivo_plural= input("Sustantivo plural: ")
madlib=f"¡programar es tan {adj}!siempre me emociona porque me encanta {verbo1} problemas. ¡Aprende a {verbo2} con FreeCodeCamp y alcanza tus {sustantivo_plural}"
print (madlib)