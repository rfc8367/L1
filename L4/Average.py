n = int(input("Введите число: "))
sum = 0
count = 0
average = 0

while n != 0:
    sum += n
    n = int(input())
    count += 1

average = (sum/count)
print(average)
