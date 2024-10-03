"""
O paradoxo do aniversário diz que a probabilidade de duas pessoas em uma mesma sala terem
o mesmo dia de aniversário é maior do que 50%, dado n, o número de pessoas na sala, maior do que 23.

Projete um programa em Python que teste este paradoxo por meio de uma série de experimentos em datas de aniversário aleatórias,
que testam o paradoxo para n = 5,10,15,20,...,100.
"""

from random import randint

def have_same_birthday(n: int) -> bool:
    birthdays = [randint(1, 366) for _ in range(n)]
    return len(set(birthdays)) != len(birthdays)

if __name__ == "__main__":
    for i in range(5, 101, 5):
        string = f" numa sala com {i} pessoas faz aniversário no mesmo dia"
        print("Ao menos duas pessoas" + string if have_same_birthday(i) else "Ninguém" + string)
