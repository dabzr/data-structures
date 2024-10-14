# O(1)
def push_element_to_list(lista:list, n):
    lista.append(n)
# O(n)
def list_have_element(lista:list, n):
    return True if list(filter(lambda x: x==n, lista)) else False
# O(n²)
def matrix_have_element(matrix, n):
    for lista in matrix:
        for item in lista:
            if item == n:
                return True
    return False
#O(logn)
def sorted_list_have_element(lista, n):
    maior, menor = len(lista), 0
    element = (maior + menor) // 2
    for _ in lista:
        if n == lista[element]:
            return True
        if n < lista[element]:
            maior = element
            element = (maior + menor) // 2
        if n > lista[element]:
            menor = element
            element = (maior + menor) // 2
    return False

print(list_have_element([1, 5, 2, 3], 5))
print(matrix_have_element([[1, 2, 3],[4, 5, 6],[11, 1, 23]], 23))
print(sorted_list_have_element([1, 1, 2, 3], 12))
