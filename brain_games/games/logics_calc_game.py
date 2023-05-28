from brain_games.cli import greet
from random import randint, choice
import prompt


NUMBER_OF_CORRECT_ANSWER = 3
GAME_ANSWER = 'What is the result of the expression?'


def solution_calc_game():
    name = greet()
    print(GAME_ANSWER)
    for game_count in range(NUMBER_OF_CORRECT_ANSWER):
        numb1_calc_game = randint(1, 35)
        numb2_calc_game = randint(1, 35)
        operation = choice(['+', '-', '*'])
        solution_game = 0
        if operation == '+':
            solution_game = numb1_calc_game + numb2_calc_game
        elif operation == '-':
            solution_game = numb1_calc_game - numb2_calc_game
        elif operation == '*':
            solution_game = numb1_calc_game * numb2_calc_game
        print(f'Question: {numb1_calc_game} {operation} {numb2_calc_game}')
        solution_user = int(prompt.string('Your answer: '))
        if solution_game == solution_user:
            print('Correct!')
        else:
            print(f'''"{solution_user}" is wrong answer ;(. Correct answer was '{solution_game}'.
Let's try again, {name}''')
            break
    else:
        print(f'Congratulations, {name}!')
