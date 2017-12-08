
import re
import urllib
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html


def getImg(html, x):
    reg = r'src="(.+?\.jpg)"'
    imgre = re.compile(reg)
    imList = re.findall(reg, html)

    print(imList)
    for i in imList:
        print(i)
        print x
        urllib.urlretrieve(i, "D:/image/%s.jpg"%x)
        x += 1
    return x


x = 1
url = "https://tieba.baidu.com/p/5428389984?pn="
for k in range(1, 28):
    ul = url + str(k)
    print ul
    html = getHtml(ul)
    # print html
    x = getImg(html, x)