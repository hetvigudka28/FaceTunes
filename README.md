# FaceTunes

This app recognizes ones emotion and mood based on facial expression. Based on the mood detected, a playlist is seleted and the songs are played on a music player.
Django framework is used in this web application. 

## Built with 

- Python
- Django
- HTML
- CSS
- Javascript
- SQL


## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/hetvigudka28/FaceTunes.git
$ cd FaceTunes
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd FaceEmotion_Recognition
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.

## Screenshots

![happyPic](media/screenshots/happyClick.jpg)

![Happy](media/screenshots/happy.jpg)

![neutralPic](media/screenshots/neutralClick.jpg)

![neutral](media/screenshots/neutral.jpg)



