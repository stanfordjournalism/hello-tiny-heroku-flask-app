# http://flask.pocoo.org/
# https://dashboard.heroku.com/apps/dandan1111/deploy/heroku-git
# https://github.com/datademofun/heroku-basic-flask


from flask import Flask
app = Flask(__name__)

@app.route("/")
def homepage():
    return "Hello World to my <strong>homepage</strong>!"

@app.route("/hello/<name>")
def hello(name):
    return "Hello, <strong>{}!</strong>".format(name)


if __name__ == "__main__":
    app.run()
