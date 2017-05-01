# Hello Really Tiny Flask App for Heroku

This repo is an abridged, updated, somewhat simpler version of this guide to getting a web app published on Heroku:

http://www.compjour.org/lessons/flask-single-page/hello-tiny-flask-app/

You can see a live-version here:

homepage: https://compjour-2017-danfoo.herokuapp.com/ 

`hello/` endpoint: https://compjour-2017-danfoo.herokuapp.com/hello/Stanford-loremipsum

`cage/` endpoint: https://compjour-2017-danfoo.herokuapp.com/cage/600/200



Assumes you have:

1. [Installed Python 3.x via Anaconda on your computer](http://2017.compciv.org/guide/topics/python/installing-python-via-anaconda.html?highlight=anaconda), which should include Flask, among other things.
2. Created a Heroku account
3. Have Git installed (which you probably do if you installed the [Github Desktop app at some point](https://desktop.github.com/))
4. Install the `gunicorn` web server library by running at your Terminal:

        $ pip install gunicorn

# Steps

## Getting started with Heroku

1. Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-command-line)
2. At your Terminal, run:

    $ heroku login
 
3. Go to this page on the Heroku website to make a new app: https://dashboard.heroku.com/new-app



### Create a new project folder/Git repository

The example below pretends that your app on Heroku is named:  `compjour-2017-danfoo`



1. Make a new directory in your own computer. It can be called anything, doesn't have to be what you named it on Heroku, e.g. `my-heroku-foo`
2. Change into that directory from the command line, then run `git init`
3. Then run: `heroku git:remote -a compjour-2017-danfoo`. This command points your local folder to the repo (remote folder) that Heroku uses to read code and deploy its app.



## Copying this app code

You'll need the following files that are in this repo (of which the README you're reading right now):

```
├── Procfile
├── app.py
├── .gitignore
├── requirements.txt
└── runfile.txt
```

Create those files manually. Copy the contents.

Then run these shell commands:

1. Run `git add .`
2. Run `git commit -m 'first'`
3. Run `git push heroku master`



The above steps are the bare-bones way to get a trivial "web app" onto the Heroku service. Check out the fuller guide here, which covers more about what a Flask app/web app is:

http://www.compjour.org/lessons/flask-single-page/hello-tiny-flask-app/


# Example student app

via Reade Levinson:

https://sleepy-woodland-12710.herokuapp.com/

The repo for the code: https://github.com/readelev/final-app

