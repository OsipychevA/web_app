from flask import Flask
from parser import get_top


app = Flask(__name__)


@app.route('/')
def home_page():
    return '<h1>Привет, Стас!</h1>'


@app.route('/api/top_250')
def top_250():
    films = get_top()
    return f'<h1>ТОП 250: {films}</h1>'


@app.route('/api/<get_film>')
def get_film(get_film: str) -> str:
    return f'<h1>Фильм который вы ищите: {get_film}</h1>'


if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=5000,
            debug=True)