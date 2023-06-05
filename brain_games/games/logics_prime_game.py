from random import randint


GAME_ANSWER = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def calculate_prime(numb):
    start_divider = 2
    while numb % start_divider != 0:
        start_divider += 1
    return numb == start_divider


def get_game():
    numb = randint(1, 99)
    print(f'Question: {numb}')
    solution_game = 'yes' if calculate_prime(numb) else 'no'
    return solution_game
