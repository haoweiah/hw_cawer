# _*_ coding:utf8 _*_
import requests
import json

base_url = 'https://api.github.com'
username = 'hw121298@163.com'
userpwd = '!QAZ2wsx'


def build_uri(endpoint):
    return '/'.join([base_url, endpoint])


def better_print(json_str):
    return json.dumps(json.loads(json_str), indent=4)


def request_method():
    response = requests.get(build_uri('user/emails'), auth=('hw121298@163.com', '!QAZ2wsx'))
    print(response.url)
    print(better_print(response.text))


def carn_pulls_info():
    response = requests.get(build_uri('repos/jianlaipinan/carn/pulls'))
    return response.text


def json_request():
    response = requests.patch(build_uri('user'), auth=('hw121298@163.com', '!QAZ2wsx'), json={'bio': 'this is a test'})
    print(better_print(response.text))
    print(response.request.headers)
    print(response.request.body)
    print(response.status_code)


def merge_request_method(merge_url,head,base):
    response = requests.post(merge_url, auth=(username, userpwd), json={"base":base,"head":head})
    if response.status_code == 201:
        print('merge sueecss')
    return response.status_code


def jianlaipinan_acrn_request():
    # response = requests.get(build_uri('repos/projectacrn/acrn-hypervisor/pulls'))
    pulls_data = json.loads(carn_pulls_info())
    for i in range(0, len(pulls_data)):
        merge_url = pulls_data[i]['base']['repo']['merges_url'].encode('utf-8')
        head = pulls_data[i]['head']['sha'].encode('utf-8')
        base = pulls_data[i]['base']['ref'].encode('utf-8')
        print(merge_url,head,base)
        status_code = merge_request_method(merge_url,head,base)
        print(status_code)


if __name__ == '__main__':
    jianlaipinan_acrn_request()
