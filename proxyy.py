import urllib.request
import random
import getips as ips
iplist = ips.main()         
url = 'http://www.whatismyip.com.tw'
proxy_support = urllib.request.ProxyHandler({'http':random.choice(iplist)})
opener = urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)
reponse = urllib.request.urlopen(url)
html = reponse.read().decode('utf-8')
print(html)
