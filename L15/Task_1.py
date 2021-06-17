import csv
import re


def open_file():
    with open('ua_auto.csv', 'r+') as auto:
        csv_reader = csv.DictReader(auto, delimiter=',')
        number_list = []
        for row in csv_reader:
            number_list.append(row)
        return number_list


def validation():
    number_list = open_file()
    car_id = input('Enter auto code: ')
    number_auto = re.findall(r'^[АВСЕНІКМОРТХABCEHIMOPTX]{2}\d{4}[АВСЕНІКМОРТХABCEHIMOPTX]{2}', car_id)
    
    if not number_auto:
        raise Exception(f'{car_id} Invalid number')
    else:
        for number in number_list:
            if number ['Код 2004']:
                number_list.append(row['Регіон'] + '2004г'
                print(f'{car_id}, 2004. Region: ', row['Регіон'])
                break
            elif number ['Код 2013']:
                number_list(row['Регіон'] + '2013г'
                print(f'{car_id}, 2013. Region: ', row['Регіон'])
                break
                            
def validation()
