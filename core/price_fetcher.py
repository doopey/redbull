import requests

class PriceFetcher(object):
    def __init__(self, code):
        self.GET_URL = 'http://qt.gtimg.cn/q='
        self.code = code

    def fetch_current_price(self):
        url = self.GET_URL + self.code
        response = requests.get(url)
        if response.status_code != 200:
            print "response status code:", response.status_code
            return None
        text = response.text
        if 'pv_none_match=1' in text:
            print 'code not match:', self.code
            return None
        strs = text.split('~', 6)
        if len(strs) == 7:
            return float(strs[3])
        return None

    def fetch_yesterday_price(self):
        url = self.GET_URL + self.code
        response = requests.get(url)
        if response.status_code != 200:
            print "response status code:", response.status_code
            return None
        text = response.text
        if 'pv_none_match=1' in text:
            print 'code not match:', self.code
            return None
        strs = text.split('~', 6)
        if len(strs) == 7:
            return float(strs[4])
        return None

    def fetch_start_price(self):
        url = self.GET_URL + self.code
        response = requests.get(url)
        if response.status_code != 200:
            print "response status code:", response.status_code
            return None
        text = response.text
        if 'pv_none_match=1' in text:
            print 'code not match:', self.code
            return None
        strs = text.split('~', 6)
        if len(strs) == 7:
            return float(strs[5])
        return None

class SinaPriceFetcher(PriceFetcher):
    def __init__(self, code):
        self.GET_URL = 'http://hq.sinajs.cn/list='
        self.code = code

    def fetch_current_price(self):
        url = self.GET_URL + self.code
        response = requests.get(url)
        if response.status_code != 200:
            print "response status code:", response.status_code
            return None
        text = response.text
        if ',' not in text:
            print 'code not match:', self.code
            return None
        strs = text.split(',', 6)
        if len(strs) == 7:
            return float(strs[3])
        return None

    def fetch_yesterday_price(self):
        url = self.GET_URL + self.code
        response = requests.get(url)
        if response.status_code != 200:
            print "response status code:", response.status_code
            return None
        text = response.text
        if ',' not in text:
            print 'code not match:', self.code
            return None
        strs = text.split(',', 6)
        if len(strs) == 7:
            return float(strs[2])
        return None

    def fetch_start_price(self):
        url = self.GET_URL + self.code
        response = requests.get(url)
        if response.status_code != 200:
            print "response status code:", response.status_code
            return None
        text = response.text
        if ',' not in text:
            print 'code not match:', self.code
            return None
        strs = text.split(',', 6)
        if len(strs) == 7:
            return float(strs[1])
        return None


if __name__ == '__main__':
    sum = 0
    with open('../input.txt', 'r') as f:
        for line in f:
            strs = line.strip().split(',')
            status = 0
            yesterday_price = SinaPriceFetcher(strs[0]).fetch_yesterday_price()
            print "%s,%s,%.2f,%d" %(strs[0], strs[1], yesterday_price, status)# , SinaPriceFetcher(k[0]).fetch_current_price()
            sum += int(strs[1]) * yesterday_price
    print "sum", sum


