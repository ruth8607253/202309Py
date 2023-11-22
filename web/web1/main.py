from flask import Flask,url_for,render_template
import random
import pandas
from bbb import bbb

app = Flask(__name__)
app.register_blueprint(bbb.bp)

@app.route("/")
def main():
    return render_template('main.html')