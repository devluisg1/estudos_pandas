import pandas as pd
import numpy as np

series = pd.Series([7, 4, np.nan, 8, 6])
# print(series)

# Sessão 3
type(series)
# 1 - 3
datas = pd.date_range('20180506', periods=6, freq='M')
# print(datas)

df = pd.DataFrame(np.random.randn(6, 4), index=datas, columns=list('ABCD'))
# print(df)

# 2 - 3
df2 = pd.DataFrame(
    {'A': 7,
     'B': pd.Timestamp('20190101'),
     'C': pd.Series(1, index=list(range(4)), dtype='float32'),
     'D': np.array([3] * 4, dtype='int32'),
     'E': pd.Categorical(["test", "train", "test", "train"]),
     'F': "Python"
     })
# print(df2)

# 3 - 3

datas1 = pd.date_range('20180506', periods=600, freq='D')
df3 = pd.DataFrame(np.random.randn(600, 5), index=datas1, columns=list("ABCDE"))

df3['F'] = 1
df3['G'] = range(600)

# Multiplicando uma coluna com outra
df3['Produto'] = df3['A'] * df3['B']

# print(df3)

# DataFrame Visualization

"""print(df3.head())
print("===")
print(df3.tail())
print(df3.columns)
print(df3.index)"""

# print(df3.to_numpy())

# print(df3.T)  # transpor de linha para colunas

# DataFrame Combination 1 - 2

df1_1 = pd.DataFrame({
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3'],
    'C': ['C0', 'C1', 'C2', 'C3']},
    index=list(range(4))
)

df1_2 = pd.DataFrame({
    'A': ['A4', 'A5', 'A6', 'A7'],
    'B': ['B4', 'B5', 'B6', 'B7'],
    'C': ['C4', 'C5', 'C6', 'C7']},
    index=list(range(4, 8))
)

df1_3 = pd.DataFrame({
    'A': ['A8', 'A9', 'A10', 'A11'],
    'B': ['B8', 'B9', 'B10', 'B11'],
    'C': ['C8', 'C9', 'C10', 'C11']},
    index=list(range(8, 12))
)

print(df1_1)