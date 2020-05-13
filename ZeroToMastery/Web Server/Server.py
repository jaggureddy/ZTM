import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/')
def home():
    return render_template('Home.html')


# C:\\Users\\JR0544\\PycharmProjects\\ZeroToMastery\\Web Server\\
@app.route('/<user>/<int:post_id>')
def hello_world(user='Jaggu', post_id=None):
    return render_template('index.html', name=user, post_id=post_id)


@app.route('/blog')
def blog():
    return 'This is my blog'


@app.route('/blog/2020/Virus')
def corona():
    return 'Corona Virus'


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')
