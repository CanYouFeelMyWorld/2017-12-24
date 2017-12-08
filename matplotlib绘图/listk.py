#-*- coding:utf-8 -*-
import urllib2
import re
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def get_id():
    url='http://service.theater.mtime.com/Cinema.api?Ajax_CallBack=true&Ajax_CallBackType=Mtime.' \
        'Cinema.Services&Ajax_CallBackMethod=GetOnlineMoviesInCity&Ajax_CrossDomain=1&Ajax_RequestUrl' \
        '=http%3A%2F%2Ftheater.mtime.com%2FChina_Guangdong_Province_Jiangmen%2F&t=201711298441987477&Ajax_' \
        'CallBackArgument0=380'
    user_agent= 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrom' \
                'e/57.0.2987.98 Safari/537.36 LBBROWSER'
    req = urllib2.Request(url=url,headers={'User-Agent':user_agent})
    webpage = urllib2.urlopen(req)
    strw = webpage.read()
    tg_start = strw.find('result_201711298441987477 = { "')
    if tg_start == -1:
        print 'not find start'
        os._exit(0)
    tmp = strw[tg_start:-1]
    tg_end = tmp.find(';')
    if tg_end == -1:
        print 'not find end'
        os._exit()
    tmp = tmp[len('result_201711298441987477 = { "'):tg_end]
    tar_ls = tmp.split("},{")
    item_id = {}
    for t0 in tar_ls:
        ls_t = t0.split(',')
        # print ls_t
        # rating = ls_t[2].split('"')[3]
        id = ls_t[0].split(':')[-1].strip()
        item_id[id] = id
    return item_id
for t in get_id():
    new_url = 'http://service.library.mtime.com/Movie.api?Ajax_CallBack=true&Ajax_CallBackType=Mtim' \
              'e.Library.Services&Ajax_CallBackMethod=GetMovieOverviewRating&Ajax_CrossDomain=1&Ajax_' \
              'RequestUrl=http%3A%2F%2Fmovie.mtime.com%2F227434%2F&t=2017125175697979&Ajax_CallBackAr' \
              'gument0=' + t
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrom' \
                 'e/57.0.2987.98 Safari/537.36 LBBROWSER'
    req = urllib2.Request(url=new_url, headers={'User-Agent': user_agent})
    webpage = urllib2.urlopen(req)
    strw = webpage.read()
    tg_start = strw.find('result_2017125175697979 = { "')
    if tg_start == -1:
        print 'not find start'
        os._exit(0)
    tmp = strw[tg_start:-1]
    tg_end = tmp.find(';')
    if tg_end == -1:
        print 'not find end'
        os._exit()
    tmp = tmp[len('result_2017125175697979 = { "'):tg_end]
    pan = tmp.find(',"hotValue":')
    pan_list = []
    if pan == -1:
         pan = tmp.split(',"error"')[0]
         pan_list.append(pan)
    else:
        pan = tmp.split(',"error"')[0].split(',"hotValue":')[0]
        pan_list.append(pan)
    # one = tmp.split(',"error"')[0]
    a = "".join(pan_list)
    pan2 = a.find(',"boxOffice":')
    pan_list2 = []
    if pan2 == -1:
        continue
    else:
        first = a.split(':{')[2]
        movie_id = first.split('},')[0].split(':')[1].split(',')[0]
        movie_ping = first.split('},')[0].split(':')[2].split(',')[0]
        movie_title = first.split('},')[1].split(':')[1].split(',')[0]
        second = a.split(':{')[3]
        TB1 = second.split(',')[1].split(':')[1].split('"')[1]
        TB2 = second.split(',')[2].split(':')[1].split('"')[1]
        DB1 = second.split(',')[3].split(':')[1].split('"')[1]
        DB2 = second.split(',')[4].split(':')[1].split('"')[1]
        # one = re.findall(r'value":{"isRelease":true,"movieRating":{"MovieId":(.*?).*?"movieTitle":(.*?).*?',first)
        # two = re.findall(r'{.*?"TotalBoxOffice":"(.*?)".*?万","TodayBoxOffice":"(.*?)".*?}',second)
        # print two
        TotalBoxOffice = TB1 + TB2
        TodayBoxOffice = DB1 + DB2

        # print second
        data = []

        # data.append(movie_id)
        # data.append(movie_ping)
        # data.append(movie_title)
        # data.append(TotalBoxOffice)
        # data.append(TodayBoxOffice)
        # 这是写出TXT
        # strx = movie_id + "," + movie_title + "," + movie_ping + "," + TotalBoxOffice + "," + TodayBoxOffice + ";"
        # data.append(strx)
        # data1 =[]
        # with open('k.txt','a')as f:
        #     for tag in data:
        #         for i in tag:
        #             f.write(str(i))

        #忽略 o = re.findall(r'value":{"isRelease":true,"movieRating":{"MovieId":(.*?),"RatingFinal":(.*?).*?}"movieTitle":"(.*?)".*?TotalBoxOffice":"(.*?)","TotalBoxOfficeUnit":"亿","TodayBoxOffice":"(.*?)","TodayBoxOfficeUnit":"万".*?',a)
        # 这是写入CSV
        dakai = open(r'k.txt')
        duqu = dakai.read()
        pipei = re.findall(r'(.*?),(.*?),(.*?),(.*?),(.*?);',duqu)
        biaoge = pd.DataFrame(pipei)
        biaoge.columns = ['电影ID', '电影名称','评分', '累计票房', '实时票房']
        biaoge.to_csv(r'text.csv', sep=',', encoding='utf-8')













    # film = ls_t[1].split('"')[3]
    # a = "".join(film)
    # # print id,a
    # if rating == "":
    #     print "id:" + id + " film:" + a + " rating:" + "0.0"
    # else:
    #     print "id:" + id + " film:" + a + " rating:" + rating
# def new_url():
#     page_id = get_id()
#     items = []
#     for i in page_id:
#
#         items.append('http://movie.mtime.com/' + str(i) + '/')
#     return items
# print new_url()

#     return i
# print new_url()
