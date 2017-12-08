#-*- coding:utf-8 -*-
import re
import urllib2
import pandas as pd
import csv
# def loadurl(url):
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
            # new_url="http://service.library.mtime.com/Movie.api?Ajax_CallBack=true&Ajax_CallBackType=Mtime.Library.Services&Ajax_CallBackMethod=GetMovieOverviewRating&Ajax_CrossDomain=1&Ajax_RequestUrl=http%3A%2F%2Fmovie.mtime.com%2F227434%2F&t=20171251181240157&Ajax_CallBackArgument0="+id
            id_list.append(id)
            # req = urllib2.Request(new_url, headers=headers)
            # response = urllib2.urlopen(req)
            # html1 = response.read()
message=[]
for id in id_list:
            new_url="http://service.library.mtime.com/Movie.api?Ajax_CallBack=true&Ajax_CallBackType=Mtime.Library.Services&Ajax_CallBackMethod=GetMovieOverviewRating&Ajax_CrossDomain=1&Ajax_RequestUrl=http%3A%2F%2Fmovie.mtime.com%2F227434%2F&t=20171251181240157&Ajax_CallBackArgument0="+id
            req = urllib2.Request(new_url, headers=headers)
            response = urllib2.urlopen(req)
            html1 = response.read()
            message.append(html1)
            # print tg_start1
# print message
message1=[]
for i in  message:
            tg_start=i.find('","I')
            tmp=i[tg_start:-1]
            tg_end=tmp.find(',"topList":')
            body=tmp[len('","I'):tg_end]
            # print body
            tg_start1=body.find('P"')
            tmp1=body[tg_start1:-1]
            tg_end1=tmp1.find('},"error":null};var movieOverviewRatingResult=result_2017125118124015')
            body1=tmp1[len('0'):tg_end1]
            tg_start2=body1.find(':')
            tmp2=body1[tg_start2:-1]
            tg_end2=tmp2.find(',"FirstDayBoxOffice":"2507.61","FirstDayBoxOfficeUnit":"万"}},"error":null};var movieOverviewRatingResult=result_20171251181240')
            body2=tmp2[len(':'):tg_end2]
            tg_start3=body2.find('0')
            tmp3=body2[tg_start3:-1]
            tg_end3=tmp3.find('"error":null};var movieOverviewRatingResult=result_2017125118')
            body3=tmp3[len(','):tg_end3]

            # saixuan=re.findall(r'"movieTitle":(".*?"),"tweetId":0,"userLastComment":"","userLastCommentUrl":"","releaseType":\d,"boxOffice":{"Rank":\d,"TotalBoxOffice":"(.*?)","TotalBoxOfficeUnit":"(.*?)","TodayBoxOffice":".*?","TodayBoxOfficeUnit":".*?","ShowDays":\d,"EndDate":".*?"',body3)
            saixaun=re.findall(r'"movieTitle":(".*?"),"tweetId":\d,".*?"TotalBoxOffice":(".*?"),"TotalBoxOfficeUnit":(".*?"),"TodayBoxOffice":(".*?)","TodayBoxOfficeUnit":(".*?"),"ShowDays":(.*?),"EndDate":(".*?"),"FirstDayBoxOffice":(".*?"),"FirstDayBoxOfficeUnit":',body3)

            message1.append(saixaun)

print message1

if message1 ==1:

    biaoge=pd.DataFrame(message1)
    biaoge.columns=['电影','票房','单位','今日票房','单位','上映日期','首映票房','aaa']
    biaoge.to_csv(r'ans020172.csv',sep=',',encoding='gb18030')
                    #
            # tg_start=i.find('"movieTitle":')
            # tmp=i[tg_start:-1]
            # tg_end=tmp.find(',')
            # movietitle=tmp[len('"movieTitle":'):tg_end]
            # print movietitle
            # tg_start1=i.find('"TotalBoxOffice":')
            # tmp1=i[tg_start1:-1]
            # tg_end1=tmp1.find('"TodayBoxOffice":')
            # piaofan=tmp1[len('"TotalBoxOffice":'):tg_end1]
            # print piaofan
            # message1.append(movietitle)
            #     with open("test.csv","w")as csvfile:
            #         writer=csv.writer(csvfile)
            #         writer.writerow(["票房","单位"])
            #         writer.writerow(i)
            # print "电影：",movietitle,"票房:",
                        # for i in piaofan:
#             #


# print message1
# biaoge=pd.DataFrame(message1)
# biaoge.columns=['电影']
# biaoge.to_csv(r'demo1.csv',sep=',',encoding='utf-8')
# if __name__=="__main__":
#     loadurl(url=r"http://service.theater.mtime.com/Cinema.api?Ajax_CallBack=true&Ajax_CallBackType=Mtime.Cinema.Services&Ajax_CallBackMethod=GetOnlineMoviesInCity&Ajax_CrossDomain=1&Ajax_RequestUrl=http%3A%2F%2Ftheater.mtime.com%2FChina_Guangdong_Province_Jiangmen%2F&t=201711282231717634&Ajax_CallBackArgument0=380")
