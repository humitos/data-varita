import os
import csv
import locale

# locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')

from decimal import Decimal

HEADERS = [
    'Masa',
    'Dia',
    'A1',
    'A2',
    'A1-B',
    'A2-B',
    'A (promedio)',
    'Prot (en reaccion)',
    'mg prot / gr muestra',
]

B = Decimal('0.063')

if __name__ == '__main__':
    with open('proteinas.csv', 'r') as fh:
        csvreader = csv.reader(fh)

        output = [] + [HEADERS]
        for row in csvreader:
            ro = [0] * 10
            ro[0] = Decimal(row[0].replace(',', '.'))  # Masa
            ro[1] = int(row[1])  # Dia
            ro[2] = row[2]  # Corte
            ro[3] = Decimal(row[3].replace(',', '.'))  # A1
            ro[4] = Decimal(row[4].replace(',', '.'))  # A2
            ro[5] = Decimal(row[3].replace(',', '.')) - B  # A1-B
            ro[6] = Decimal(row[4].replace(',', '.')) - B  # A2-B
            ro[7] = (ro[5] + ro[6]) / Decimal('2.0')  # A Promedio
            ro[8] = (ro[7] - Decimal('2E-16')) / 11
            ro[9] = (ro[8] * Decimal('2.2') * Decimal('20')) / (Decimal('0.05') * ro[0])
            output.append(ro)

    with open('proteinas_analizado.csv', 'w') as fh:
        csvwriter = csv.writer(fh)
        csvwriter.writerows(output)

    print 'Terminado!'
