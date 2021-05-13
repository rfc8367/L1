def shift():
    user_list = list(map(int, input("Введите список: ").split()))
    move = int(input("Введите значение: "))

    user_list = user_list[-move:] + user_list[:-move]
    print(user_list)

shift()
