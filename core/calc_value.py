from price_fetcher import PriceFetcher

code_count_map = {}

def read_input():
    with open('../input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            strs = line.split(',')
            if len(strs) != 2:
                print 'wrong input:', line
                exit()
            code_count_map[strs[0]] = strs[1]


read_input()
for code in code_count_map:
    pf = PriceFetcher(code)
    price = pf.fetch()
    if price:
        value = int(code_count_map[code]) * price
        print code, value
