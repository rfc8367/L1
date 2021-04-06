a = input()
a = int(a)

even_count = 0
odd_count = 0

while a != 0:
    if a % 2 == 0:
        even_count += 1

    else:
        odd_count += 1
    a = a // 10
print("Even: %d, Odd: %d" % (even_count, odd_count))

