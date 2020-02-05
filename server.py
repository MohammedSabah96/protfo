from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<string:pagename>')
def html_page(pagename):
    return render_template(pagename)


def write_to_csv(data):
    with open("database.csv", 'a', newline='') as database:
        email = data['email']
        subject = data['subject']
        messege = data['messege']
        csv_file = csv.writer(database,  delimiter=',',
                              quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_file.writerow([email, subject, messege])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return "data did not save"
    else:
        return "something went wrong"
