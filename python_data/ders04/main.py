import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# ilk 20 veride aynı olanların ortalamasını alıp aynen verisini yazdırıyoruz
veri = pd.read_csv("./ds_salaries.csv")
meslek = veri["job_title"].head(10) # ilk 10 meslek
# maas = veri["salary"].head(10) # en yüksek 10 maaş
maas = veri["salary"].tail(10) # en düşük 10 maaş

figure, eksen = plt.subplots()
eksen.bar(meslek, maas)
# eksen.barh(meslek, maas) # yatay grafik

plt.title("Meslek - MaaşGrafiği")
plt.xlabel("Meslek")
plt.ylabel("Maaş")

yas = np.random.randint(17, 45, 10)
kilo = np.random.randint(50, 100, 10)

plt.plot(yas, kilo, marker="*", color="red", linestyle="--")
plt.title("Yaş - Kilo Grafiği\nÇizgisel gösterim")
plt.xlabel("Yaş")
plt.ylabel("Kilo")
plt.show()