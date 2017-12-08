#-*-coding:utf-8 -*-
import urllib2
import re
import os
url="http://service.theater.mtime.com/Cinema.api?Ajax_CallBack=true&Ajax_CallBackType=Mtime.Cinema.Services&Ajax_CallBackMethod=GetOnlineMoviesInCity&Ajax_CrossDomain=1&Ajax_RequestUrl=http%3A%2F%2Ftheater.mtime.com%2FChina_Guangdong_Province_Jiangmen%2F&t=201711282231717634&Ajax_CallBackArgument0=380"
user_agent="Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50"
headers={"User-Agent":user_agent}
req=urllib2.Request(url,headers=headers)
response=urllib2.urlopen(req)
html=response.read()
tg_start=html.find('var result_201711282231717634 = { "value":{"movies":[')
if tg_start==-1:
    print 'not find start tag'
    os.exit()
tmp=html[tg_start:-1]
tg_end=tmp.find('],')
if tg_end==-1:
    print 'not find end  tag'
    os.exit()
tmp=tmp[len('var result_201711282231717634 = { "value":{"movies":['):tg_end]
tar_ls=tmp.split("},{")
for ls in tar_ls:
    ls_t=ls.split(',')
    id= ls_t[0].split(':')[-1]
    title=ls_t[1].split(':')[-1]
    rating=ls_t[2].split(':')[-1]
    if rating=='""':
         print "电影名：" + title +"," + "电影id:" + id +","+"电影评分：" + "0.0"
    else:
         print "电影名："  + title +","+ "电影id:"  + id + ","+"电影评分：" + rating
# print ''.join(tar_ls)
# for t0 in tar_ls:
#     ls_t=t0.split(',')
#     id=ls_t[0].split(":")[-1].split()
#     film=ls_t[-1].split()[-2].strip()
#     dict_film[id]==film
# for t in dict_film:
#     print "id:"+t+"film:"+dict_film[t]
#     print 'ok total:'+len(dict_film)
# # print html