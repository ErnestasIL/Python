from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    search_text = request.args.get('paieskoslaukelis')
    print(search_text)
    return render_template("forma_get.html")

@app.route("/login", methods=['post', 'get'])
def login_user():
    if request.method == "GET":
        return render_template("forma_post.html")
    elif request.method == "POST":
        form_text = request.form.get("loginlaukelis")
        return render_template("login_result.html", user_login=form_text)




















































































































































app.run()