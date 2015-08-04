#coding:utf-8

import requests
from bs4 import  BeautifulSoup
import re
from collections import Counter

URL=['http://www.qidian.com/Book/TopDetail.aspx?TopType=3&Category=-1&PageIndex=1'
    ,'http://www.qidian.com/Book/TopDetail.aspx?TopType=3&Category=-1&PageIndex=2'
    ,'http://www.qidian.com/Book/TopDetail.aspx?TopType=3&Category=-1&PageIndex=3'
    ,'http://www.qidian.com/Book/TopDetail.aspx?TopType=3&Category=-1&PageIndex=4'
    ,'http://www.qidian.com/Book/TopDetail.aspx?TopType=3&Category=-1&PageIndex=5'
    ,'http://www.qidian.com/Book/TopDetail.aspx?TopType=3&Category=-1&PageIndex=6'
    ,'http://www.qidian.com/Book/TopDetail.aspx?TopType=3&Category=-1&PageIndex=7'
    ,'http://www.qidian.com/Book/TopDetail.aspx?TopType=3&Category=-1&PageIndex=8'
    ,'http://www.qidian.com/Book/TopDetail.aspx?TopType=3&Category=-1&PageIndex=9'
    ,'http://www.qidian.com/Book/TopDetail.aspx?TopType=3&Category=-1&PageIndex=9'
     ]
#存放排名钱500书的url
Catalog=[]

#用于存放更新字数
listforWords=[]
#存放书目种类的排名
Catalog_Num=Counter()

#这个函数用于获得书单的url
def get_Book_Inf(URL):
    s=requests.session()
    html=s.get(URL).text
    UrlRe="http://.*?./Book/\d{7}.aspx"
    NameUrl=' class="type">.*?</a>'
    reg=re.compile(UrlRe)#找到书的url
    reg1=re.compile(NameUrl)
    global Catalog
    fuben=re.findall(reg,html)
    Catalog+=fuben
    listForKind=re.findall(reg1,html)
    print ('正在爬取书目种类.....')
    global  Catalog_Num
    for i in listForKind:
        Catalog_Num[i.split('>')[1].split('<')[0]]+=1


#这个函数根据每本书的url来获得作者每日跟新字数

def get_Book_Writespeed(bookUrl):
    s=requests.session()
    html=s.get(bookUrl).text
    reg=u"作者平均每天更新了.*?字"
    regtail=re.compile(reg)
    print ('正在下载作者的跟新速度.....')
    global listforWords
    string=re.findall(regtail,html)

    try:
        listforWords.append(string[0].split(u"了")[1].split(u"字")[0])
    except IndexError:
        pass

if __name__=='__main__':
    for i in URL:
        get_Book_Inf(i)
    for i in Catalog:
        get_Book_Writespeed(i)
    print Catalog_Num

    with open(u'speed.txt','w') as f:
        for i in listforWords:
            f.write(i+'\n')

    with open('record.txt','w') as f:
        for i in Catalog_Num:
            try:
                f.write('%s:%s\n'%(i,Catalog_Num[i]))
            except UnicodeDecodeError:
                pass
