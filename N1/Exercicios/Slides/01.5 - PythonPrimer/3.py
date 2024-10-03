from functools import reduce
from operator import add

def square_sum_even(n: int) -> int:
    return reduce(add, filter(lambda x: x%2 == 0, map(lambda x: x*x, range(n))))

if __name__ == "__main__":
    print(square_sum_even(5))
