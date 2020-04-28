from random import randint, choice


def add():
    '''Addition.

    Return:
        5 if correct
        -3 in incorrect
    '''
    n1 = randint(2, 1000)
    n2 = randint(2, 1000)
    result = n1 + n2
    answer = input(f'{n1} + {n2} = ')
    if result == int(answer):
        print('correct')
        return 5
    else:
        print('incorrect')
        print(f'{n1} + {n2} should be {result}')
        return -3


def mul():
    '''Multiplication.

    Return: 
        3 if correct.
        -2 if incorrect.
    '''
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


def play(target=50):
    '''Play calculation game for ramdom add/mul.

    Args:
        target(int): target score, 50 by default.
    '''
    points = 0
    question = 0
    while points < target:
        question += 1
        print(f'Question-{question}'.center(79, '~'))
        points += choice([add, mul])()
    print(f'Congratulations! You have answered {question} questions and earned {points}!')