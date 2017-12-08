#-*-coding:utf-8-*-
import re
import pandas as pd
dakai=open(r'spider.log')
duqu=dakai.read()
pipei=re.findall(r'http://www.movie.com/.*?《(.*?)》;(.*?);(.*?);.*?票房（万）(.*?) ;.*? ;',duqu)
print type(pipei)
print pipei
biaoge=pd.DataFrame(pipei)
print biaoge
biaoge.columns=['电影名称','上映日期','结束放映日期','票房收入']
biaoge.to_csv(r'ans0201.csv',sep=',',encoding='gb18030')