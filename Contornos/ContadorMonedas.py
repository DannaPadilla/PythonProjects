import cv2
import numpy as np # libreria principal de Python, permite trabajar con informatica cientifica, matrices, 
#desenfoque de Gauss
valorGauss=3
valorKernel=3
original= cv2.imread('Contornos/monedassoles.jpg')
gris=cv2.cvtColor(original,cv2.COLOR_BGR2GRAY)
#eliminacion de ruidos 1 con gauss
gauss=cv2.GaussianBlur(gris, (valorGauss,valorGauss), 0)
#eliminacion de ruidos 2 con Canny
canny= cv2.Canny(gauss,60,100)
#para indicarle que contorno quiero mostrar
kernel= np.ones((valorKernel,valorKernel), np.uint8)
#aplicamos clausura porque el ruido esta dentro de la figura
cierre= cv2.morphologyEx(canny, cv2.MORPH_CLOSE, kernel)
contornos, jerarquia= cv2.findContours(cierre.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("monedas encontradas: {}", format(len(contornos)))
cv2.drawContours(original,contornos,-1, (0,0,255),2)
#mostrar resultados
cv2.imshow("Grises",gris)
cv2.imshow("Gauss",gauss)
cv2.imshow("Canny",canny)
cv2.imshow("Cierre",cierre)
cv2.imshow("Resultado",original)
cv2.waitKey(0)


