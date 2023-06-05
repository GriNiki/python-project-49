from random import randint, choice


GAME_ANSWER = 'What is the result of the expression?'


def calculate_expression(numb1, numb2, operation):
    if operation == '+':
        solution_game = numb1 + numb2
    elif operation == '-':
        solution_game = numb1 - numb2
    else:
        solution_game = numb1 * numb2
    return solution_game


def get_game():
    numb1 = randint(1, 35)
    numb2 = randint(1, 35)
    operation = choice(['+', '-', '*'])
    print(f'Question: {numb1} {operation} {numb2}')
    solution_game = calculate_expression(numb1, numb2, operation)
    return str(solution_game)
