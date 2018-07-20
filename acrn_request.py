# _*_ coding:utf-8_*_

import requests
import json


class ProjectacrnPullRequest(object):
    base_url = 'https://api.github.com/repos/projectacrn/acrn-hypervisor/'

    def __init__(self, username, userpwd):
        self.url = ''
        self.username = username
        self.userpwd = userpwd

    def acrn_pulls_info(self, url):
        # 获取数据
        response = requests.get(url)
        return json.loads(response.text)

    def merge_request_method(self, merge_url, head, base):
        # merge当前分支到主分支
        response = requests.post(merge_url, auth=(self.username, self.userpwd), json={'base': base, 'head': head})
        if response.status_code == 201:
            print('merge sueecss')
        else:
            print(response.status_code, 'merge fail')

    def projectcarn_merge(self):
        # 解析json数据
        pulls_json = self.acrn_pulls_info(self.url)
        with open('pull_json.json', 'w') as f:
            f.write(json.dumps(pulls_json))
        merge_url = pulls_json[0]['base']['repo']['merges_url']

        for i in range(0, len(pulls_json)):
            head = pulls_json[i]['head']['sha']
            base = pulls_json[i]['base']['ref']
            num = pulls_json[i]['number']
            statuses_url = pulls_json[i]['statuses_url']
            review_url = self.base_url + 'pulls/%s/reviews' % num
            review_json = self.acrn_pulls_info(review_url)
            check_json = self.acrn_pulls_info(statuses_url)
            if len(review_json) != 0 and review_json[0].get('state') == "APPROVED":
                print(str(num) + '\n' + head + '\n' + base)


if __name__ == '__main__':
    projectacrn_pullrequest = ProjectacrnPullRequest('hw121298@163.com', '!QAZ2wsx')
    projectacrn_pullrequest.url = projectacrn_pullrequest.base_url + 'pulls'
    projectacrn_pullrequest.projectcarn_merge()
