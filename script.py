import os

proxy = 'http://4d7eb21cc7a5a44f865362fd7276f04a:5b0bd2a34a918a3cb2c360cd3d3a4c4c@199.189.86.111:9500'

os.environ['http_proxy'] = proxy
os.environ['HTTP_PROXY'] = proxy
os.environ['https_proxy'] = proxy
os.environ['HTTPS_PROXY'] = proxy

from urllib.request import urlopen
html = urlopen("http://ipv4.icanhazip.com/").read()
print(html)
