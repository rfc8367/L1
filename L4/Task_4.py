n = int(input("Введите число: "))
ladder = ""

if n <= 9:
    for i in range(1, n + 1):
        ladder = ladder + str(i)
        print(ladder)
else:
    print("Число больше 9")
