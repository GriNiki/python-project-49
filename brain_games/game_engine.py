import prompt


NUMBER_OF_CORRECT_ANSWER = 3


def start_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.GAME_ANSWER)

    for game_count in range(NUMBER_OF_CORRECT_ANSWER):
        solution_game = game.get_game()
        solution_user = prompt.string('Your answer: ')
        if solution_game == solution_user:
            print('Correct!')
        else:
            print(f'"{solution_user}" is wrong answer ;(. '
                  f'Correct answer was "{solution_game}".')
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
