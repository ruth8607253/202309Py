from flask import Blueprint,render_template

bp=Blueprint('bbb',__name__,url_prefix='/bbb')

@bp.route("/")
def index():
    return render_template("bbb/index.html")