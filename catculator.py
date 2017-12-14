#!/usr/bin/python3
# --coding:utf-8--

import sys
import os

try:
    a = int(sys.argv[1])
except ValueError:
    print("Parameter Error")
    os.exit(0)


pay = int(sys.argv[1])

threshold = 3500

tax_in = (pay - threshold)
if tax_in < 1500:
    tax_pay = tax_in * 0.03
    print(format(tax_pay, '.2f'))
elif tax_in >= 1500 and tax_in <= 4500:
    tax_pay = (tax_in * 0.1 - 105)
    print(format(tax_pay, '.2f'))
elif tax_in > 4500 and tax_in <= 9000:
    tax_pay = (tax_in * 0.2 - 555)
    print(format(tax_pay, '.2f'))
elif tax_in > 9000 and tax_in <= 35000:
    tax_pay = (tax_in * 0.25 - 1005)
    print(format(tax_pay, '.2f'))
elif tax_in > 35000 and tax_in <= 55000:
    tax_pay = (tax_in * 0.3 - 2755)
    print(format(tax_pay, '.2f'))
elif tax_in > 55000 and tax_in <= 80000:
    tax_pay = (tax_in * 0.35 - 5505)
    print(format(tax_pay, '.2f'))
else:
    tax_pay = (tax_in * 0.45 - 13505)
    print(format(tax_pay, '.2f'))

