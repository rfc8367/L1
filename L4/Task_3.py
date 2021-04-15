a_int = int(input("Введите A: "))
b_int = int(input("Введите B: "))

if a_int < b_int:
    for i in range(a_int, b_int + 1):
        print(i)
else:
    for i in range(a_int, b_int - 1, -1):
        print(i)
