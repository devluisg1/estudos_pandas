import pandas as pd
import numpy as np

# Seleção de linhas e colunas 1 – 2

datas = pd.date_range('20200101', periods=600, freq='D')
# print(datas)

df1 = pd.DataFrame(np.random.rand(600, 5), index=datas, columns=list('ABCDE'))
# print(df1)

# print(df1['D'])
# print(df1[1: 4])  # Slicing

#  print(df1.loc[:, ['A', 'B', 'C']])

# print(df1.loc['20200101': '20200701'])  # Selecionando através das datas | Selecionando todas as colunas

# print(df1.loc['20200101': '20200701'], ['A', 'B', 'C'])  # Selecionando através das datas |
# Selecionando algumas colunas


# Seleção de linhas e colunas 2 – 2

# print(df1.iloc[0])
# print(df1.iloc[1: 5, 0: 3])

# print(df1.iloc[[1, 5, 6], [0, 3]])
# print(df1.iloc[1:10, :])

# Filtros booleanos

print(df1[df1.A > 0])
print(df1[df1 > 0])
