#!/usr/bin/python3

import db.crud as db
from fuzzywuzzy import fuzz

def takescore(lis):
        return lis[-1]

sumber_data = db.SumberData( \
        'localhost', \
        3050, \
        'C:\msys64\home\KITAGROUP\KASIRRUSAK\BACKOFFICE.FDB', \
        'SYSDBA', \
        'masterkey'
        )
while (True):
        test = input("Input: ")
        items = sumber_data.get_data_produk()
        result = list()
        for item in items:
                ratio = fuzz.token_set_ratio(test, item[1])
                liss = (list(item))
                liss.append(ratio)
                result.append(liss)

        result.sort(reverse=True, key=takescore)
        print(*result[:20], sep='\n')

sumber_data.tutup()
