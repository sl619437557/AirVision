from flask import render_template,flash,redirect,url_for
from . import english
from .forms import NameForm
from ..models import English
from nltk.corpus import wordnet as wn
import os,json

# ---Json格式的网络文件

d = {"name": ""}
e = {"source": -1, "target": -1,"type":-1}
jsonOut = 'wordnet.json'
#-----Json

@english.route('/index',methods=['GET','POST'])
def index():
    return render_template('index.html')

@english.route('/',methods=['GET','POST'])
def wordnet():
    name='hello'
    return redirect(url_for('english.wordUrl', name=name))

@english.route('/<name>',methods=['GET','POST'])
def wordUrl(name):
    #name=name
    wordc = ''
    wnSyn = []
    wnSynName = []
    wnHypernyms = []
    wnHyponyms = []
    wnLemmas = []
    wnAnto = []
    wnDef = ''
    hyper = []
    hhyper = []
    hypo = []
    hhypo = []
    nodejson = []
    edgejson = []
    form=NameForm()
    if form.validate_on_submit():
        name=form.name.data
        print(form.name.data)
        return redirect(url_for('english.wordUrl', name=name))
    else:
        word = English.query.filter_by(english=name).first()
        if (wn.synsets(name) != []):
            wnSyn = wn.synsets(name)
            wnSynName = wn.synsets(name)
            i = 0
            for h in wnSynName:
                wh = h.__str__()[h.__str__().find('\'') + 1: h.__str__().find('.')]
                wnSynName[i] = wh
                i = i + 1
            # 写入Json文件
            # 节点与边
            gg = []
            j = 1
            netjson = {"links": "", "nodes": ""}
            nodejson = []
            edgejson = []
            for g in wnSynName:
                # 节点
                gg.append(g)
                test = d.copy()  # json格式
                test["name"] = g  # json格式
                nodejson.append(test)  # json格式
                # 边
                teste = e.copy()
                teste["source"] = wnSynName.index(wnSynName[0])
                teste["target"] = wnSynName.index(g)
                teste["type"] = 'synsets'
                edgejson.append(teste)

                j = j + 1
            netjson["nodes"] = nodejson
            netjson["links"] = edgejson
            jsonfile = os.getcwd() + '\\app\\static\\' + jsonOut
            print(jsonfile)
            f = open(jsonfile, 'w')
            f.write(json.dumps(netjson))
            f.close()

            wnHypernyms = wnSyn[0].hypernyms()
            i = 0
            for h in wnHypernyms:
                wh = h.__str__()[h.__str__().find('\'') + 1: h.__str__().find('.')]
                wnHypernyms[i] = wh
                i = i + 1
            wnHyponyms = wnSyn[0].hyponyms()
            i = 0
            for h in wnHyponyms:
                wh = h.__str__()[h.__str__().find('\'') + 1: h.__str__().find('.')]
                wnHyponyms[i] = wh
                i = i + 1
            wnLemmas = wnSyn[0].lemmas()

            wnDef = wn.synset(name + '.n.01').definition()
            wnSyn = wn.synsets(name)
            wnAnto = wnSyn[0].lemmas()[0].antonyms()
            i = 0
            for h in wnAnto:
                wh = h.__str__()[h.__str__().find('\'') + 1: h.__str__().find('.')]
                wnAnto[i] = wh
                i = i + 1

            i = 0
            for h in wnLemmas:
                wh = h.__str__()[h.__str__().rfind('.') + 1: h.__str__().rfind('\'')]
                wnLemmas[i] = wh
                i = i + 1
            theword=wnSyn[0]
            hypo = lambda s: s.hyponyms()
            hyper = lambda s: s.hypernyms()
            hhypo = list(theword.closure(hypo))
            hhyper = list(theword.closure(hyper))
            i = 0
            for h in hhypo:
                wh = h.__str__()[h.__str__().find('\'') + 1: h.__str__().find('.')]
                hhypo[i] = wh
                i = i + 1
            hhyper = list(theword.closure(hyper))
            i = 0
            for h in hhyper:
                wh = h.__str__()[h.__str__().find('\'') + 1: h.__str__().find('.')]
                hhyper[i] = wh
                i = i + 1
        else:
            wnSyn = "None"
            wnSynName = "None"
            wnDef = "None"
            wnHypernyms = "None"
            wnHyponyms = "None"
            wnLemmas = "None"
            wnAnto = "None"
            hhypo = "None"
            hhyper = "None"

            if(word):
                wordc=word.chinese
            else:
                wordc='None!'
    return render_template('wordnet.html',form=form,name=name,wordc=wordc,wnSyn=wnSynName, wnDef=wnDef,wnHypernyms=wnHypernyms,wnHyponyms=wnHyponyms,wnLemmas=wnLemmas,wnAnto=wnAnto,hypo=hhypo,hyper=hhyper,nodejson=nodejson,edgejson=edgejson)

@english.route('/hist',methods=['GET','POST'])
def english():
    name=None
    form=NameForm()
    wordc=''
    wnSyn=[]
    wnDef=''
    if form.validate_on_submit():
        name=form.name.data
        form.name.data=''
        word=English.query.filter_by(english=name).first()
        if (wn.synsets(name)!=[]):
            wnSyn=wn.synsets(name)
            wnDef=wn.synset(name+'.n.01').definition()
        else:
            wnSyn ="Error"
            wnDef ="Error"

        if(word):
            wordc=word.chinese
        else:
            wordc='None!'
    str=chr(97)
    wordcount=[]
    for i in range(0,26):
        str=chr(97+i)
        wcount=English.query.filter(English.english.like(''+str+'%')).count()
        if wcount:
            wordcount.append(wcount)
        else:
            flash('没有这样的单词！')
    print(wordcount)
    return render_template('english.html',form=form,name=name,wordc=wordc,wnSyn=wnSyn, wnDef=wnDef,wordcount=wordcount)

def graphJson():
    pass