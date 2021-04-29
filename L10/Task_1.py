def new_file():
    user_file = str
    lines = []

    while user_file != '':
        user_file = str(input('Введите построчно файл: '))
        lines.append(user_file)

    with open('file1.txt', 'w' ) as file:
        for line in lines:
            file.write(line + '\n')
    file.close()

new_file()