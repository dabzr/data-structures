"""
Escreva uma função em Python que receba um inteiro positivo n 
e retorne a soma dos quadrados de todos os inteiros positivos pares menores do que n.
"""

def square_sum_even(n: int) -> int:
    return sum(filter(lambda x: x%2 == 0, map(lambda x: x*x, range(n))))

if __name__ == "__main__":
    print(square_sum_even(5))
