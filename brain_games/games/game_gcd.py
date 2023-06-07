from random import randint


GAME_ANSWER = 'Find the greatest common divisor of given numbers.'
START_RANDOM_NUMBER = 1
STOP_RANDOM_NUMBER = 99


def calculate_divisor(numb1, numb2):
    while numb1 != 0 and numb2 != 0:
        if numb1 > numb2:
            numb1 = numb1 % numb2
        elif numb1 < numb2:
            numb2 = numb2 % numb1
    solution_game = numb1 + numb2
    return solution_game


def get_game():
    numb1 = randint(START_RANDOM_NUMBER, STOP_RANDOM_NUMBER)
    numb2 = randint(START_RANDOM_NUMBER, STOP_RANDOM_NUMBER)
    print(f'Question: {numb1} {numb2}')
    solution_game = calculate_divisor(numb1, numb2)
    return str(solution_game)
