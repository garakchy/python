# görsel üzerinden yazım ve şekil çizme

import cv2

foto = cv2.imread("./yazi2.png")
# https://docs.opencv.org/4.x/dc/da5/tutorial_py_drawing_functions.html
# ekranda düz çizgi oluşturmak
# cv2.line(resim, başlangıç noktası, bitiş noktası, renk, kalınlık)

cv2.line(foto, (100, 100), (300, 100), (0, 0, 255), 5)
cv2.circle(foto, (200, 200), 50, (200, 200, 200), -1) # içi dolu olsun
cv2.rectangle(foto, (200, 300), (250, 350), (50, 50, 50), 3)

# yazı karakterleri işlemleri
yaziailesi = cv2.FONT_HERSHEY_PLAIN
cv2.putText(foto, "Merhaba", (200, 100), yaziailesi, 2, (255, 255, 255), 2)
# cv2.putText(resim, yazı, (x, y), yazıtipi, boyut, renk, kalınlık)
# font_size, ondalık olabilir

cv2.imshow("Cizgi1", foto)

if (cv2.waitKey(0) & 0xFF == ord("q")):
    cv2.destroyAllWindows()
    exit()
