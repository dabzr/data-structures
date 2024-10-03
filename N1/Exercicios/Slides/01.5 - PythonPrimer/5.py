from random import randint

def have_same_birthday(n: int) -> bool:
    birthdays = [randint(1, 366) for _ in range(n)]
    return len(set(birthdays)) != len(birthdays)

if __name__ == "__main__":
    for i in range(5, 101, 5):
        string = f" numa sala com {i} pessoas faz aniversário no mesmo dia"
        print("Ao menos duas pessoas" + string if have_same_birthday(i) else "Ninguém" + string)
