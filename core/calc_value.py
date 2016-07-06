# -*- coding:utf8 -*-
import time
import os
from price_fetcher import PriceFetcher
from price_fetcher import SinaPriceFetcher
from holdings import Holdings

def init_input():
    init_dict = {}
    for h in read_input().holdings:
        strs = h.split(',')
        code = strs[0]
        operation_count = int(strs[1])
        if code not in init_dict:
            init_dict[code] = operation_count
        else:
            init_dict[code] += operation_count
    with open('../input.txt', 'w') as f:
        sum = 0
        for key in init_dict:
            if init_dict[key] > 0:
                line = key + ',' + str(init_dict[key]) + ',' + str(SinaPriceFetcher(key).fetch_yesterday_price()) + ',0'
                f.write(line + '\n')
                sum += SinaPriceFetcher(key).fetch_yesterday_price() * init_dict[key]
        print 'sum', sum

def read_input():
    holdings = []
    with open('../input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            strs = line.split(',')
            if len(strs) != 4:
                print 'wrong input:', line
                exit()
            if strs[3] == '-1': # 停
                continue
            holdings.append(line)
    return Holdings(holdings = holdings)

def read_cache():
    output_file = '../output.txt'
    if not os.path.isfile(output_file):
        return None
    cache = ''
    ctime = time.strftime("%Y-%m-%d", time.localtime(int(os.path.getctime(output_file))))
    today = time.strftime("%Y-%m-%d", time.localtime())
    if ctime == today:
        with open(output_file, 'r') as f:
            cache = f.readline().strip()
    return cache

def get_value():
    holdings = read_input()
    profit = 0
    for h in getattr(holdings, 'holdings'):
        strs = h.split(',')
        code = strs[0]
        operation_count = int(strs[1])
        operation_price = float(strs[2])
        status = strs[3]
        pf = SinaPriceFetcher(code)
        current_price = pf.fetch_current_price()
        if current_price:
            profit += (current_price - operation_price) * operation_count
        if status == '1':
            opertation_amount = operation_count * operation_price
            if abs(opertation_amount * 0.0025) < 5:
                profit += 5
            else:
                profit += opertation_amount * 0.0025
            if opertation_amount < 0:
                profit -= opertation_amount * 0.001
    setattr(holdings, 'profit', profit)
    return holdings

# to be completed
def init_input():
    new_input_list = []
    with open('../input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            strs = line.split(',')
            code = strs[0]
            pf = SinaPriceFetcher(code)
            current_price = pf.fetch_current_price()
            

if __name__ == '__main__':
    print "--------", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    start_value, end_value, min_value, max_value = 0, 0, 99999999, -99999999
    cache = read_cache()
    if cache:
        strs = cache.split(',')
        if len(strs) == 4:
            start_value, end_value, min_value, max_value = float(strs[0].strip()), float(strs[1].strip()), float(strs[2].strip()), float(strs[3].strip())
            print start_value, end_value, min_value, max_value
        else:
            print 'wrong format'

    # init input.txt
    try:
        while True:
            now = time.strftime('%H:%M')
            if now == '09:27':
                init_input()
                time.sleep(60)
            if now < '09:28' or (now > '11:30' and now < '13:00'):
                print "now:", now
                time.sleep(60)
                continue
    
            h = get_value()
            profit = getattr(h, 'profit')
            print profit
            if profit:
                if profit < min_value:
                    min_value = profit
                if profit > max_value:
                    max_value = profit
    
            if now > '15:01':
                end_value = profit
                print 'exit:', start_value, end_value, min_value, max_value
                exit()
            if now < '09:29':
                start_value = profit
            print start_value, end_value, min_value, max_value
            time.sleep(5)

    except (KeyboardInterrupt, SystemExit):
        with open('../output.txt', 'w') as f:
            record = '%s,%s,%s,%s' %(start_value, end_value, min_value, max_value)
            f.write(record + '\n')

