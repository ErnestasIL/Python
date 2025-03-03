from flask import Flask

app = (Flask(__name__))

@app.route('/')
def home():
    return 'Welcome to Flask application!'

@app.route('/about')
def about():
    return 'This is a page about us :)'

@app.route('/user/<text>')
def user(text):
    return f'Hello {text}, Happy to see you!'

@app.route('/number/<int:item>')
def number(item):
    return f'You typed Nr: {item}'

@app.route('/trip/<start>/<end>')
def trip(start, end):
    return f'Trip from {start} to {end}'

if __name__ == '__main__':
    app.run()
