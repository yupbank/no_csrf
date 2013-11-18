#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
demo.py
Author: yupbank
Email:  yupbank@gmail.com

Created on
2013-11-18
'''
from no_csrf import nicer_get


def main():
    demo_url = 'http://www.appannie.com/apps/ios/top-table/20131117-US-36-iphone/?p=%s-&h=23&iap=undefined'
    init_url = demo_url%1
    headers = {
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36',
            'Host':'www.appannie.com',
            'Connection':'keep-alive',
            'DNT':'1',
            'X-Requested-With':'XMLHttpRequest',
            }
    new_get = nicer_get(init_url, headers=headers)
    for i in range(1, 10):
        request_url = demo_url%i
        nicer_res = new_get(request_url, headers=headers)
        print nicer_res


if __name__ == '__main__':
    main()
