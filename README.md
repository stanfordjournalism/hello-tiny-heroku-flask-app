# Hello Really Tiny Flask App for Heroku

An updated, kind-of simpler guide to getting a web app online:

http://www.compjour.org/lessons/flask-single-page/hello-tiny-flask-app/

Assumes you have:

1. [Installed Python 3.x via Anaconda on your computer](http://2017.compciv.org/guide/topics/python/installing-python-via-anaconda.html?highlight=anaconda), which should include Flask, among other things.
2. Created a Heroku account
3. Have Git installed (which you probably do if you installed the [Github Desktop app at some point](https://desktop.github.com/))


# Steps

## Getting started with Heroku

1. Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-command-line)
2. Go to this page on the Heroku website to make a new app: https://dashboard.heroku.com/new-app
3. Pretend your app is named `compjour-2017-danfoo`


### Create a new project folder/Git repository

1. Make a new directory, e.g. `my-first-heroku-flask`
2. Change into that directory from the command line, then run `git init`
3. Then run: `heroku git:remote -a compjour-2017-danfoo`



## Copying this app code

You'll need the following files that are in this repo (of which the README you're reading right now):

```
├── Procfile
├── app.py
├── requirements.txt
└── runfile.txt
```

Create those files manually. Copy the contents.

Then

1. Run `git add .`
2. Run `git commit -m 'first'`
3. Run `git push heroku master`






