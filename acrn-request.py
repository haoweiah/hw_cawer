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

s = requests.Session()
s.auth=(username, userpwd)

def build_uri(endpoint):
    # 构建url
    return '/'.join([base_url, endpoint])


def better_print(json_str):
    # 让json输出好看点
    return json.dumps(json.loads(json_str), indent=4)


def carn_pulls_info():
    # 获取所有的pulls
    response = s.get(build_uri('repos/jianlaipinan/carn/pulls'))
    return response.text


def json_request():
    response = s.patch(build_uri('user'), auth=('hw121298@163.com', '!QAZ2wsx'), json={'bio': 'this is a test'})
    print(better_print(response.text))
    print(response.request.headers)
    print(response.request.body)
    print(response.status_code)


def merge_post_request_method(merge_url, head):
    # merge 当前分支到主分支
    response = s.put(merge_url, auth=(username, userpwd),
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
    response = s.put(merge_url, headers=headers,
                            json={
                                "sha": head,
                                "merge_method": "rebase",
                            })
    return response.text


def get_comments(url):
    response = s.get(url)
    print(response.text)
    with open('jianlai_comments.json', 'w') as f:
        f.write(response.text)
    print(response.status_code)


def get_commit(url):
    response = s.get(url)
    with open('jianlai_commit.json', 'w') as f:
        f.write(response.text)


def post_comments(url):
    body = "代码评论测试2"

    response = s.post(url, json={'body': body})
    return response.status_code


def jianlaipinan_acrn_request():
    # 解析json数据
    pulls_data = carn_pulls_info()
    with open('jianlai.json', 'w') as f:
        f.write(pulls_data)
    pulls_data = json.loads(pulls_data)
    for i in range(0, len(pulls_data)):
        url = pulls_data[i]['url'] + '/merge'
        num = pulls_data[i]['number']
        sha = pulls_data[i]['head']['sha']
        review_url = pulls_data[i]['review_comment_url'].replace("{/number}", "/%s" % num)
        commit_url = pulls_data[i]['commits_url']
        comment_url = pulls_data[i]['comments_url']
        # get_comments(comment_url)
        # print(comment_url)
        status_code = post_comments(comment_url)
        print(type(status_code))
        print(status_code)
        body = "成功" if status_code == 201 else "失败"
        print(body)
        # merge_url = pulls_data[i]['base']['repo']['merges_url']

        # base = pulls_data[i]['base']['ref']
        # print(url + '\n' + head + '\n' + base)
        # responsetext = merge_put_request_method(url, sha)
        # print(responsetext)


if __name__ == '__main__':
    jianlaipinan_acrn_request()
