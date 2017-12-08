#-*- coding:utf-8 -*-
import  urllib2
import re
import os
import parser
url="http://theater.mtime.com/China_Guangdong_Province_Jiangmen/"
user_agent="Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50"
header={"User-Agent":user_agent}
req=urllib2.Request(url,headers=header)
response=urllib2.urlopen(req)
html=response.read()
# soup=BeautifulSoup(html)
# for link in  soup.find_all("div"):
#     print link
#pattendemo=re.compile(r'<a href=\".+?" title="\s*(.*?).\s*" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover">',re.I)
patten=re.compile(r'<a href=\"(.+?)\" class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text" target="_blank">(.*?)</a>',re.I)
# patten=re.compile(r'<a href=\"(.+?)" target="_blank">\s*(.*?)\s*</a>',re.I)
# patten1=re.compile(r'<h3><a href=\"(.+?)\" target="_blank">\s*(.*?)\s*</a></h3>',re.I)
# # patten=re.compile(r'<a href=\"(.+?)\" title="\s*(.*?)\s*" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover">',re.I)
# patten=re.compile(r'<span class=\".*?\" mid=\".*?\">(.*?)</span>',re.I)
# patten=re.compile(r'<a href=\"(.+?)\" title="\s*(.*?)" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover"><img src=\"(.+?)\" alt="\s*(.*?)"><span class=".+?" mid=".+?">\d.\d</span>',re.I)
# patten=re.compile(r'<span class=\".*?\" mid=\".*?\">.*?</span>',re.I)
item_list = patten.findall(html)
# print html
# print html
# new_item_list=patten1.findall(html)
# print item_list
# item_new_list=sorted(set(item_list),key=item_list.index)#删除列表重复内容
# item_new_list=sorted(set(item_list),key=item_list.index)#删除列表重复内容
# for i in item_new_list:
#          # print i
#          s=i[0]
#          # print i[1]
#          print "电影编号："+s[-7:-1].replace("/","")
#          print "电影名："+i[1]
# # new_len_item_list=bytes(len(item_new_list))
# print "_-_"*50
# print "电影总数："+new_len_item_list
# print "="*100+"即将上映的电影"
# for x in new_item_list:
#     # print x
#     s=x[0]
#     print "电影编号：" + s[-7:-1].replace("/", "")
#     print "电影名：" + x[1]
print "*"*1000
list =[]
for i in item_list:
        if not i in list:
            list.append(i)
            print (''.join(i)).split("/",4)[3]
            print i[1]
# print type("".join(i))


# # print list
# print type(x)
# print type(x.__str__())#转字符串
# print (''.join(x))元组里的东西是字符串可用''.join(x)转换
