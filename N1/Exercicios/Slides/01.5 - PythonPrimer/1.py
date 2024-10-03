from typing import List, Tuple

def min_max(lista: List[int | float]) -> Tuple[int | float, int | float]:
    return min(lista), max(lista)

if __name__ == "__main__":
    print(min_max([1, 2, 7, 483, 23, 53, -6, 12]))

