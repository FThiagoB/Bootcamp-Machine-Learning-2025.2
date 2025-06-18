# 5) Crie uma função que receba uma lista de tuplas, cada uma contendo o nome e a idade de uma pessoa, e retorne a lista ordenada pelo nome das pessoas em ordem alfabética.

def sort_persons( pessoas ):
    # Sorteia a lista de tuplas considerando a primeira letra de cada nome
    return sorted( pessoas, key = lambda pessoa: pessoa[0][0] )

if __name__ == "__main__":
    lista_pessoas = [
        ("Ciclano de Tals", 40),
        ("Aline fernandes", 35),
        ("Gustavo Augusto", 25),
        ("Luana de Sousa", 20),
        ("Fernanda Luiza", 18),
        ("Beatriz Barbosa", 34),
        ("Alan Pessoa", 23)
    ]

    print( sort_persons(lista_pessoas) )