# 10) Utilizando pandas, como lidar com valores ausentes (NaN) em um DataFrame?

import numpy as np
import pandas as pd

# Exemplo de dataframe com elementos faltantes (poderíamos especificar 'na_values' caso fosse lido por meio de read_csv)
dataframe = pd.DataFrame({'Nome': ["Miguel", "Luiza", "Souza", "Felipe", "Andreza", "Sérgio"], 'Idade': [30, "?", 18, "?", 10, "?"]})

# Substitui os elementos faltantes por NaN
dataframe = dataframe.where( dataframe != "?", np.nan)
print( dataframe, "\n" )

# A partir dai teríamos algumas opções, tais como atribuir valores específicos para campos com NaN ou remover eles
dataframe_fill_nan = dataframe.fillna(5)    # Preenche os NaN com um valor
print( dataframe_fill_nan, "\n" )

dataframe_without_nan = dataframe.dropna()  # Remove os campos com NaN
print( dataframe_without_nan, "\n" )