from flask import render_template,flash,redirect,url_for
from . import news
from .forms import NameForm
from ..models import News
import jieba
import os,json
# 统计词频后绘制词云图
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

@news.route('/news',methods=['GET','POST'])
def newsfirst():
    keyword='中国'
    return redirect(url_for('news.news', name=keyword))

@news.route('/news/<name>',methods=['GET','POST'])
def news(name):
    #name =''
    form = NameForm()
    title=''
    contents=''
    news = []
    count=''
    wctext=''
    wc={}
    wccount=0
    if form.validate_on_submit():
        name=form.name.data
        form.name.data=''
    try:
        #rs=News.query.filter(News.title.like('%' + name + '%')).first()
        if name.isdigit():
            rs = News.query.filter().order_by(News.newscount.desc()).limit(name)
        else:
            rs = News.query.filter(News.title.like('%' + name + '%')).order_by(News.newsdate.desc()).all()
        if rs:
            for r in rs:
                news.append({'title': r.title, 'date': r.newsdate,'contents':r.contents,'url':r.newsurl,'newscount':r.newscount})
                #print(r.newsdate)
                wctext=wctext+r.contents
            count = len(news)
            wc=wordcloud(wctext)
            wccount=len(wc)
        else:
            news.append({'title':'none', 'date': '0000-00-00','contents':'no thus news','url':'--','newscount':'---'})
    except:
        print('error')
    return render_template('news.html',form=form,news=news,count=count,wc=wc,wccount=wccount)

def wordcloud(texts):
    jieba.load_userdict("dict.txt")  # 添加词典
    seg_list = jieba.cut(texts, cut_all=False)  # 分词

    tf = {}  # 统计词频
    for seg in seg_list:
        if seg in tf:  # 如果该键在集合tf的对象中，则该键所属对象值加1
            tf[seg] += 1
        else:  # 否则，生成新词的键值对，初始值为1
            tf[seg] = 1

    ci = list(tf.keys())  # 将字典的健值转为列表
    with open('stopword.txt', 'r') as ft:
        stopword = ft.read()

    for seg in ci:
        if len(tf)<=300 and (tf[seg] < 5 or len(seg) < 2 or seg in stopword or '一' in seg or '\r\n' in seg):
            tf.pop(seg)
        if len(tf)>300 and (tf[seg] < 20 or len(seg) < 2 or seg in stopword or '一' in seg or '\r\n' in seg):
            tf.pop(seg)
    print(tf)
    mask_img = np.array(Image.open("heart.png"))
    font = r'c:\Windows\Fonts\simfang.ttf'
    wc = WordCloud(background_color="white", mask=mask_img, collocations=False, font_path=font, max_font_size=200,
                   width=1600, height=500, margin=0).generate_from_frequencies(tf)
    # plt.imshow(wc)
    # plt.axis('off')
    # plt.show()

    # 基于彩色图像生成相应彩色
    image_colors = ImageColorGenerator(mask_img)
    # plt.imshow(wc.recolor(color_func=image_colors))
    # plt.axis('off')
    # plt.show()
    wcjpg= os.getcwd() + '\\app\\static\\wc.jpg'
    wc.to_file(wcjpg)
    return tf