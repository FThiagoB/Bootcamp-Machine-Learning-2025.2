# 7) Como concaternar vários DataFrames (empilhando linhas ou colunas), mesmo que tenham colunas diferentes?

"""
Conforme mencionado, podemos utilizar pd.concat para fazer a concatenação de DataFrames. Dessa forma já temos um tratamento para colunas diferentes, que serão preenchidos com NaN. Além disso, podemos especificar se a concatenação será de linhas ou colunas por meio do valor escolhido para o argumento axis.
"""

import pandas as pd

dataframe_1 = pd.DataFrame({'Nome': ["Miguel", "Luiza"], 'Idade': [30, 24]})
dataframe_2 = pd.DataFrame({'Nome': ["André", "Felipe"], 'Idade': [20, 34]})
dataframe_3 = pd.DataFrame({'Comida favorita': ["Pizza", "Pudim"], 'Altura': [1.8, 1.6]})

# Concatena as linhas (resetando o índice)
pessoas = pd.concat([dataframe_1, dataframe_2], axis=0, ignore_index=True)

# Concatena as colunas
pessoas = pd.concat([pessoas, dataframe_3], axis=1)

print( pessoas )