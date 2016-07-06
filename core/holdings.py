# coding: utf8

class Holdings(object):

    def __init__(self, **kwargs):
        self.holdings = kwargs.get('holdings', []) # 000000,-300,9.00,1
        self.profit = kwargs.get('profit', 0)
        self.stocks = set()
        for k in self.holdings:
            strs = k.split(',')
            stock = strs[0]
            self.stocks.add(stock)

if __name__ == '__main__':
    h = Holdings(profit=132, holdings=['abc,500', 'qwe,1000', 'abc,-300,10.00'])
    print getattr(h, 'stocks')
    print getattr(h, 'profit')
    print getattr(h, 'holdings')
