first_var = int(input("Введите A: "))
second_var = int(input("Введите B: "))

if first_var < second_var:
    for i in range(first_var, second_var + 1):
        print(i)
else:
    for i in range(first_var, second_var - 1, -1):
        print(i)
