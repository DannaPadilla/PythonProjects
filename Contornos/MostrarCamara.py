import cv2
CapturarVideo= cv2.VideoCapture(0)
if not CapturarVideo.isOpened():
    print ("no se encontró una camara")
    exit()

while True:
    _,Camara =CapturarVideo.read()
    grisis=cv2.cvtColor(Camara,cv2.COLOR_BGR2GRAY)
    cv2.imshow("En vivo", grisis)
    if cv2.waitKey(1)==ord("q"):
        break

CapturarVideo.release()
cv2.destroyAllWindows()