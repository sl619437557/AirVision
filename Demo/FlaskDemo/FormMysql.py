from flask import Flask,render_template,flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SECRET_KEY']='hard to guess string'
bootstrap=Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:2018@127.0.0.1:3306/flask2018'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
db=SQLAlchemy(app)

class English(db.Model):
    __tablename__='map_enword'
    id=db.Column(db.Integer,primary_key=True)
    english=db.Column(db.String(64))
    pt=db.Column(db.String(64))
    chinese=db.Column(db.String(64))
    flag=db.Column(db.String(64))

class NameForm(FlaskForm):
    name=StringField('你的名字？',validators=[DataRequired()])
    submit=SubmitField('提交')


@app.route('/',methods=['GET','POST'])
def index():
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
    for i in range(0,25):
        str=chr(97+i)
        wcount=English.query.filter(English.english.like(''+str+'%')).count()
        if wcount:
            wordcount.append(wcount)
        else:
            flash('没有这样的单词！')
    print(wordcount)
    return render_template('index.html',form=form,name=name,wordc=wordc,wordcount=wordcount)

if __name__=='__main__':
    print(English.query.count())
    app.run()
