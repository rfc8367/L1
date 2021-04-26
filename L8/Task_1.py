import requests
import json
import argparse
from datetime import timedelta, datetime

today = datetime.now()
result = ['From: ', 'To: ', 'Amount: ', 'Result: ', 'Date: ']


def open_file():
    with open('symbols.json', 'r+') as file:
        data = json.load(file)
        symbol_check = data['symbols']
        if arg.currency_from in symbol_check and arg.currency_to in symbol_check:
            pars()



def pars():

    if arg.start_date != today:
        start_date = datetime.strptime(arg.start_date, "%Y-%m-%d")

        while start_date <= today:

            response = requests.get('https://api.exchangerate.host/convert',
                            params={'from': arg.currency_from, 'to': arg.currency_to, 'amount': arg.amount,
                                    'date': start_date}).json()

            result.append([str(response['date']), str(response['query']['from']), str(response['query']['to']),
                       str(response['query']['amount']), str(response['result'])])

            start_date += timedelta(days=1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Online Currency Converter')
    parser.add_argument('currency_from', default = 'USD', type = str)
    parser.add_argument('currency_to', default = 'UAH', type = str)
    parser.add_argument('amount', default = 100, type = float)
    parser.add_argument('--start-date',default = today, type = str)

    arg = parser.parse_args()

pars()
