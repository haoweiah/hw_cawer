# _*_ coding:utf-8 _*_

import requests
from requests.auth import HTTPBasicAuth
import json
import logging
import pymysql

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='myapp.log',
                    filemode='a'
                    )
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-8s: %(levelname)-4s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)


class ProjectacrnPullRequest(object):

    def __init__(self, username, userpwd):
        self.base_url = 'https://api.github.com/repos/projectacrn/acrn-hypervisor/pulls'
        self.url = ''
        self.s = requests.Session()
        self.s.auth = HTTPBasicAuth(username, userpwd)

    def sql_handle(self, sql_dict):
        db = pymysql.connect('localhost', 'root', '123456', 'intelmail')
        cursor = db.cursor()
        sql = 'select email from mail;'
        cursor.execute(sql)
        results = cursor.fetchall()
        result = [x[0] for x in results]
        for email, name in sql_dict.items():
            if email in result:
                continue
            sql = 'INSERT INTO mail (name, email) values("%s", "%s")' % (name, email)
            try:
                cursor.execute(sql)
                db.commit()
            except Exception as e:
                print(e)
                db.rollback()
        db.close()

    def acrn_url_info(self, url):
        # request data
        response = self.s.get(url)
        return json.loads(response.text)

    def searchmail(self, commit_url):
        # 检查是否TrackOn
        try:
            author = self.acrn_url_info(commit_url)[0]['commit']['author']
            return author
        except Exception as e:
            logging.error('commit错误%s' % e)
            return False

    def projectcarn_merge_rebase(self):
        # Parse the json data and execute the method
        sql_mail = {}
        close_url = ['https://api.github.com/repos/projectacrn/acrn-hypervisor/pulls',
                     'https://api.github.com/repos/projectacrn/acrn-kernel/pulls']
        page = 1
        lenth_pulls = 0
        for url in close_url:
            while 1:
                page += 1
                # response = self.s.get(url, params={"state": "all", "page": page})
                response = self.s.get(url)
                pulls_json = json.loads(response.text)
                lenth_pulls += len(pulls_json)
                if not pulls_json:
                    break
                for pull_json in pulls_json:
                    commits_url = pull_json['commits_url']
                    mail = self.searchmail(commits_url)
                    print(mail)
                    if mail is not None:
                        sql_mail[mail['email']] = mail['name']
                break
            print(lenth_pulls)
            self.sql_handle(sql_mail)


if __name__ == '__main__':
    projectacrn_pullrequest = ProjectacrnPullRequest('hw121298@163.com', 'hw!QAZ2wsx')
    projectacrn_pullrequest.projectcarn_merge_rebase()

