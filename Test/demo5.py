#-*- coding:utf-8 -*-
import urllib2
import re
url="http://movie.mtime.com/70233/"
user_agent="Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50"
header={"User-Agent":user_agent}
req=urllib2.Request(url,headers=header)
response=urllib2.urlopen(req)
html=response.read()
pattern=re.compile(r'<dt>.*?</dt>',re.I)
item_list=pattern.findall(html)
# for i in  item_list:
#     print i
print item_list