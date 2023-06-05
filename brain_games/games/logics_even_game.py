from random import randint


GAME_ANSWER = 'Answer "yes" if the number is even, otherwise answer "no".'


def calculate_parity(numb):
    return numb % 2 == 0


def get_game():
    numb = randint(1, 99)
    print(f'Question: {numb}')
    solution_game = 'yes' if calculate_parity(numb) else 'no'
    return solution_game
