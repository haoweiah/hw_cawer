# _*_ coding:utf-8 _*_

import requests
from requests.auth import HTTPBasicAuth
import json
import os
import operator
import smtplib
from email.mime.text import MIMEText
import logging
import re

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='myapp.log',
                    filemode='a'
                    )
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)


class ProjectacrnPullRequest(object):

    def __init__(self, username, userpwd):
        self.base_url = 'https://api.github.com/repos/projectacrn/acrn-hypervisor/pulls'
        self.url = ''
        self.s = requests.Session()
        self.s.auth = HTTPBasicAuth(username, userpwd)

    def send_email(self, subject, content, mail=[]):
        # Send a reminder email
        sender = 'weix.hao@intel.com'
        receivers = ['jinxiax.li@intel.com', 'wenling.zhang@intel.com', 'nanlin.xie@intel.com'] + mail
        msg = MIMEText(content, 'plain', 'utf-8')
        msg['Subject'] = subject
        msg['From'] = sender
        msg['TO'] = ','.join(receivers)
        print(subject)
        print(content)
        print(receivers)
        # try:
        #     s = smtplib.SMTP('smtp.intel.com')
        #     s.sendmail(sender, receivers, msg.as_string())
        #     logging.info('send suess')
        # except smtplib.SMTPException as err:
        #     logging.info('Failed to send mail\n{}'.format(err))

    def acrn_url_info(self, url):
        # request data
        response = self.s.get(url)
        return json.loads(response.text)

    def post_comments(self, url):
        # Post Merge Comments

        body = "Ready to merge"
        response = self.s.post(url, json={'body': body})
        return response.status_code

    def merge_put_request_method(self, merge_url, head):
        # Rebase Merge

        response = self.s.put(merge_url, json={"sha": head, "merge_method": "rebase"})
        return response.text

    def read_file(self):
        try:
            with open('num_dict.json', 'r') as f:
                merge_num = f.read()
            return eval(merge_num)
        except FileNotFoundError as e:
            return {}

    def write_file(self, num_list):
        with open('num_dict.json', 'w') as f:
            f.write(str(num_list))

    def checkon(self, num, commit_url):
        message = self.acrn_url_info(commit_url)['message']
        list = re.findall(r'Tracked-On: #(\d+)', message)
        mail = re.findall(r'Signed-off-by:.*?<(.*?@intel.com)>', message)
        if not list:
            if not mail:
                print('未找到mail 邮件发给谁')
                subject = 'PR %d 未找到mail联系人' % num
                content = 'PR %d 未找到mail联系人， Tracked-On信息未填写' % num
                mail.append('minxia.wang@intel.com')
                self.send_email(subject, content)
            else:
                print('找到mail发邮件', mail)
                subject = 'PR %d 未填写Tracked-On信息' % num
                content = 'PR %d 未填写Tracken-On信息' % num
                mail.append('minxia.wang@intel.com')
                self.send_email(subject, content, mail)
            return False
        issues_num = int(list[0])
        issues_url = "https://api.github.com/repos/projectacrn/acrn-hypervisor/issues/%d/comments" % issues_num
        try:
            body = self.acrn_url_info(issues_url)
            for message in body:
                try:
                    ID = message['body']
                except Exception as e:
                    break
                list = re.findall(r'\[External_System_ID\]', ID)
            if not list:
                print('未找到ID发邮件 需要发送给5个人', mail)
                subject = 'issues 问题'
                content = 'PR {} 的issues {} 没有 External_System_ID '.format(num, issues_num)
                self.send_email(subject, content)
                return False
        except Exception as e:
            print('issuers链接错误发邮件 需要发送给5个人', mail)
            subject = 'issues的连接错误，可能是Tracken-On信息错误'
            content = 'issues的连接错误，可能是Tracken-On信息错误'
            self.send_email(subject, content, mail)
            return False
        print('checkon OK')

    def projectcarn_merge_rebase(self):
        # Parse the json data and execute the method
        read_num_dict = self.read_file()
        merge_num_dict = {}
        send_num_dict = {}
        pulls_json = self.acrn_url_info(self.base_url)
        merge_url = pulls_json[0]['base']['repo']['merges_url']
        for i in range(0, len(pulls_json)):
            head = pulls_json[i]['head']['sha']
            base = pulls_json[i]['base']['ref']
            num = pulls_json[i]['number']
            commits_url = pulls_json[i]['commits_url']
            print(num)
            self.checkon(num, commits_url)
        #     num_url = pulls_json[i]['url']
        #     num = pulls_json[i]['number']
        #     comment_url = pulls_json[i]['comments_url']
        #     statuses_url = pulls_json[i]['statuses_url']
        #     review_url = pulls_json[i]['url'] + '/reviews'
        #     review_json = self.acrn_url_info(review_url)
        #     for review in review_json:
        #         user = review["user"]["login"]
        #         if review.get('state') == "APPROVED" and (user == "anthonyzxu" or user == "dongyaozu"):
        #             check_json = self.acrn_url_info(statuses_url)
        #             if check_json[0]['state'] == 'success':
        #                 merge_num_dict[num] = [0, comment_url]
        #                 send_num_dict[num] = num_url
        #
        # merge_num_list = sorted([key for key in merge_num_dict.keys()])
        # read_num_list = sorted([key for key in read_num_dict.keys()])
        # logging.info('merge_num_list %s' % merge_num_list)
        # logging.info('read_num_list %s' % read_num_list)
        # if not operator.eq(read_num_list, merge_num_list):
        #     # 使用operator判断两个列表是否相同
        #     logging.info("可以rebase编号：%s" % merge_num_list)
        #     self.send_email(json.dumps(send_num_dict))
        #     for num, list in merge_num_dict.items():
        #         if num in read_num_list:
        #             merge_num_dict[num][0] = 1
        #             list[0] = 1
        #         if list[0] == 0:
        #             status_code = self.post_comments(list[1])
        #             merge_num_dict[num][0] = 1
        #             body = "修改成功" if status_code == 201 else "修改失败"
        #             logging.info(body)
        #     self.write_file(merge_num_dict)


if __name__ == '__main__':
    projectacrn_pullrequest = ProjectacrnPullRequest('hw121298@163.com', 'hw!QAZ2wsx')
    projectacrn_pullrequest.projectcarn_merge_rebase()
