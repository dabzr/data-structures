from typing import List

def have_repeated_items(lista: List[int]) -> bool:
    return len(set(lista)) != len(lista)

if __name__ == "__main__":
    print(have_repeated_items([1, 1, 3, 4, 5]))
