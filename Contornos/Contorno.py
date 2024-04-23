import cv2

imagen= cv2.imread('Contornos\contorno.jpg')
grises= cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)#para convertirlo a escala de grises

#threshold (src es imagen)
_,umbral= cv2.threshold(grises,128,255,cv2.THRESH_BINARY)
#findcontours
contorno, jerarquia = cv2.findContours(umbral, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
#dibujar contornos
cv2.drawContours(imagen, contorno,-1,(0,0,255),3)
#mostrar
cv2.imshow('Imagen original',imagen)
cv2.imshow('Imagen grises',grises)
cv2.imshow("Imagen Umbral", umbral)
cv2.waitKey(0) # 0 para mantenerlo estatico, 1 se usa para videos o reconocimiento facial
cv2.destroyAllWindows() #destruir todas las ventanas que esten abiertas









