# 6) Como identificar e tratar outliers em uma coluna numérica usando desvio padrão ou quartis?

"""
    Podemos visualizar os dados usando um boxplot de forma que os outliers fiquem visíveis. Além disso,
uma das formas de tratar os outliers seria removendo esses pontos da análise (possível ao calcular os 
valores dos quartis, de forma a obter os limites de corte).
"""

import numpy as np
import matplotlib.pyplot as plt

# Cria uma distribuição normal e adiciona algum ruido (representaria os dados da coluna)
y = np.random.normal( 0, 10, 20 )
y = np.append(y, [50, -45, 80])

# Exibe o boxplot, onde os outliers seriam visíveis
fig = plt.boxplot( y, showmeans=True )
plt.show( block = True )