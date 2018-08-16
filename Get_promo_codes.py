# -*- coding:utf-8 -*-
# Author: 搬瓦工优惠网（bwgyhw.com）
# Date: 2018/8/16
# Time: 18:46

import csv
import re
import time

import requests

BWH_PROMO_CODE_URL = 'https://bwh1.net/cart.php?a=add&pid=15'
BWH_CHECK_DISCOUNT_URL = 'https://bwh1.net/cart.php?a=view'
CODES = []


def regex_promo_code():
    code_html = requests.post(BWH_PROMO_CODE_URL).text
    code = re.search(r'Try this promo code: (\w*)', code_html)
    print(code[1])
    return code[1]


def check_promo_code(code):
    data = {'promocode': code}
    check_html = requests.post(BWH_CHECK_DISCOUNT_URL, data).text
    discount = re.search(r'- ([\d\.]+)%', check_html)
    return discount[0]


def save_to_file(code, discount):
    with open('codes.csv', "a") as file:
        writer = csv.writer(file)
        writer.writerow([code, discount])


if __name__ == "__main__":
    while True:
        g_code = regex_promo_code()
        g_discount = check_promo_code(g_code)
        if g_code not in CODES:
            CODES.append(g_code)
            save_to_file(g_code, g_discount)
        time.sleep(5)
