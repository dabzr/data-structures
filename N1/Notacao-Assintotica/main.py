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

#O(n logn)
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid] 
        right_half = arr[mid:]

        merge_sort(left_half) 
        merge_sort(right_half)  

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


arr = [38, 27, 43, 3, 9, 82, 10]
print("Original Array:", arr)
merge_sort(arr)
print("Array sorted:", arr)
print(list_have_element([1, 5, 2, 3], 5))
print(matrix_have_element([[1, 2, 3],[4, 5, 6],[11, 1, 23]], 23))
print(sorted_list_have_element([1, 1, 2, 3], 12))
