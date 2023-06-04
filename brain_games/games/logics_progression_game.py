from random import randint


GAME_ANSWER = 'What number is missing in the progression?'


def get_game():
    index = randint(1, 9)
    list_answer = list(range(randint(1, 25), randint(75, 99), randint(1, 5)))
    solution_game = list_answer.pop(index)
    list_answer.insert(index, '..')
    print('Question: ', end='')
    print(*list_answer[:10], sep=' ')
    return str(solution_game)
