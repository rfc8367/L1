a = int(input())
max = 0
i = 0
maxi = 0

while a != 0:
    if a > max:
        max = a
        maxi = i
    a = int(input())
    i += 1
print(maxi)
