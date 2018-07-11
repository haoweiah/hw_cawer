# !/usr/bin/env python
# _*_ coding:utf-8 _*_


import urllib2

def renren_profile_data():

    # 登录自己的人人网账号--> 邓永杰数据
    url = 'http://www.renren.com/410043129/profile'

    #  手动添加 后台需要认证的 cookie
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
        'Cookie':'anonymid=jelikm2r-dmfdi6; _r01_=1; depovince=GW; _de=BF09EE3A28DED52E6B65F6A4705D973F1383380866D39FF5; ln_uact=mr_mao_hacker@163.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn421/20171230/1635/main_JQzq_ae7b0000a8791986.jpg; jebecookies=ffefe608-c58b-4e82-b096-fb8c76e14859|||||; JSESSIONID=abcRwSGC27Nx7-MnC8Skw; ick_login=4fd22db8-3927-417d-821b-80f3e79cc436; jebe_key=c1f05c91-cd19-4ef8-a08a-4c464fb39bd9%7Cc13c37f53bca9e1e7132d4b58ce00fa3%7C1523282455415%7C1%7C1523319950318; p=b3fe0cd6659ef489129dbf202675c0859; first_login_flag=1; t=96d07b12b220820713a0e4c1cf4e23c19; societyguester=96d07b12b220820713a0e4c1cf4e23c19; id=327550029; xnsid=5283a0d8; loginfrom=syshome; ch_id=10016; wp_fold=0'
    }

    request = urllib2.Request(url, headers=headers)

    response = urllib2.urlopen(request)

    data = response.read()

    with open('06renren.html', 'w') as f:
        f.write(data)


if __name__ == '__main__':
    renren_profile_data()