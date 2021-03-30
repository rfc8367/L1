list_of_six = [100, 106, 112, 118, 124, 130, 136, 142, 148, 154, 160, 166, 172, 178, 184, 190, 196]
Max = 150
DivNumber = 5

for i in list_of_six:
    if (i < Max) and (i % DivNumber == 0):
        print("Число {0} из списка делится на 5".format(i))
