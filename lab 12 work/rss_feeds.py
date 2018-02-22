from flask import Flask, render_template
import feedparser

app = Flask(__name__)

MOTOR_SPORTS = "http://feeds.reuters.com/reuters/UKMotorSportsNews"

@app.route("/")
def headlines():
    feed = feedparser.parse(MOTOR_SPORTS)
    articles = feed['entries']
    return render_template('bbc_headline',articles=articles)

@app.route("/<word>")
def headlines_word(word):
    word = word.lower()
    feed = feedparser.parse(MOTOR_SPORTS)
    articles = feed['entries']
    return render_template('bbc_headline',articles=articles,word=word)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)
