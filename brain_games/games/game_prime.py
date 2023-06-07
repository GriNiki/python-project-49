from random import randint


GAME_ANSWER = 'Answer "yes" if given number is prime. Otherwise answer "no".'
START_RANDOM_NUMBER = 1
STOP_RANDOM_NUMBER = 99


def calculate_prime(numb):
    start_divider = 2
    while numb % start_divider != 0:
        start_divider += 1
    return numb == start_divider


def get_game():
    numb = randint(START_RANDOM_NUMBER, STOP_RANDOM_NUMBER)
    print(f'Question: {numb}')
    solution_game = 'yes' if calculate_prime(numb) else 'no'
    return solution_game
