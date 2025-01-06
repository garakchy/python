# dışarıdan girilen değere göre resim dosyasını boyutlandırma

import cv2
genislik = int(input("Genişlik değeri giriniz: "))
yukseklik = int(input("Yükseklik değeri giriniz: "))

x, y = 800, 600

resim1 = cv2.imread("./resim1.jpg")
# resmin gir tonlu olması daha az pikseli kapsadığı için gri tonlu yapılır
# görserli okuma işleminde blue, green, red değerleri okunur
gri_resim = cv2.cvtColor(resim1, cv2.COLOR_BGR2GRAY)
