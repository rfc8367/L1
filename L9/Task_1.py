import csv
import argparse


def check_args(row):
    dict_args = {'brand': 'BRAND',
                 'color': 'COLOR',
                 'year': 'MAKE_YEAR',
                 'fuel': 'FUEL',
                 'reg_num': 'N_REG_NUM'}
    args_check = {key: value for key, value in dict_args.item() if value is not None}

    save_flag = False
    for key, value in args_check.items():
        if not value:
            continue
        if row[row[key]] == value:
            save_flag = True
        else:
            save_flag = False
    return save_flag



def open_file():
    data = []
    with open('tz_opendata_z01012021_po01042021.csv') as csv_file:
        columns = ['BRAND', 'MODEL', 'MAKE_YEAR', 'COLOR', 'FUEL', 'N_REG_NEW']
        csv_reader = csv.DictReader(csv_file, fieldnames=columns, delimiter=',')
        next(csv_reader)

        for row in csv_reader:
            if check_args(row):
                data.append(row)
        csv_file.close()


def save_file(data):
    with open('csv_file.csv', 'w') as new_csv:
        columns = ['BRAND', 'MODEL', 'MAKE_YEAR', 'COLOR', 'FUEL', 'N_REG_NEW']
        csv_writer = csv.DictWriter(new_csv, fieldnames=columns, delimiter=',')
        csv_writer.writerows(data)
    new_csv.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CarFinder')
    parser.add_argument('file_name', default='tz_opendata_z01012021_po01042021.csv', type=str)
    parser.add_argument('--brand', type=str)
    parser.add_argument('--color', type=str)
    parser.add_argument('--year', type=str)
    parser.add_argument('--fuel', type=str)
    parser.add_argument('--reg_num', type=str)
    args = parser.parse_args()