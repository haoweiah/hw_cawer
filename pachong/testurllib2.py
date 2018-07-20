# coding:utf-8
import urllib
word = {"wd":"测试"}
encode = urllib.urlencode(word)

print(encode)
print(word)