from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Главная'


@app.route('/all')
def all_():
    return 'all'


app.run()
