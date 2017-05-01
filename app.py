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

@app.route("/cage/<width>/<height>")
def placecage(width=400, height=400):
    templatetext = """
    <p>
        This is a hotlinked {w}x{h} picture of Nicolas Cage
        from
        <a href="http//placecage.com">placecage.com</a>:
    </p>
    <img src="http://placecage.com/{w}/{h}" alt="placecage">
    """

    return templatetext.format(w=width, h=height)



if __name__ == "__main__":
    app.run()
