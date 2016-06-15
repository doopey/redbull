import time
from price_fetcher import PriceFetcher
from holdings import Holdings

def read_input():
    holdings = []
    with open('../input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            strs = line.split(',')
            if len(strs) != 3:
                print 'wrong input:', line
                exit()
            holdings.append(line)
    return Holdings(holdings = holdings)

def get_value():
    holdings = read_input()
    profit = 0
    for h in getattr(holdings, 'holdings'):
        strs = h.split(',')
        code = strs[0]
        operation_count = int(strs[1])
        operation_price = float(strs[2])
        pf = PriceFetcher(code)
        current_price = pf.fetch_current_price()
        if current_price:
            profit += (current_price - operation_price) * operation_count
        print profit
    setattr(holdings, 'profit', profit)
    return holdings

if __name__ == '__main__':
    start_value, end_value, min_value, max_value = 0, 0, 99999999, -99999999
    while True:
        now = time.strftime('%H:%M')
        h = get_value()
        profit = getattr(h, 'profit')
        if profit:
            if profit < min_value:
                min_value = profit
            if profit > max_value:
                max_value = profit

        if now > '15:01':
            end_value = profit
            print 'exit:', start_value, end_value, min_value, max_value
            break
        if now < '09:30':
            start_value = get_value()
        print start_value, end_value, min_value, max_value
        time.sleep(5)
