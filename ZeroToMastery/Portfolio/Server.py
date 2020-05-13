import os
import csv
from flask import Flask, render_template, send_from_directory, request, redirect

app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/')
def home():
    return render_template('index.html')


# C:\\Users\\JR0544\\PycharmProjects\\ZeroToMastery\\Web Server\\
# @app.route('/<user>/<int:post_id>')
# def hello_world(user='Jaggu', post_id=None):
#     return render_template('index.html', name=user, post_id=post_id)

"""
@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/project.html')
def project():
    return render_template('project.html')


@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/services.html')
def services():
    return render_template('services.html')


@app.route('/contact.html')
def contact():
    return render_template('contact.html')


@app.route('/components.html')
def components():
    return render_template('components.html')


@app.route('/sample-page.html')
def sample():
    return render_template('sample-page.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')

"""


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_dbfile(data)
            write_to_csv(data)
            return redirect('/Thankyou.html')
        except:
            return 'Did not save to db'
    else:
        return 'something went wrong. Try again!'
    # return render_template('login.html', error=error)


def write_to_dbfile(data):
    with open('db.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('dbcsv.csv', mode='a', newline='') as csvfile:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        #
        # fieldnames = ['email', 'subject', 'message']
        # writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # writer.writeheader()
        csv_writer.writerow([email, subject, message])
