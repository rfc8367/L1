word_count = 0
char_count = 0

usr_str = input("Введите строку: ")
split_string = usr_str.split()
word_count = len(split_string)
for word in split_string:
    char_count += len(word)

print("Количество слов: {}".format(word_count))
print("Количество символов: {}".format(char_count))
