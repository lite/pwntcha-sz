#!/usr/bin/env python
# coding=utf-8

from flask import Flask, url_for,json, request
import captcha 
app = Flask(__name__)
    
@app.route('/captcha')
def api_captcha():
    s1 = request.args['s1'] 
    s2 = request.args['s2']
    print "%s: %s" %(s1, s2) 
    return captcha.get_info(s1, s2)
    
@app.route('/')
def api_root():
    return "works"
                 
if __name__ == '__main__':
    app.run()
        
#curl -H "Content-type: application/json" http://127.0.0.1:5000/captcha?s1=苏EMV132&s2=0670444
#curl -H "Content-type: application/json" http://127.0.0.1:5000/