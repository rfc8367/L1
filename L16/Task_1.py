import csv
import argparse


class CountryNotFoundError(Exception):
    def __init__(self, cnty_error, error_str):
        self.cnty_error = 'Country not found'
        self.error_str = error_str

    def __str__(self):
        return self.cnty_error + self.error_str


class AirportNotFoundError(Exception):
    def __init__(self, air_error, error_str):
        self.air_error = 'Airport not found'
        self.error_str = error_str

    def __str__(self):
        return 'Error' + self.air_error + self.error_str


class MultipleOptionsError(Exception):
    pass


class NoOptionsFoundError(Exception):
    pass


class IATACodeError(Exception):
    pass


class Airport():

    def __init__(self, arguments):
        self.args = self.checker(arguments)
        
    def open_file():
        param_data = []
        with open('airport-codes_csv.csv', 'r') as file:
            csv_reader = csv.DictReader(file, delimiter=',')
            for param in csv_reader:
                param_data.append(param)
        return param_data

    def checker(self, arguments):
        result = []
        argument = [('iata_code', arguments.iata_code),
                    ('country', arguments.country),
                    ('name', arguments.name)]

        for args in argument:
            if args[1] is not None:
                result.append(args)

        if len(result) > 1:
            raise MultipleOptionsError('Только один параметр обязателен')
        elif len(result) == 0:
            raise NoOptionsFoundError('Параметры отсутствуют')
        elif 'iata_code' in len(result) != 3:
            raise IATACodeError('IATA код может быть только 3х буквенным в верхнем регистре')
        else:
            return result

    def find():

        air = []
        ctry = []
        csv = open_file()
        check = checker()

        for row in csv:
            if check == 'iata_code' in row['iata_code']:
                air.append(row)
            if check == 'country' in row['country']:
                ctry.append(row)
            if check == 'name' in row['name']:
                air.append(row['name'])

        if len(ctry) == 0:
            raise CountryNotFoundError
        if len(air) == 0:
            raise AirportNotFoundError
        return air


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Airport')
    parser.add_argument('--iata_code')
    parser.add_argument('--country')
    parser.add_argument('--name')
    arguments = parser.parse_args()
