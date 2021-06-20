from flask import Flask 
from flask import render_template
from flask import request
from flask import redirect
import csv
app = Flask(__name__)
print(__name__)

@app.route('/')
def hello_world():
    return render_template('./index.html')

@app.route('/project.html')
def project():
    return  render_template('./project.html')


@app.route('/index.html')
def home():
    return render_template('./index.html')  
    
@app.route('/components.html')
def components():
    return render_template('./components.html')

@app.route('/thankyou.html')
def thankyou():
    return render_template('./thankyou.html')


def write(data):
    with open('database.txt', mode='a')as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email}, {subject}, {message}')

def write_to_csv(data):
    with open('database.csv', 'w', newline='') as csvfile:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:

            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save your response to the database- please mail to databaseupdates0102gmail.com'
    else:
        return "something went wrong"