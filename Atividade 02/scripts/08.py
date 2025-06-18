# 8) Utilizando panda, como realizar a leitura de um arquivo CSV em um DataFrame e exibir as primeiras linhas?

import pandas as pd

# Podemos usar read_csv para abrir arquivos CSV (há diversas configurações possíveis)
dataset_path = "../iris.data"
dataset = pd.read_csv(dataset_path, names = ["sepal length", "sepal width", "petal length", "petal width", "class"])

# O método head exibe as primeiras linhas
dataset.head()