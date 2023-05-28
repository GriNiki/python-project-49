from brain_games.cli import greet
from random import randint
import prompt


NUMBER_OF_CORRECT_ANSWER = 3
GAME_ANSWER = 'Find the greatest common divisor of given numbers.'


def solution_game_gcd():
    name = greet()
    print(GAME_ANSWER)
    for game_count in range(NUMBER_OF_CORRECT_ANSWER):
        number1_gcd_game = randint(1, 99)
        number2_gcd_game = randint(1, 99)
        print(f'Question: {number1_gcd_game} {number2_gcd_game}')
        while number1_gcd_game != 0 and number2_gcd_game != 0:
            if number1_gcd_game > number2_gcd_game:
                number1_gcd_game = number1_gcd_game % number2_gcd_game
            elif number1_gcd_game < number2_gcd_game:
                number2_gcd_game = number2_gcd_game % number1_gcd_game
        solution_game = number1_gcd_game + number2_gcd_game
        solution_user = int(prompt.string('Your answer: '))
        if solution_game == solution_user:
            print('Correct!')
        else:
            print(f'''"{solution_user}" is wrong answer ;(. Correct answer was "{solution_game}".
Let's try again, {name}!''')
            break
    else:
        print(f'Congratulations, {name}!')
