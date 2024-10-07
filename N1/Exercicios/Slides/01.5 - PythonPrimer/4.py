"""
Escreva uma função em Python que receba uma sequência de números 
e determine se todos os números são diferentes um dos outros.
"""

def have_repeated_items(lista: list) -> bool:
    return len(set(lista)) != len(lista)

if __name__ == "__main__":
    print(have_repeated_items([1, 1, 3, 4, 5]))
