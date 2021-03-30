import random
guesses_made = 0
name = input("Как твоё имя, user? ")

number = random.randint(1,10)
print("Посмотри на себя, {0}. Как ты посмел бросить вызов безупречной, бессмертной машине?".format(name))


while guesses_made < 3:

    guess = int(input("Число: "))
    guesses_made += 1

    if guess < number:
        print("Ты не угадал. Бьюсь об заклад, что считать числа побольше ты не способен")
    if guess > number:
        print("Ты не угадал. Бьюсь об заклад, что взять число поменьше ты не способен")
    if guess == number:
      break


if guess == number:
    print("Пользователь {0} одержал победу. Ты угадал число с {1} попытки. Слава пользователям!".format(name, guesses_made))
else:
    print("Ты не угадал. Пользователь подлежит уничтожению")