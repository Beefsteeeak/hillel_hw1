from flask import Flask
from flask import request
from faker import Faker
import csv
import requests

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


# task3
@app.route('/mean/')
def mean():
    j = 0
    height = 0
    weight = 0
    with open("hw.csv") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if row:
                j += 1
                height += float(row[1])
                weight += float(row[2])
    meanheight = (height / j) * 2.54
    meanweight = (weight / j) * 0.454
    superline = "Mean height in cm: " + "{}".format(meanheight) + "\n" + "Mean weight in kg: " + "{}".format(meanweight)
    superline = superline.replace('\n', '<br>')
    return superline


# task4
@app.route('/space/')
def number_of_astronauts():
    r = requests.get("http://api.open-notify.org/astros.json")
    a = r.json()["number"]
    number = "Number of astronauts: " + "{}".format(a)
    return number


if __name__ == '__main__':
    app.run()
