def area(figure, data):
    if figure == 'К':
        a, b = data
        res = a * b
    if figure == 'Т':
        a, b = data
        res = (a * b) / 2
    return ' Площадь {} = {}'.format(figure, res)


figure = input('Введите первую заглавную букву фигуры: ')
data = [float(i) for i in input('Значения исходных данных через пробел: ').split()]
print(area(figure, data))
