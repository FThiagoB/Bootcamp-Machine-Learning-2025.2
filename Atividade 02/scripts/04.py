# 4) Dada uma lista de números inteiros, escreva uma função para encontrar o segundo maior valor na lista.

import numpy as np

def second_largest( números ):
    # Converte a lista em um array do numpy
    if not isinstance( números, np.ndarray ):
        números = np.array( números )

    # Organiza em ordem crescente
    números.sort()
    
    # Retorna o segundo maior valor da lista
    return números[-2]

if __name__ == "__main__":
    lista_números = np.random.randint( -50, 50, size=(10) )

    print(f"Os números da lista são: {lista_números}")
    print(f"Segundo maior valor: {second_largest(lista_números)}")