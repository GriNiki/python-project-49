from brain_games.cli import greet
from random import randint
import prompt


NUMBER_OF_CORRECT_ANSWER = 3
GAME_ANSWER = 'What number is missing in the progression?'


def solution_progression_game():
    name = greet()
    print(GAME_ANSWER)
    for game_count in range(NUMBER_OF_CORRECT_ANSWER):
        index = randint(1, 9)
        list_answer = list(range(randint(1, 25), randint(75, 99), randint(1, 5)))
        solution_game = list_answer.pop(index)
        list_answer.insert(index, '..')
        print('Question: ', end='')
        print(*list_answer[:10], sep=' ')
        solution_user = int(prompt.string('Your answer: '))
        if solution_game == solution_user:
            print('Correct!')
        else:
            print(f'''"{solution_user}" is wrong answer ;(. Correct answer was '{solution_game}'.
Let's try again, {name}''')
            break
    else:
        print(f'Congratulations, {name}!')
