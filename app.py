from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/requirements/')
def show_requirements():
    with open("requirements.txt", "r") as r:
        g = r.read()
        g = g.replace('\n', '<br>')
    return g

if __name__ == '__main__':
    app.run()
