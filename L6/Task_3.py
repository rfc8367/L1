value = ['a', 'b', 'c', 'd', 'e']
dict_a = {}

for key in value:
    dict_a[value.index(key)] = key

print(dict_a)


#Enumerate

value = ['a', 'b', 'c', 'd', 'e']
dict_b = dict(enumerate(value, 0))

print(dict_b)
