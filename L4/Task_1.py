x_var = int(input("Введите x: "))
y_var = int(input("Введите y: "))
i = 1

while x_var < y_var:
    x_num = x_var + (x_var * 0.1)
    i += 1

print(i)
