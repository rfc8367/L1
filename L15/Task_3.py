import re


def password_patterns():
    while True:
        user_password = input('Enter your password: ')
        length = len(user_password)
        print(f'Your password length {length}')
        if len(user_password) <= 8:
            print('Password must contain at least 8 characters')
            continue
        lowerRE = re.compile(r'[a-z]')
        if not (lowerRE.search(user_password)):
            print('Password must contain lower characters')
            continue
        upperRE = re.compile(r'[A-Z]')
        if not (upperRE.search(user_password)):
            print('Password must contain upper characters')
            continue
        numberRE = re.compile(r'[0-9]')
        if not (numberRE.search(user_password)):
            print('Password must contain numbers')
            continue
        symbolRE = re.compile(r'[$#@+=-]')
        if not (symbolRE.search(user_password)):
            print('Password must contain symbols')
        else:
            print('Password is strong')

password_patterns()