# -*- coding:UTF-8 -*-
import urllib
import urllib2
import re
from collections import Counter
import random
import string


def pic_download(url, file_path):
    # 打开网页
    # url = r'http://tieba.baidu.com/p/2166231880'
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    content = response.read()
    # print content

    # 正则表达式
    rule_str = r'<img class="BDE_Image" src="(.*?)'
    rule = re.compile(rule_str)
    img_list = rule.findall(content)

    print u"正在下载图片..."
    x = 0
    len_temp = []
    for img in img_list:
        len_temp.append(len(img))  # 计算每个图片链接的长度
    most_length = tuple(Counter(len_temp).most_common(1))[0][0]  # 默认需要下载的图片是链接中最多的，寻找最多的图片链接的长度

    for img in img_list:
        if len(img) != most_length:
            continue  # 不是目标图片，跳出继续
        else:
            pic = urllib2.urlopen(img).read()
            f = open(r"%s\%s%s.jpg" % (file_path, x, random.choice(string.ascii_letters)), "wb+")
            f.write(pic)
            f.close()
            x += 1

    print u"%s 张图片已被下载至指定位置" % x

# 主函数
if __name__ == "__main__":
    url = raw_input(r"Please input the BAIDU tieba link:")  # 请输入百度贴吧链接的帖子
    file_path = raw_input(r"Please input the file path(default: C:\Users\Wind\Pictures): ")  # 请输入想要保存图片的位置
    pic_download(url=r'https://tieba.baidu.com/p/5433959304?fid=608&pn=', file_path=r"D:\image\demo3")