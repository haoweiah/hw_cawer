import requests
import urllib
from urllib import parse, request


def requests_base_use():
    # url = 'http://www.github.com'
    url = 'https://api.github.com/repos/projectacrn/acrn-hypervisor/pulls/687'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
    params = {"email": "hw@121298@163.com", "password": "!QAZ2wsx"}
    # params_str = parse.urlencode(params)
    # request.Request(url, data=params, headers=headers)
    url_reviews = url + '/reviews'
    print(url_reviews)
    r = requests.get(url_reviews)

    with open('acrn.json', 'w') as f:
        f.write(r.text)
    res = requests.post('https://api.github.com/repos/jianlaipinan/acrn/merges',)
    print(res.text)

if __name__ == '__main__':
    requests_base_use()
