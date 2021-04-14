def replace_odd(l, v = '0'):
    return [v if not i % 2 else x for i, x in enumerate(l)]

print(replace_odd(list(input("Введите список: "))))
