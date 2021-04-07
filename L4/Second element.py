a = int(input())
f_max = 0
s_max = 0

while a != 0:
    if a > f_max:
        s_max = f_max
        f_max = a
    elif a > s_max:
        s_max = a
    a = int(input())

print(s_max)