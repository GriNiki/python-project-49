import prompt


def greet():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello! {name}!')
    return name


def win():
    print(f'Congratulations, {greet()}!')