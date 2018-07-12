# !/usr/bin/env python
# _*_ coding:utf-8 _*_


import pytesseract
from PIL import Image

if __name__ == '__main__':
    # 1.读取图片
    image_data = Image.open('test.jpg')

    # 2.识别图片
    text = pytesseract.image_to_string(image_data)

    image_data_chi = Image.open('排序算法.png')
    chi_text = pytesseract.image_to_string(image_data_chi, lang="chi_sim")

    print(chi_text)
