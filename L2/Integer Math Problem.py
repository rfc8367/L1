v = int(input("Введите скорость: "))
t = int(input("Введите время: "))
s = 100

if v > 0:
    d = (v * t) % s
else:
    d = abs((abs(v * t) - s)) % s
print(d)