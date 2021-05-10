def longest_word():
    user_string = str(input('Enter your string: '))
    max_word = max(user_string.split(), key=len)
    return max_word

print(longest_word())