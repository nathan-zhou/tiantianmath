from random import randint, choice


def add():
    n1 = randint(2, 1000)
    n2 = randint(2, 1000)
    result = n1 + n2
    answer = input(f'{n1} + {n2} = ')
    if result == int(answer):
        print('correct')
        return True
    else:
        print('incorrect')
        print(f'{n1} + {n2} = {result}')
        return False


def mul():
    n1 = randint(2, 10)
    n2 = randint(2, 10)
    result = n1 * n2
    answer = input(f'{n1} * {n2} = ')
    if result == int(answer):
        print('correct')
        return 3
    else:
        print('incorrect')
        print(f'{n1} * {n2} should be {result}')
        return -2
