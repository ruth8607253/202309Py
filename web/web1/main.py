from flask import Flask,url_for,render_template
import random
import pandas
from A import aaa

app = Flask(__name__)
app.register_blueprint(aaa.bp)

@app.route("/")
def hello():
    return render_template('hello.html')

@app.route("/post/<int:post_id>")
def aaa(post_id):
    return f"<h1>{post_id*5}</h1>"

@app.route("/main")
def main():
    dataFrame=get_dataFrame()
    return render_template('main.html',dataFrame=dataFrame)

def get_dataFrame():
    data=[['小明',100,99,98],
          ['小華',97,96,95],
          ['小美',94,93,92]]

    return pandas.DataFrame(data,columns=("姓名",'國文','英文','數學'))