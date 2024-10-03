"""
Escreva uma função em Python que receba um inteiro positivo n 
e retorne a soma dos quadrados de todos os inteiros positivos menores do que n.
"""

def square_sum(n: int) -> int:
    return sum(map(lambda x: x*x, range(n)))

if __name__ == "__main__":
    print(square_sum(5))
