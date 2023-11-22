from flask import Blueprint,render_template

bp=Blueprint('aaa',__name__,url_prefix='/aaa')

@bp.route("/")
def index():
    return render_template("auth/index.html")

@bp.route("/login")
def login():
    return render_template("auth/login.html")