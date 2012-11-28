# captcha

pwntcha for http://58.210.126.206:9091/QueryVD_test001/

# prepare
 
swfdump

+ download swfdump from http://www.swftools.org/download.html
+ compile and test it with b64.swf, then put the same directory with b64.swf

server

+ install python 2.7
+ install pip(or virtualenv)
+ pip install -r requirements.txt

# start server

    python server

# test

    curl http://127.0.0.1:5000/captcha?s1=苏EMV132&&s2=0670444