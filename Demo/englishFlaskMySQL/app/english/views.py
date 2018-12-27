from flask import render_template,flash
from . import english
from .forms import NameForm
from ..models import English

@english.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

@english.route('/eng',methods=['GET','POST'])
def english():
    name=None
    form=NameForm()
    wordc=''
    if form.validate_on_submit():
        name=form.name.data
        form.name.data=''
        word=English.query.filter_by(english=name).first()
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
    return render_template('english.html',form=form,name=name,wordc=wordc,wordcount=wordcount)

