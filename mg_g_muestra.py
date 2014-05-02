import os
import csv
import locale
import string

# locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')

from decimal import Decimal, getcontext
getcontext().prec = 5

HEADERS = [
    '',
    'ED',
    'CM',
    'CC',
]

if __name__ == '__main__':
    with open('proteinas_analizado.csv', 'r') as fh:
        csvreader = csv.reader(fh)

        output = []  # + [HEADERS]
        reader_list = list(csvreader)

        list_of_slices = zip(*(iter(reader_list),) * 6)

        for rows in list_of_slices:
            # import ipdb;ipdb.set_trace()
            # row = map(lambda x: string.replace(x, ',', '.'), row)

            ro1 = [0] * 4
            ro1[0] = rows[0][1]  # Dia
            ro1[1] = rows[0][9]  # mg/g
            ro1[2] = rows[2][9]  # mg/g
            ro1[3] = rows[4][9]  # mg/g

            ro2 = [0] * 4
            ro2[0] = rows[1][1]  # Dia
            ro2[1] = rows[1][9]  # mg/g
            ro2[2] = rows[3][9]  # mg/g
            ro2[3] = rows[5][9]  # mg/g
            output.append(ro1)
            output.append(ro2)

    with open('proteinas_analizado_invertido.csv', 'w') as fh:
        csvwriter = csv.writer(fh)
        csvwriter.writerows(output)

    print 'Terminado!'
