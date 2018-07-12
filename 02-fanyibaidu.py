# !/usr/bin/env python
# _*_ coding:utf-8 _*_


import urllib2
import urllib
import json


#  POST ajax json数据
#  如果爬虫遇到很棘手的问题 换策略; 手机端

def fanyi_baidu():
    url = 'http://fanyi.baidu.com/basetrans'
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
    }
    keyword = raw_input('请输入翻译的内容:')

    formdata = {
        "query": keyword,
        "from": "zh",
        "to": "en",
    }
    formdata_str = urllib.urlencode(formdata)
    # reuqest
    request = urllib2.Request(url, data=formdata_str, headers=headers)

    response = urllib2.urlopen(request)

    data = response.read()

    # print type(data) str

    # 将翻译的结果输出
    # 1.将字符串 -->dict
    dict_data = json.loads(data)

    # 2. 根据key 获取内容
    result = dict_data['trans'][0]['result'][0][1]

    print result


if __name__ == '__main__':
    fanyi_baidu()
