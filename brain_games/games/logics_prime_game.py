from random import randint


GAME_ANSWER = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def calculate_prime(numb):
    start_divider = 2
    while numb % start_divider != 0:
        start_divider += 1
    if numb == start_divider:
        solution_game = 'yes'
    else:
        solution_game = 'no'
    return solution_game


def get_game():
    numb = randint(1, 99)
    print(f'Question: {numb}')
    solution_game = calculate_prime(numb)
    return solution_game
