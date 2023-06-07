from random import randint, choice


GAME_ANSWER = 'What is the result of the expression?'
START_RANDOM_NUMBER = 1
STOP_RANDOM_NUMBER = 35
OPERATION = ['+', '-', '*']


def calculate_expression(numb1, numb2, operation):
    if operation == '+':
        solution_game = numb1 + numb2
    elif operation == '-':
        solution_game = numb1 - numb2
    else:
        solution_game = numb1 * numb2
    return solution_game


def get_game():
    numb1 = randint(START_RANDOM_NUMBER, STOP_RANDOM_NUMBER)
    numb2 = randint(START_RANDOM_NUMBER, STOP_RANDOM_NUMBER)
    operation = choice(OPERATION)
    print(f'Question: {numb1} {operation} {numb2}')
    solution_game = calculate_expression(numb1, numb2, operation)
    return str(solution_game)
