#-*-coding:utf-8 -*-
import urllib2
import re
url="https://movie.douban.com/chart"
user_agent="Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50"
headers={"User-Agent":user_agent}
req=urllib2.Request(url,headers=headers)
response=urllib2.urlopen(req)
html=response.read()

pattern=re.compile(r'<span class="rating_nums">\d.\d</span>',re.I)
item_list=pattern.findall(html)
print item_list