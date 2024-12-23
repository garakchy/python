import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# takımların kazandıkları madalya türü ve sayısını bulalım
# Example data for veri
veri = pd.DataFrame({
	"takim": ["Team A", "Team B", "Team C", "Team D"],
	"madalya_Gold": [1, 2, 3, 4],
	"madalya_Silver": [2, 1, 4, 3],
	"madalya_Bronze": [3, 4, 1, 2]
})

mydata = veri[["takim", "madalya_Gold", "madalya_Silver", "madalya_Bronze"]].groupby(["takim"]).sum().sort_values(by="madalya_Gold", ascending=False)
              
print(mydata.head(10))

import seaborn as sns

def boy_kilo_sacilim():
    sns.scatterplot(data=veri, x="boy", y="kilo", hue="madalya", alpha=0.3)
    plt.title("boy-kilo dağilimi")
    plt.show()

boy_kilo_sacilim()