"""
Escreva uma função em Python que receba uma sequência de um ou mais números,
e retorne o menor e o maior número na forma de uma tupla de tamanho 2.
"""

from typing import List, Tuple

def min_max(lista: List[int | float]) -> Tuple[int | float, int | float]:
    return min(lista), max(lista)

if __name__ == "__main__":
    print(min_max([1, 2, 7, 483, 23, 53, -6, 12]))

