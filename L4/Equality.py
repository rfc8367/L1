maximum = 0
count = 1
num = int(input())

while num != 0:
    if num > maximum:
        maximum = num
        count = 1
    elif num == maximum:
        count += 1
    num = int(input("Введите число: "))
print(count)
