import pymysql
import requests as re
from bs4 import BeautifulSoup

def spiderCUC():
    try:
        for i in range(1, 405):  # 405总页数
            url = "http://by.cuc.edu.cn/zcyw/" + str(i)
            r = re.get(url)
            # print(r.text)
            soup = BeautifulSoup(r.text, 'html.parser')
            title = soup.find_all('h3', attrs={'class', 'tit'})
            print(i)
            for t in title:
                newsurl = t.find_all('a')
                urllen = str(newsurl[0]).find('target')
                news = str(newsurl[0])[9:urllen - 2]
                getUrl(news)
                #print(str(newsurl[0])[9:urllen - 2])
                #print(t.get_text())
    except:
        print("error")


def getUrl(url):
    # url="http://www.cuc.edu.cn/zcyw/11584.html"
    try:
        r = re.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        title = soup.find_all('h1')
        newsfrom = soup.find_all('sapn')
        newsdate = soup.find_all('sapn')
        viewcount = soup.find_all('span', attrs={'id': 'hits'})
        newscontent = soup.find_all('article', attrs={'class', 'con-area'})

        ntitle = title[0].get_text()
        fromlen = newsfrom[0].get_text().find('20')
        fromtest = newsfrom[0].get_text().find('-')
        nfrom = newsfrom[0].get_text()[27:fromlen].strip()
        ndate = newsdate[0].get_text()[fromlen:fromlen + 10]
        ncount = viewcount[0].get_text()
        ncontent = newscontent[0].get_text()
        saverec(url, ntitle, nfrom, ndate, ncount, ncontent)
    except:
        print("error")


def saverec(url, ntitle, nfrom, ndate, ncount, ncontent):
    # pymysql.connect(数据库url,用户名,密码,数据库名 )
    db = pymysql.connect("localhost", "root", "2017", "engword", charset='utf8')
    cursor = db.cursor()
    try:
        cursor.execute(
            "INSERT INTO cucnews(newsurl,title,newsfrom,newsdate,contents,newscount) VALUES(%s,%s,%s,%s,%s,%s)",
            (url, ntitle, nfrom, ndate, ncontent, ncount))
        db.commit()
    except:
        print(db.error())
        db.rollback()
    db.close()

spiderCUC()