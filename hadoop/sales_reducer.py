#!/usr/bin/env python

import sys

current_year = None
current_sales = 0.0
num_titles = 0
for line in sys.stdin:
    line = line.strip()
    year, NA_sales = line.split('\t')
    try:
        year = int(year)
	NA_sales = float(NA_sales)
    except ValueError:
        continue
    if current_year == year:
        current_sales += NA_sales
        num_titles += 1
    else:
        if current_year:
	    print '%d\t%f' % (current_year, current_sales/num_titles)
	current_sales = NA_sales 
	current_year = year
        num_titles = 1
if current_year == year:
    print '%d\t%f' % (current_year, current_sales)


