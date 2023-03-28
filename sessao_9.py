import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Tipos de arquivos .TXT .CSV .XLSX
# Repositório de dados gratuitos

"""https://archive.ics.uci.edu/ml/index.php"""

df = pd.read_csv(r"Repository/iris.data")
# print(df.head(5))
# df.columns = list('ABCDE')
# print(df)

# Salvando dados do Excel para .CSV

df1 = pd.read_excel(r"Repository/dados_3.xlsx")
print(df1)

df1.to_csv("Repository/createdtest.csv")
