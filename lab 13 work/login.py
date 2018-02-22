from flask import Flask, render_template
from flask import request, flash
import string
from flask_wtf import Form
from wtforms import PasswordField
from wtforms import StringField
from wtforms import SubmitField
from wtforms import validators


class LoginForm(Form):
    username = StringField('username', validators = [validators.DataRequired()])
    password = PasswordField('password', validators =[validators.DataRequired(), validators.length(min=8)])
    password2 = PasswordField('password2', validators=[validators.DataRequired(),
        validators.EqualTo('password', message='Passwords must match')])
    submit = SubmitField('submit', [validators.DataRequired()])

app = Flask(__name__)

USERNAME, PASSWORD = 'hussein', '123454dfgd'
app.secret_key = '123456789987654321'

def sanitise_string(userinput):
	# clean up the inputs
    return ''.join(e for e in userinput if e.isalnum())
    # https://docs.python.org/3.5/library/stdtypes.html

@app.route("/", methods = ['GET','POST'])

def show_user():
    username, password ='',''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        username = sanitise_string(username)
        password = sanitise_string(password)
        
        if username == USERNAME and password == PASSWORD:
           flash('yup your in !') 
    list = [username, password]
    return render_template('mock_login.html', list=list)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)
