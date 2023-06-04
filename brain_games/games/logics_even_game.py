from random import randint


GAME_ANSWER = 'Answer "yes" if the number is even, otherwise answer "no".'


def calculate_parity(numb):
    if numb % 2 == 0:
        solution_game = 'yes'
    else:
        solution_game = 'no'
    return solution_game


def get_game():
    numb = randint(1, 99)
    print(f'Question: {numb}')
    solution_game = calculate_parity(numb)
    return solution_game
