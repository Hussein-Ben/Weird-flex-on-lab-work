from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<center><h1>  Hello, World!  </h1></center>'

@app.route('/time')
def show_time():
    t =  str(datetime.datetime.now())
    return '<center><h1>  %s  </h1></center>' % t
    

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)
