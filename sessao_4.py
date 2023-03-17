import pandas as pd
import numpy as np

# Merge de dados  Sintaxe 1-5

cadastro_a = {'Id': ['AA2930', 'BB4563', 'CC2139', 'DE2521', 'GT3462', 'HH1158'],
              'Nome': ['Victor', 'Amanda', 'Bruna', 'Carlos', 'Ricardo', 'Maria'],
              'Idade': [20, 35, 40, 54, 30, 27],
              'CEP': ['00092-029', '11111-111', '22222-888', '00000-999', '88888-111', '77777-666']
              }
cadastro_a = pd.DataFrame(cadastro_a, columns=['Id', 'Nome', 'Idade', 'CEP'])

# print(cadastro_a)

print("=" * 25)

cadastro_b = {'Id': ['CC9999', 'EF4488', 'DD9999', 'GT3462', 'HH1158'],
              'Nome': ['Marcos', 'Patricia', 'Ericka', 'Ricardo', 'Maria'],
              'Idade': [19, 30, 22, 30, 27],
              'CEP': ['00092-029', '11111-111', '11111-888', '88888-111', '77777-666']
              }
cadastro_b = pd.DataFrame(cadastro_b, columns=['Id', 'Nome', 'Idade', 'CEP'])


compras = {'Id': ['AA2930', 'EF4488', 'CC2139', 'EF4488', 'CC9999', 'AA2930', 'HH1158', 'HH1158'],
           'Data': ['2019-01-01', '2019-01-30', '2019-01-30', '2019-02-01', '2019-02-20', '2019-03-15', '2019-04-01',
                    '2019-04-10'],
           'Valor': [200, 100, 40, 150, 300, 25, 50, 500]
           }
compras = pd.DataFrame(compras, columns=['Id', 'Data', 'Valor'])
# print(compras)
# print(cadastro_b)

print("=" * 25)

# Merge de dados — INNER JOIN 2 – 5

# print(pd.merge(cadastro_a, cadastro_b, on=['Id'], how='inner'))

# print(pd.merge(cadastro_a, cadastro_b[['Id', 'Idade', 'CEP']], on=['Id'], how='inner', suffixes=('_A', '_B')))


"""print(pd.merge(cadastro_a[['Id', 'Idade', 'CEP']], cadastro_b[['Id', 'Idade', 'CEP']],
               on=['Id'], how='inner', suffixes=('_A', '_B')))"""

# Merge de dados — FULL JOIN 3 – 5

lojas = pd.concat([cadastro_a, cadastro_b], ignore_index=True)
# print(lojas)

lojas = lojas.drop_duplicates(subset='Id')
# print(lojas)

# Merge de dados — LEFT JOIN 4 – 5


esquerda = pd.merge(cadastro_a, compras, on=['Id'], how='left')

inner = pd.merge(cadastro_a, compras, on=['Id'], how='inner')

# print(inner.groupby(['Id', 'Nome'])['Valor'].sum())

# print(esquerda.groupby(['Id', 'Nome'])['Valor'].sum())

# Merge de dados — OTHER 5 – 5

outer = pd.merge(cadastro_a, cadastro_b, on=['Id'], how='outer', indicator=True)
# print(outer)

# Uso do groupby

df = pd.DataFrame({
    "A": ['Verdadeiro', 'Falso', 'Verdadeiro', 'Falso', 'Verdadeiro', 'Falso',
          'Verdadeiro', 'Falso'],
    "B": ['Um', 'Um', 'Dois', 'Tres', 'Dois', 'Dois', 'Um', 'Tres'],
    "C": np.random.randn(8),
    "D": np.random.randn(8)
})

verdadeiro = df.groupby(['A']).sum(True)
print(verdadeiro)
print("===" * 20)

um_dois = df.groupby(['B']).sum(True)
print(um_dois)
print("===" * 20)

both_group = df.groupby(['A', 'B']).sum(True)
print(both_group)
