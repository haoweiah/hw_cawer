# _*_ coding:utf8 _*_
import os
import time

try:
    import requests
except ImportError as e:
    status = os.system('pip install requests')
    while 1:
        list = os.popen('pip freeze').read()
        print(list)
        time.sleep(3)
        if 'requests' in list:
            break
import json

base_url = 'https://api.github.com'
username = 'hw121298@163.com'
userpwd = '!QAZ2wsx'


def build_uri(endpoint):
    # 构建url
    return '/'.join([base_url, endpoint])


def better_print(json_str):
    # 让json输出好看点
    return json.dumps(json.loads(json_str), indent=4)


def carn_pulls_info():
    # 获取所有的pulls
    response = requests.get(build_uri('repos/jianlaipinan/carn/pulls'))
    return response.text


def json_request():
    response = requests.patch(build_uri('user'), auth=('hw121298@163.com', '!QAZ2wsx'), json={'bio': 'this is a test'})
    print(better_print(response.text))
    print(response.request.headers)
    print(response.request.body)
    print(response.status_code)


def merge_post_request_method(merge_url, head):
    # merge 当前分支到主分支
    response = requests.put(merge_url, auth=(username, userpwd),
                            json={"commit_title": "this is commit test",
                                  "commit_message": "this is add commit test",
                                  "sha": head,
                                  "merge_method": "rebase"})
    if response.status_code == 200:
        print('merge sueecss')
    return response.status_code


def merge_put_request_method(merge_url, head):
    # merge 当前分支到主分支
    headers = {"Authorization": "token 4ea84e0fe94fff027bdb78c949d0897b911b8b8e",
               "Accept": "application/vnd.github.polaris-preview"
               }
    response = requests.put(merge_url, headers=headers,
                            json={
                                "sha": head,
                                "merge_method": "rebase",

                            }
                            )
    if response.status_code == 200:
        print(response.text)
    return response.status_code


def jianlaipinan_acrn_request():
    # 解析json数据
    pulls_data = json.loads(carn_pulls_info())
    with open('jianlai.json','w') as f:
        f.write(json.dumps(pulls_data))
    for i in range(0, len(pulls_data)):
        url = pulls_data[i]['url'] + '/merge'
        # merge_url = pulls_data[i]['base']['repo']['merges_url']
        head = pulls_data[i]['head']['sha']
        base = pulls_data[i]['base']['ref']

        print(url + '\n' + head + '\n' + base)
        status_code = merge_put_request_method(url, head)
        print(status_code)


if __name__ == '__main__':
    jianlaipinan_acrn_request()
    # json_request()
