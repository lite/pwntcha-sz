#!/usr/bin/env python
# coding=utf-8

import os, sys
import base64
import re
import requests
from subprocess import Popen, PIPE, STDOUT

s = requests.session()

headers = {
    'content-type': 'text/x-gwt-rpc; charset=utf-8',
    'Connection': 'keep-alive',
    'X-GWT-Module-Base': 'http://58.210.126.206:9091/QueryVD_test001/peccancyquery/',
    'X-GWT-Permutation': 'F0317D2D24BC0477895D3B40DF9C657C',
    }
        
#from mechanize import Browser, CookieJar
def get_memo(s1, s2):
    # 苏EMV132
    # 0670444 3条违章
    payload = u"7|0|7|http://58.210.126.206:9091/QueryVD_test001/peccancyquery/|973C0FA83C82BE3B3FD3D9E85151BC5E|com.cgs.client.GreetingService|queryObjectZb|java.lang.String/2004016611|queryVehiclePeccancyReady|02\!%s\!%s|1|2|3|4|2|5|5|6|7|" %(s1, s2)
    data = payload.encode('utf8')
    r = s.post("http://58.210.126.206:9091/QueryVD_test001/peccancyquery/greet", data=data, headers=headers)
    m = re.search(',\"\",\"(.+)\",\"1\",', r.text)
    token = m.group(1)
    
    r =  s.get("http://58.210.126.206:9091/QueryVD_test001/viewVerify.jsp?a=1354092211137")
    m = re.search('flashvars.memo = \"(.+)\";', r.text)
    memo = m.group(1)
    return memo, token
    
def get_info_by_captcha(token, captcha):
    payload = u"7|0|7|http://58.210.126.206:9091/QueryVD_test001/peccancyquery/|973C0FA83C82BE3B3FD3D9E85151BC5E|com.cgs.client.GreetingService|queryObjectCl|java.lang.String/2004016611|queryVehiclePeccancy|%s\!%s|1|2|3|4|2|5|5|6|7|" %(token, captcha)
    data = payload.encode('utf8')
    r = s.post("http://58.210.126.206:9091/QueryVD_test001/peccancyquery/greet", data=data, headers=headers)
    return r.text
    
def memo_to_swf(txt, swf):
    with open(swf, 'w') as f:
        f.write(base64.b64decode(txt))
    return swf
    
def get_captcha(swf):
    output,error = Popen("swfdump %s"%(swf), shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT).communicate()
    m = re.search('FRAMELABEL \"F_(\d{6})\"', output)
    return m.group(1)
            
def get_info(s1, s2):
    b64, token = get_memo(s1, s2)
    fn = "b64.swf"
    memo_to_swf(b64, fn)
    captcha = get_captcha(fn)
    return get_info_by_captcha(token, captcha)
    
if __name__ == '__main__':
    print get_info(u"苏EMV132",u"0670444")
    