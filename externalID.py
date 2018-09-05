# _*_ coding:utf-8 _*_

import requests
from requests.auth import HTTPBasicAuth
import json
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

    def send_email(self, subject, content):
        # Send a reminder email
        # 发送邮件
        sender = 'Integration_auto_merge@intel.com'  # 邮件发送人可以为一个虚拟的邮箱（需要加后缀@...com）
        receivers = ['weix.hao@intel.com', 'minxia.wang@intel.com']
        msg = MIMEText(content, 'plain', 'utf-8')

        msg['Subject'] = subject
        msg['From'] = sender
        msg['TO'] = ','.join(receivers)
        try:
            s = smtplib.SMTP('smtp.intel.com')
            s.sendmail(sender, receivers, msg.as_string())
            logging.info('send suess')
        except smtplib.SMTPException as err:
            logging.info('Failed to send mail\n %s' % err)

    def acrn_url_info(self, url):
        # request data
        response = self.s.get(url)
        return json.loads(response.text)

    def TrackenOn(self, commit_url, html_url):
        # 检查是否TrackOn
        try:
            message = self.acrn_url_info(commit_url)[0]['commit']['message']
            # me_list = re.findall(r'Tracked-On: #(\d+)', message)
            mail = re.findall(r'Signed-off-by:.*?<(.*?@.*?)>', message)
            for email in mail:
                print(email)
                if email[-9:] != 'intel.com':
                    return mail
            return False
        except Exception as e:
            logging.error('commit错误%s link：%s' % (e, html_url))
            return False

    def projectcarn_merge_rebase(self):
        # Parse the json data and execute the method
        send_mail = {}
        pr_close_url = 'https://api.github.com/repos/projectacrn/acrn-hypervisor/pulls'
        kn_close_url = 'https://api.github.com/repos/projectacrn/acrn-kernel/pulls'
        page = 1
        lenth_pulls = 0
        while 1:
            page += 1
            response = self.s.get(kn_close_url, params={"state": "all", "page": page})
            pulls_json = json.loads(response.text)
            lenth_pulls += len(pulls_json)
            if not pulls_json:
                break
            for pull_json in pulls_json:
                num = pull_json['number']
                commits_url = pull_json['commits_url']
                html_url = pull_json['html_url']
                mail = self.TrackenOn(commits_url, html_url)
                if mail:
                    send_mail[num] = [mail, html_url]

        print(send_mail)
        print(lenth_pulls)
        # subject = 'outmail'
        # content = 'outmail %s\n' % send_mail
        # self.send_email(subject, content)


if __name__ == '__main__':
    projectacrn_pullrequest = ProjectacrnPullRequest('hw121298@163.com', 'hw!QAZ2wsx')
    projectacrn_pullrequest.projectcarn_merge_rebase()
