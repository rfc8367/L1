x = int(input("Введите x: "))
y = int(input("Введите y: "))
i = 1

while x < y:
    x = x + (x * 0.1)
    i += 1

print(i)
