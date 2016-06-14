import requests

class PriceFetcher(object):
    def __init__(self, code):
        self.GET_URL = 'http://qt.gtimg.cn/q='
        self.code = code

    def fetch(self):
        url = self.GET_URL + self.code
        response = requests.get(url)
        if response.status_code != 200:
            print "response status code:", response.status_code
            return None
        text = response.text
        if 'pv_none_match=1' in text:
            print 'code not match:', self.code
            return None
        strs = text.split('~', 4)
        if len(strs) == 5:
            return float(strs[3])
        return None


if __name__ == '__main__':
    pf = PriceFetcher('sz300219')
    print pf.fetch()
