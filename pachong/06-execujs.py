# !/usr/bin/env python
# _*_ coding:utf-8 _*_


import execjs

if __name__ == '__main__':
    js_one = "'a b c'.split(' ')"

    result = execjs.eval(js_one)

    # 方法
    js_method = """
        function fnSum(a,b){
            return a + b
        }
    """
    method = execjs.compile(js_method)
    result = method.call("fnSum", 10, 30)

    print result
