n = int(input("Введите число: "))
f = 1

for i in range(2, n + 1):
    f *= i

print(f)