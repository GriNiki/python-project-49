from random import randint


GAME_ANSWER = 'Answer "yes" if the number is even, otherwise answer "no".'
START_RANDOM_NUMBER = 1
STOP_RANDOM_NUMBER = 99


def calculate_parity(numb):
    return numb % 2 == 0


def get_game():
    numb = randint(START_RANDOM_NUMBER, STOP_RANDOM_NUMBER)
    print(f'Question: {numb}')
    solution_game = 'yes' if calculate_parity(numb) else 'no'
    return solution_game
