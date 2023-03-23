import pandas as pd
import numpy as np

# Reshaping dados

datas = pd.date_range('20200101', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=datas, columns=['Var_A', 'Var_B', 'Var_C', 'Var_D'])

dft = df.T

"""print(dft)

print(dft.shape)
print(df.shape)"""

values = dft.values
# print(values.size)
values = values.reshape(2, 12)  # Lembre que o reshape tem que ser em uma estrutura múltipla do tamanho origial
# print(values)

# Função pivot()

dias = pd.date_range(start='20190101', periods=12)

# print(dias)

pessoas = ['George', 'Victor', 'Lucas']

np.random.choice(pessoas)

nomes = []
gastos = []

for i in range(12):
    nomes.append(np.random.choice(pessoas))
    gastos.append(round(np.random.rand() * 100, 2))

# print(nome)
# print(gasto)
df_aula2 = pd.DataFrame({'Dia': dias,
                         'Pessoa': nomes,
                         'Gasto': gastos
                         })

# print(df_aula2)
# print(df_aula2.pivot(index='Dia', columns='Pessoa', values='Gasto'))

# Função pivot_table()

carros = [7, 4, 3, 2, 8]
dias_aula3 = pd.date_range('20190101', '20190101', periods=5)
vendedor = ['George', 'Vagner', 'Pedro', 'Vagner', 'George']

df_aula3 = pd.DataFrame({
    'Dia': dias_aula3,
    'Qtd_Carros': carros,
    'Vendedor': vendedor
})
# print(df_aula3)
# print(df_aula3.pivot_table(index='Dia', columns='Vendedor', values='Qtd_Carros'))
# print(pd.pivot_table(df_aula3, index="Dia", columns="Vendedor", values="Qtd_Carros", aggfunc=['sum', 'mean']))
# print(pd.pivot_table(df_aula3, index="Dia", columns="Vendedor", values="Qtd_Carros", aggfunc='sum'))

# Stack e Unstack de dados

df_nba = pd.read_csv('https://cdncontribute.geeksforgeeks.org/wp-content/uploads/nba.csv')

# print(df_nba.head())

stack_df_nba = df_nba.stack()
# print(stack_df_nba.head())

unstack_df_nba = stack_df_nba.unstack()
# print(unstack_df_nba.head())

# Usando melt() 1-2
df_aula5 = pd.DataFrame({
    'A': {0: 'a', 1: 'b', 2: 'c'},
    'B': {0: 1, 1: 3, 2: 5},
    'C': {0: 2, 1: 4, 2: 6},
})
# print(df_aula5)

# print(pd.melt(df_aula5, id_vars='A', value_vars='B'))

# print(df_aula5.melt(id_vars=['A'], value_vars=['B', 'C']))
# print(df_aula5.melt(id_vars=['A'], value_vars=['B', 'C'], var_name="TestandoVar", value_name='TestandoValor'))

# Usando melt() 2-2

datas_aula6 = {
    'Localização': ["CidadeA", "CidadeB"],
    'Temperatura': ["Prevista", "Atual"],
    'Set-2019': [30, 32],
    'Out-2019': [45, 43],
    'Nov-2019': [24, 22],
}
# print(datas_aula6)

df_aula6 = pd.DataFrame(datas_aula6, columns=['Localização', 'Temperatura', 'Set-2019', 'Out-2019', 'Nov-2019'])
print(df_aula6)
print("==="*20)
print(df_aula6.melt(id_vars=['Localização', 'Temperatura'], var_name='Data', value_name='Valor'))

# Não é interessante
# print(df_aula6.melt(id_vars=['Localização'], var_name='Data', value_name='Valor'))
