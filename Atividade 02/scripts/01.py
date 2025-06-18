# 1) Escreva uma função que receba uma lista de números e retorne outra lista com os números ímpares.

import numpy as np

def get_odd_numbers( números ):
    # Converte a lista em um array do numpy
    if not isinstance( números, np.ndarray ):
        números = np.array( números )

    # Retorna os elementos ímpares do array
    return números[ números % 2 != 0 ]

if __name__ == "__main__":
    lista_números = [0, 1, 2, 3, 4, 10, 13, 17, 20]

    print(f"Os números da lista são: {lista_números}")
    print(f"Os números ímpares são: {get_odd_numbers(lista_números)}")