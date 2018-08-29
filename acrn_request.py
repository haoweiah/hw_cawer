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

    def send_email(self, num_dict):
        # Send a reminder email
        sender = 'weix.hao@intel.com'
        receivers = ['jinxiax.li@intel.com', 'wenling.zhang@intel.com']
        subject = 'PR rebase list'
        content = 'PR list {}'.format(num_dict)
        msg = MIMEText(content, 'plain', 'utf-8')
        msg['Subject'] = subject
        msg['From'] = sender
        msg['TO'] = ','.join(receivers)
        try:
            s = smtplib.SMTP('smtp.intel.com')
            s.sendmail(sender, receivers, msg.as_string())
            logging.info('send suess')
        except smtplib.SMTPException as err:
            logging.info('Failed to send mail\n{}'.format(err))

    def acrn_pulls_info(self, url):
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

    def checkon(self, body):
        pass

    def projectcarn_merge_rebase(self):
        # Parse the json data and execute the method
        read_num_dict = self.read_file()
        merge_num_dict = {}
        send_num_dict = {}
        pulls_json = self.acrn_pulls_info(self.base_url)
        merge_url = pulls_json[0]['base']['repo']['merges_url']
        for i in range(0, len(pulls_json)):
            head = pulls_json[i]['head']['sha']
            base = pulls_json[i]['base']['ref']
            num_url = pulls_json[i]['url']
            num = pulls_json[i]['number']
            comment_url = pulls_json[i]['comments_url']
            statuses_url = pulls_json[i]['statuses_url']
            review_url = pulls_json[i]['url'] + '/reviews'
            review_json = self.acrn_pulls_info(review_url)
            for review in review_json:
                user = review["user"]["login"]
                if review.get('state') == "APPROVED" and (user == "anthonyzxu" or user == "dongyaozu"):
                    check_json = self.acrn_pulls_info(statuses_url)
                    if check_json[0]['state'] == 'success':
                        merge_num_dict[num] = [0, comment_url]
                        send_num_dict[num] = num_url

        merge_num_list = sorted([key for key in merge_num_dict.keys()])
        read_num_list = sorted([key for key in read_num_dict.keys()])
        logging.info('merge_num_list %s' % merge_num_list)
        logging.info('read_num_list %s' % read_num_list)
        if not operator.eq(read_num_list, merge_num_list):
            logging.info("可以rebase编号：%s" % merge_num_list)
            self.send_email(json.dumps(send_num_dict))
            for num, list in merge_num_dict.items():
                if num in read_num_list:
                    merge_num_dict[num][0] = read_num_dict[num][0]
                if list[0] == 0:
                    # status_code = self.post_comments(comment_url)
                    status_code = self.post_comments(list[1])
                    merge_num_dict[num][0] = 1
                    body = "修改成功" if status_code == 201 else "修改失败"
                    logging.info(body)
            self.write_file(merge_num_dict)


if __name__ == '__main__':
    projectacrn_pullrequest = ProjectacrnPullRequest('wenlingz', '68e5f1a119e3eab70c93729d6229a4af8e8bac03')
    projectacrn_pullrequest.projectcarn_merge_rebase()
