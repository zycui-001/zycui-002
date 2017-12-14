#!/usr/bin/env python3
# --coding:utf-8

import sys
import os

for arg in sys.argv[1: ]:
    try:
        pay_id = int(arg.split(":")[0])
        pay = int(arg.split(":")[1])
    except ValueError:
        print("Parameter Error")
        os.exit(0)
    # 工号
    pay_id = int(arg.split(":")[0])
    # 工资
    pay = int(arg.split(":")[1])
    # 各项社会保险费，养老保险：8%；医疗保险：2%；失业保险：0.5%；公积金：6%
    pay_safe = pay * (0.08 + 0.02 +0.005 + 0.06)
    # 起征点
    a = 3500
    # 应纳税所得额
    if pay <= 3500:
        # 税后工资:pay_tax
        pay_tax = (pay - pay_safe)
        print(pay_id, end=':'),
        print(format(pay_tax, '.2f'))
    else:
        # 应纳税所得额：pay_out
        pay_out = (pay - pay_safe -a)
        if pay_out < 0:
            pay_in = (pay - pay_safe)
            print(pay_id, end=':'),
            print(format(pay_in, '.2f'))
        elif pay_out > 0 and pay_out <= 1500:
            # 应纳税额：tax_in
            tax_in = (pay_out * 0.03)
            pay_tax = (pay- pay_safe - tax_in)
            print(pay_id, end=':'),
            print(format(pay_tax, '.2f'))

        elif pay_out > 1500 and pay_out <= 4500:
            tax_in = (pay_out * 0.1 -105)
            pay_tax = (pay - pay_safe - tax_in)
            print(pay_id, end=':'),
            print(format(pay_tax, '.2f'))

        elif pay_out > 4500 and pay_out <= 9000:
            tax_in = (pay_out * 0.2 - 555)
            pay_tax = (pay - pay_safe - tax_in)
            print(pay_id, end=':'),
            print(format(pay_tax, '.2f'))

        elif pay_out > 9000 and pay_out <= 35000:
            tax_in = (pay_out * 0.25 -1005)
            pay_tax = (pay - pay_safe - tax_in)
            print(pay_id, end=':'),
            print(format(pay_tax, '.2f'))

        elif pay_out > 35000 and pay_out <= 55000:
            tax_in = (pay_out * 0.3 -2755)
            pay_tax = (pay - pay_safe - tax_in)
            print(pay_id, end=':'),
            print(format(pay_tax, '.2f'))

        elif pay_out > 55000 and pay_out <= 80000:
            tax_in = (pay_out * 0.35 -5505)
            pay_tax = (pay - pay_safe - tax_in)
            print(pay_id, end=':'),
            print(format(pay_tax, '.2f'))

        else:
            tax_in = (pay_out * 0.45 - 13505)
            pay_tax = (pay - pay_safe - tax_in)
            print(pay_id, end=':'),
            print(format(pay_tax, '.2f'))

            



















