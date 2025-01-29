from operator import xor
from functools import reduce
from collections import Counter
from itertools import product

strings = [ "apple", "voadora", "banjo", "banana", "cherry", "date",
"elderberry", "fig", "grape", "honeydew", "kiwi", "xuru", "runin", "xamã",
"mirtilho", "lemon", "mango", "nectarine", "orange", "papaya", "quince",
"raspberry", "strawberry", "tangerine", "ugli", "voavanga", "maravilha",
"IFCE", "maracanaú", "ceará", "manga", "rendemption", "bobo", "maluco" ]

# Implementação

def somatorio(string: str):
    return sum(map(ord, string))

def dispersao_polinomial(string: str):
    return sum(ord(string[i])*(97**i)for i in range(len(string)))

def dispersao_de_deslocamento(string: str):
    return reduce(xor, map(ord, string)) ^ ord(string[0])


# Compressão
def divisao(k):
    return k%32

def dobra(k):
    arr = list(map(int, str(k)))
    while len(arr) > 2:
        if len(arr) == 3:
            arr = [(arr[1]+arr[2])%10, arr[0]]
            break
        num1 = (arr[0] + arr[3])%10
        num2 = (arr[1] + arr[2])%10
        arr = [num2, num1, *arr[4:]]
    
    return divisao(arr[0]*10 + arr[1]) if len(arr) > 1 else arr[0] 

def mad(k):
    return divisao((257*k+1)%1009)

def hash(impl_method, compression_method):
    return lambda x: compression_method(impl_method(x))

# Comparação de diferentes métodos.
l1 = [somatorio, dispersao_polinomial, dispersao_de_deslocamento]
l2 = [divisao, dobra, mad]
options = list(product(l1, l2))
for f1, f2 in options:
    print(f"({f1.__name__}, {f2.__name__}) colisões:", end=" ")
    collision = sum(map(lambda x: x-1, Counter(map(hash(f1, f2), strings)).values()))
    print(collision)
