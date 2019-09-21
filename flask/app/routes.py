#导入模板模块
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'duke'}
    #将需要展示的数据传递给模板进行显示
    return render_template('index.html',title='我的',user=user)