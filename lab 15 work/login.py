from flask import Flask, request
from flask import render_template
from flask import redirect, url_for
from flask import session, flash, abort
from vs_url_for import vs_url_for
from forms_8 import addTwitForm, editTwitForm, loginForm
from dbhelper_8 import DBHelper

app = Flask(__name__)
db = DBHelper()
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route('/')
def index():
    twits = db.get_all_twits()
    return render_template("mytwits_mysql_6.html", twits=twits)

@app.route('/add_twit', methods = ['GET', 'POST'])
def add_twit():
    if not session.get('username'):
        abort(401)
    form = addTwitForm()
    if form.validate_on_submit():
        twit = form.twit.data
        db.add_twit(twit,session['user_id'])
        return redirect(vs_url_for('index'))
    return render_template('add_twit_mysql_6.html',form=form)

@app.route('/edit_twit', methods = ['GET', 'POST'])
def edit_twit():
    if not session.get('username'):
        abort(401)
    form = editTwitForm()
    if request.args.get('id'):
        twit_id = request.args.get('id')
        twit = db.get_twit(twit_id)
        form.twit.data = twit[0]
        form.twit_id.data = twit_id
        return render_template('edit_twit_mysql_6.html',form=form,twit=twit)
    if form.validate_on_submit():
        twit = form.twit.data
        twit_id = form.twit_id.data
        db.update_twit(twit,twit_id)
        return redirect(vs_url_for('index'))
    return render_template('edit_twit_mysql_6.html',form=form)

@app.route('/delete_twit', methods = ['GET', 'POST'])
def delete_twit():
    if not session.get('username'):
        abort(401)
    if request.args.get('id'):
        twit_id = request.args.get('id')
        twit = db.delete_twit(twit_id)
    return redirect(vs_url_for('index'))
   
@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = loginForm()
    if form.validate_on_submit():
        password = form.password.data
        username = form.username.data
        user_id = db.check_password(username,password)
        if user_id:
            session['username'] = username
            session['user_id'] = user_id[0]
            flash('login successful!')
            return redirect(vs_url_for('index'))
        else:
            flash('login unsuccessful!')
    return render_template('login.html',form=form)

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(vs_url_for('index'))

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)
