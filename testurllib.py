import os
import urllib,urllib2


# data = os.popen('curl https://api.github.com/repos/projectacrn/acrn-hypervisor/pulls/597/reviews')
# print(data)
# with open('a.txt','w') as f:
#     f.write(str(data))
# print(type(data))
word = {"q":"is:open+is:pr"}
word = urllib.urlencode(word)
url = 'https://api.github.com/repos/projectacrn/acrn-hypervisor/pulls?'+word
req = urllib2.Request(url = url)
res = urllib2.urlopen(req)
res = res.read()
with open('a.txt', 'w') as f:
    f.write(str(res))
print(res)
