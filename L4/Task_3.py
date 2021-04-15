first_int = int(input("Введите A: "))
second_int = int(input("Введите B: "))

if first_int < second_int:
    for i in range(first_int, second_int + 1):
        print(i)
else:
    for i in range(first_int, second_int - 1, -1):
        print(i)
