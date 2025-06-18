# 9) Utilizando pandas, como selecionar uma coluna específica e filtrar linhas em um "DataFrame" com base em uma condição?

import pandas as pd

# Pandas permite realizar isso de forma direta, apenas especificando o nome da coluna e a condição desejada
dataframe_1 = pd.DataFrame({'Nome': ["Miguel", "Luiza", "Souza", "Felipe", "Andreza", "Sérgio"], 'Idade': [30, 24, 18, 15, 10, 20]})

# Por exemplo, filtrando todas as linhas que possuem valores maiores que 20 na coluna de idade
print( dataframe_1[ dataframe_1["Idade"] > 20 ] )