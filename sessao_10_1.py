import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
Solarize_Light2
_classic_test_patch
_mpl-gallery
_mpl-gallery-nogrid
bmh
classic
dark_background
fast
fivethirtyeight
ggplot
grayscale
seaborn-v0_8
seaborn-v0_8-bright
seaborn-v0_8-colorblind
seaborn-v0_8-dark
seaborn-v0_8-dark-palette
seaborn-v0_8-darkgrid
seaborn-v0_8-deep
seaborn-v0_8-muted
seaborn-v0_8-notebook
seaborn-v0_8-paper
seaborn-v0_8-pastel
seaborn-v0_8-poster
seaborn-v0_8-talk
seaborn-v0_8-ticks
seaborn-v0_8-white
seaborn-v0_8-whitegrid
tableau-colorblind10
"""

#  Estilos de plotagens com Pandas - Linha
# for x in plt.style.available:
#    print(x)

# plt.style.use()

plt.rcParams['figure.figsize'] = (25, 7)
df_titanic = pd.read_csv(r'Repository/titanic_train.csv')
print(df_titanic)
print(df_titanic.shape)

# print(df_titanic.query('Age >= 32 and Age <= 45'))


plt.plot(df_titanic.Age, '*-g')

# Dados em gráficos — Linhas

plt.title("Passageiros / Idade Titanic")
plt.xlabel("Passageiro", size=14)
plt.ylabel("Idade", size=14)
plt.show()

df_titanic.Age.plot()
df_titanic.plot()
plt.show()
