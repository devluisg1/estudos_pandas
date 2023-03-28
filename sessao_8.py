import pandas as pd
import numpy as np

# Sumarizando dados
datas = pd.date_range('20220701', periods=6)
# print(datas)
columns = ['Var_A', 'Var_B', 'Var_C', 'Var_D']
df1 = pd.DataFrame(np.random.randn(6, 4), index=datas, columns=columns)
# print(df1)

"""print(df1.shape)
print(df1.dtypes)
print(df1.describe())"""

# print('==' * 20)

df2 = pd.DataFrame({
    'A': 1.,
    'B': pd.Timestamp('20130102'),
    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
    'D': np.array([3] * 4, dtype='int32'),
    'E': pd.Categorical(['test', 'train', 'test', 'train']),
    'F': 'Python'
    })
"""print(df2.shape)
print(df2.dtypes)
print(df2.describe())"""
# print('==' * 20)
df3 = df1.reindex(index=datas[0:4], columns=list(df1.columns) + ['Var_E'])
# print(df3)
df3.loc[datas[0]:datas[1], 'Var_E'] = 77
# print(df3)
# df3.loc[datas[1]:, 'Var_E'] = 77
# print(df3)

datas2 = pd.date_range('20190101', periods=60, freq='D')
df2_1 = pd.DataFrame(np.random.randn(60, 5), index=datas2, columns=list("ABCDE"))


df2_1['F'] = df2_1.A[df2_1.A > 0]
# print(df2_1.shape)

# df2_1 = df2_1.dropna()

df2_2 = df2_1.copy()
df2_2 = df2_2.F.fillna(np.mean(df2_2.A))
# df2_2 = df2_2.F.fillna(value=9999)
# print(df2_2)

# Dados únicos

df3_1 = pd.DataFrame({
    'A': 1.,
    'B': pd.Timestamp('20130102'),
    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
    'D': np.array([3] * 4, dtype='int32'),
    'E': pd.Categorical(['test', 'train', 'test', 'train']),
    'F': 'Python',
    'G': [2, 2, 4, 4],
    'H': [np.nan, 2, 4, np.nan]
    })
# print(df3_1)
"""print(df3_1.nunique(axis=1))
print(df3_1.nunique(axis=0))
print(df3_1.nunique(axis=0, dropna=True))
print(df3_1.nunique(axis=0, dropna=False))"""

# Removendo duplicatas

"""print(df3_1)
print('==' * 20)
print(df3_1.drop_duplicates(subset=['G']))
print('==' * 20)
print(df3_1.drop_duplicates(subset=['G'], keep='last'))
print('==' * 20)
print(df3_1.drop_duplicates(subset=['G'], keep=False))"""

# Ordenação dos dados

df4_1 = pd.DataFrame({
    'Col1': ['A', 'A', 'B', np.nan, 'D', 'C'],
    'Col2': [2, 1, 9, 8, 7, 4],
    'Col3': [0, 1, 9, 4, 2, 3]
})
"""print(df4_1)
print('==' * 20)
print(df4_1.sort_values(by='Col1'))
print('==' * 20)
print(df4_1.sort_values(by='Col2'))
print('==' * 20)
print(df4_1.sort_values(by=['Col3', 'Col1']))
print('==' * 20)
print(df4_1.sort_values(by='Col2', ascending=False))
print('==' * 20)
print(df4_1.sort_values(by='Col2', axis=0, ascending=False))
"""