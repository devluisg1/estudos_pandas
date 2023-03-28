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

# Dados em gráficos - Histogramas
# pd.set_option('display.max_columns', None)
# pd.reset_option("^display")

df_titanic = pd.read_csv(r'Repository/titanic_train.csv')
plt.rcParams['figure.figsize'] = (15, 7)

print(df_titanic)
df_titanic.Age.hist()
plt.show()

