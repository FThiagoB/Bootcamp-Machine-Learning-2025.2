# 2) Escreva uma função que receba uma lista de números e retorne outra lista com os números primos presentes.

import numpy as np

def get_prime_numbers( números ):
    def is_prime( number ):
        if number <= 1:
            return False
        
        # Percorre os antecessores de dado número
        for antecessor in range( number - 1, 1, -1 ):
            # Verifica se o número é divisível por seu antecessor
            if number%antecessor == 0:
                return False
        
        return True
    
    # Converte a lista em um array do numpy
    if not isinstance( números, np.ndarray ):
        números = np.array( números )

    # Aplica a função criada à todos os elementos da lista
    índices_primos = list( map(is_prime, números) )

    # Retorna os elementos primeos da lista
    return números[ índices_primos ]

if __name__ == "__main__":
    lista_números = [0, 1, 2, 3, 4, 10, 13, 17, 20]

    print(f"Os números da lista são: {lista_números}")
    print(f"Os números primos são: {get_prime_numbers(lista_números)}")