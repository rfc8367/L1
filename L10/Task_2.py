def palindrome():
    new_string = str(input("Введите строку: "))

    if new_string == new_string[::-1]:
        print("Слово является палиндромом")
    else:
        print("Слово не является палиндромом")

palindrome()