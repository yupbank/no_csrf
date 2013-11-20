#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
no_csrf.py
Author: yupbank
Email:  yupbank@gmail.com

Created on
2013-11-18
'''
import requests
from urlparse import urlparse
from slow_it import slow

def nicer_get(url, *args, **kwagrs):
    parsed_uri = urlparse(url)
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    headers = kwagrs.get('headers', {})
    if 'User-Agent' not in headers:
        headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36'
    res = requests.get(url, headers=headers)
    Referer = res.url
    cookies = res.cookies.get_dict()
    headers.update(dict(Referer = Referer))
    if 'cookies' not in kwagrs:
        kwagrs.update(dict(cookies = cookies))
    @slow()
    def _(url, *args, **kwagrs):
        real_res = requests.get(url, *args, **kwagrs)
        cookies = real_res.cookies.get_dict()
        Referer = real_res.url
        return real_res
    return _

if __name__ == '__main__':
    main()
