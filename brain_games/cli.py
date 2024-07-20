def welcome_user():
    import prompt
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    return print(f'Hello, {name}')