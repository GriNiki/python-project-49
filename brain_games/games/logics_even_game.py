from brain_games.cli import greet
from random import randint
import prompt


NUMBER_OF_CORRECT_ANSWER = 3
GAME_ANSWER = 'Answer "yes" if the number is even, otherwise answer "no".'


def solution_even_game():
    name = greet()
    print(GAME_ANSWER)
    for game_count in range(NUMBER_OF_CORRECT_ANSWER):
        numb_even_game = randint(1, 99)
        print(f'Question: {numb_even_game}')
        if numb_even_game % 2 == 0:
            solution_game = 'yes'
        else:
            solution_game = 'no'
        solution_user = prompt.string('Your answer: ')
        if solution_game == solution_user:
            print('Correct!')
        else:
            print(f'''"{solution_user}" is wrong answer ;(. Correct answer was '{solution_game}'.
Let's try again, {name}''')
            break
    else:
        print(f'Congratulations, {name}!')
