from brain_games.cli import greet
from random import randint
import prompt


NUMBER_OF_CORRECT_ANSWER = 3
GAME_ANSWER = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def solution_game_gcd():
    name = greet()
    print(GAME_ANSWER)
    for game_count in range(NUMBER_OF_CORRECT_ANSWER):
        number_prime_game = randint(1, 99)
        print(f'Question: {number_prime_game}')
        start_divider = 2
        while number_prime_game % start_divider != 0:
            start_divider += 1
        if number_prime_game == start_divider:
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
