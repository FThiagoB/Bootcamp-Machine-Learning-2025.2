# 3) Escreva uma função que receba duas listas e retorne outra lista com os elementos que estão presentes em apenas uma das listas.

import numpy as np

def xor_lists( lista_a, lista_b ):
    # Converte a lista em um array do numpy
    if not isinstance( lista_a, np.ndarray ):
        lista_a = np.array( lista_a )

    # Converte a lista em um array do numpy
    if not isinstance( lista_b, np.ndarray ):
        lista_b = np.array( lista_b )
    
    # Numpy tem um método builtin para obter os elementos exclusivos entre as listas
    return np.setxor1d( lista_a, lista_b )

if __name__ == "__main__":
    lista_a = [0, 1, 2, 3, 4, 10, 13, 17, 20]
    lista_b = [0, 2, 4, 6, 7, 8, 10, 17, 25]

    print(f"Primeira lista: {lista_a}")
    print(f"Segunda lista: {lista_b}")

    print(f"Os números exclusivos são: {xor_lists(lista_a, lista_b)}")
