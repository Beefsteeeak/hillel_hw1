from flask import Flask
from flask import request
from faker import Faker

fake = Faker()

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


# task1
@app.route('/requirements/')
def show_requirements():
    superline = ""
    with open("requirements.txt", "r") as r:
        for line in r:
            superline += line
    superline = superline.replace('\n', '<br>')
    return superline
# another option
#        g = r.read()
#        g = g.replace('\n', '<br>')
#    return g


# task2
@app.route('/generate-users/')
def generate_users():
    n = min(int((request.args.get("count", 100))), 100)
    superline = ""
    for _ in range(n):
        superline += fake.name() + ' ' + fake.name().lower().replace(' ', '') + '@mail.com' + '\n'
    superline = superline.replace('\n', '<br>')
    return superline


if __name__ == '__main__':
    app.run()
