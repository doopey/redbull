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
    for k in [('sz300040', 2000), ('sz300219', 1000), ('sz300118', 600), ('sz002519', 800), ('sz002340', 3000), ('sz002722',200), ('sh603600', 200), ('sz300256', 600), ('sz300230', 300)]:
        status = 0
        yesterday_price = SinaPriceFetcher(k[0]).fetch_yesterday_price()
        print "%s,%d,%.2f,%d" %(k[0], k[1], yesterday_price, status)# , SinaPriceFetcher(k[0]).fetch_current_price()
        sum += k[1] * yesterday_price
    print "sum", sum


