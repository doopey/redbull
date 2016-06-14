import time
from price_fetcher import PriceFetcher

def read_input():
    code_count_map = {}
    with open('../input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            strs = line.split(',')
            if len(strs) != 2:
                print 'wrong input:', line
                exit()
            strs[0] = strs[0].strip()
            strs[1] = strs[1].strip()
            code_count_map[strs[0]] = strs[1]
    return code_count_map

def get_value():
    sum_value = 0
    code_count_map = read_input()
    for code in code_count_map:
        pf = PriceFetcher(code)
        price = pf.fetch()
        if price:
            value = int(code_count_map[code]) * price
            sum_value += value
#            print code, value
#    print 'sum_value:', sum_value
    return sum_value

if __name__ == '__main__':
    start_value, end_value, min_value, max_value = 0, 0, 99999999, -99999999
    while True:
        now = time.strftime('%H:%M')
        sum_value = get_value()
        print sum_value
        if sum_value:
            if sum_value < min_value:
                min_value = sum_value
            if sum_value > max_value:
                max_value = sum_value

        if now > '15:01':
            end_value = get_value()
            print 'exit:', start_value, end_value, min_value, max_value
            break
        if now < '09:30':
            start_value = get_value()
        print start_value, end_value, min_value, max_value
        time.sleep(5)
