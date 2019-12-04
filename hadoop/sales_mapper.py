#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split(',')
    #title = words[1]
    try:
        year = int(float(words[3]))
        NA_sales = float(words[6])
    except Exception as e:
        continue
    print '%d\t%f' % (year, NA_sales)
