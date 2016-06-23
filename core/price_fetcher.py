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
    print SinaPriceFetcher('sz300040').fetch_yesterday_price(), SinaPriceFetcher('sz300040').fetch_current_price();
    print SinaPriceFetcher('sz002070').fetch_yesterday_price(), SinaPriceFetcher('sz002070').fetch_current_price();
    print SinaPriceFetcher('sz300219').fetch_yesterday_price(), SinaPriceFetcher('sz300219').fetch_current_price();
    print SinaPriceFetcher('sz300118').fetch_yesterday_price(), SinaPriceFetcher('sz300118').fetch_current_price();
    print SinaPriceFetcher('sz002519').fetch_yesterday_price(), SinaPriceFetcher('sz002519').fetch_current_price();
    print SinaPriceFetcher('sz002340').fetch_yesterday_price(), SinaPriceFetcher('sz002340').fetch_current_price();
    print SinaPriceFetcher('sz002108').fetch_yesterday_price(), SinaPriceFetcher('sz002108').fetch_current_price();
