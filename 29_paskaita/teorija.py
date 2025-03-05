
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/vardusarasas")
def names_list():
    names = ["Adomas", "Antanas", "Valdas", "Jonas"]
    return render_template("vardai.html", names_for_template=names)




























# from flask import Flask
#
# app = Flask(__name__)
#
# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route("/")
# def home():
#     return """
#     <h1>Homepage</h1>
#     <p>Hello World!!!</p>
#     <p><a href='/verslas'>pereiti į verslo skyrių</a></p>
#     """
# @app.route('/verslas')
# def verslas():
#     return '<h1>Verslo Skyrius</h1><p>Verslo naujienos</p>'
#

# @app.route('/')
# def home():
#     return "Hello World from my first FLASK webApp!!\nHOMEPAGE"
#
# @app.route("/news")
# def news():
#     return "Čia pagrindinis naujienų puslapis"
#
# @app.route("/news/<int:item>")
# def news_item(item):
#     return f"Čia naujiena NR {item}"
#
# @app.route("/<text>")
# def any_route(text):
#     return f"Jūs surinkote maršrutą {text} Jokio resurso čia nėra"

if __name__ == '__main__':
    app.run()