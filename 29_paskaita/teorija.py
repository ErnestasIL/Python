from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World from my first FLASK webApp!!\nHOMEPAGE"

@app.route("/news")
def news():
    return "Čia pagrindinis naujienų puslapis"

@app.route("/news/<int:item>")
def news_item(item):
    return f"Čia naujiena NR {item}"

@app.route("/<text>")
def any_route(text):
    return f"Jūs surinkote maršrutą {text} Jokio resurso čia nėra"

if __name__ == '__main__':
    app.run()