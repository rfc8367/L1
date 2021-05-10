def word_changer():

    old_string = str(input("Enter string for changes: "))
    old_word = str(input("Enter word to change: "))
    new_word = str(input("Enter new word: "))
    count = int(input("Amount of word changes: "))

    word_replace = old_string.replace(old_word, new_word, count)

    return word_replace

print(word_changer())