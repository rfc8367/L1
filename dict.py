dict1 = {'first_color': 'Red', 'second_color': 'Green', 'third_color': None}
dict = {k:v for k, v in dict1.items() if v is not None}
print(dict)