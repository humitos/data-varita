import os
import csv
import locale
import string

# locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')

from decimal import Decimal, getcontext

HEADERS = [
    'Masa',
    'Dia',
    'Corte',
    'A1',
    'A2',
    'A1-B',
    'A2-B',
    'A (promedio)',
    'Proteinas (en reaccion)',
    'mg protreinas / g muestra',
]

# BLANCO = Decimal('0.063')
# VOL_MUESTRA = Decimal('0.05')  # Muestra PAL a 2 grados
# VOL_MUESTRA = Decimal('0.10')  # Muestra PPO a 2 grados


def process(name, finput, foutput, blanco, vol_muestra, prec=5):
    getcontext().prec = prec

    with open(finput, 'r') as fh:
        csvreader = csv.reader(fh)
        # omitir primera linea
        csvreader.next()

        output = [['NOMBRE', name, '', '', '', '', '', '', '', '']] + [HEADERS]
        for row in csvreader:
            row = list(map(lambda x: string.replace(x, ',', '.'), row))

            ro = [0] * 10
            ro[0] = Decimal(row[0])  # Masa
            ro[1] = int(row[1])  # Dia
            ro[2] = row[2]  # Corte
            ro[3] = Decimal(row[3])  # A1
            ro[4] = Decimal(row[4])  # A2
            ro[5] = Decimal(row[3]) - blanco  # A1-B
            ro[6] = Decimal(row[4]) - blanco  # A2-B
            ro[7] = (ro[5] + ro[6]) / Decimal('2.0')  # A Promedio
            ro[8] = Decimal(str(round((ro[7] - Decimal('2E-16')) / 11, 3)))
            ro[9] = round((ro[8] * Decimal('2.2') * Decimal('20')) / (vol_muestra * ro[0]), 3)
            output.append(ro)

    with open(foutput, 'w') as fh:
        csvwriter = csv.writer(fh)
        csvwriter.writerows(output)
