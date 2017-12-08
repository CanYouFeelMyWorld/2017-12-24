#-*- coding:utf-8 -*-
import re
import urllib2
import pandas as pd
import csv
#def loadurl(url):
url="http://service.theater.mtime.com/Cinema.api?Ajax_CallBack=true&Ajax_CallBackType=Mtime.Cinema.Services&Ajax_CallBackMethod=GetOnlineMoviesInCity&Ajax_CrossDomain=1&Ajax_RequestUrl=http%3A%2F%2Ftheater.mtime.com%2FChina_Guangdong_Province_Jiangmen%2F&t=201711282231717634&Ajax_CallBackArgument0=380"
user_agent="Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50"
headers={"User-Agent":user_agent}
req=urllib2.Request(url,headers=headers)
response=urllib2.urlopen(req)
html = response.read()
tg_start=html.find('var result_201711282231717634 = { "value":{"movies":[')
if tg_start==-1:
            print ('not find start tag')
            os.exit()
tmp=html[tg_start:-1]
tg_end=tmp.find('],')
if tg_end==-1:
            print ('not find end  tag')
            os.exit()
tmp=tmp[len('var result_201711282231717634 = { "value":{"movies":['):tg_end]
tar_ls=tmp.split("},{")
id_list=[]
for ls in tar_ls:
            ls_t=ls.split(',')
            id= ls_t[0].split(':')[-1]
            id_list.append(id)

message=[]
message1=[]
for id in id_list:
            new_url="http://service.library.mtime.com/Movie.api?Ajax_CallBack=true&Ajax_CallBackType=Mtime.Library.Services&Ajax_CallBackMethod=GetMovieOverviewRating&Ajax_CrossDomain=1&Ajax_RequestUrl=http%3A%2F%2Fmovie.mtime.com%2F227434%2F&t=20171251181240157&Ajax_CallBackArgument0="+id
            req = urllib2.Request(new_url, headers=headers)
            response = urllib2.urlopen(req)
            html1 = response.read()
            message.append(html1)
for i in  message:

    saixaun = re.findall(
        r'"movieTitle":"(.*?)","tweetId":\d,".*?"TotalBoxOffice":"(.*?)","TotalBoxOfficeUnit":"(.*?)","TodayBoxOffice":"(.*?)","TodayBoxOfficeUnit":"(.*?)","ShowDays":(.*?),"EndDate":"(.*?)","FirstDayBoxOffice":"(.*?)","FirstDayBoxOfficeUnit":"(.*?)"',
        i)

    for i in  saixaun:
        # list1=sorted(set(i),key=i.index)
        message1.append(i)
print message

biaoge=pd.DataFrame(message1)
biaoge.columns=['电影','票房','单位','今日票房','单位','上映日期','上映时间','首映票房','单位']
biaoge.to_csv(r'ans020173.csv',sep=',',encoding='gb18030')