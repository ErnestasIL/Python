from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/vartotojai')
def user_list():
    names = ['John', 'Debbie', 'Kevin', 'Angela']
    return render_template('vartotojai.html', names_for_template=names)
@app.route('/vartotojas/<vardas>')
def user_page(vardas):
    return f"Page by User: {vardas}"


app.run()