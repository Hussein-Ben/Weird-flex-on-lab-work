from flask import Flask, render_template
from flask import request
import feedparser

app = Flask(__name__)

RSS_FEEDS = { 'Motor Sports': 'http://feeds.reuters.com/reuters/UKMotorSportsNews',
              'Science' : 'http://feeds.reuters.com/reuters/UKScienceNews',
              'ars technica':'http://feeds.arstechnica.com/arstechnica/index'}

@app.route("/")
def headlines():
    publication =''
    if request.args.get('publication'):
        publication = request.args.get('publication')
    if not publication or publication.lower() not in RSS_FEEDS:
        publication = "Motor Sports"
    else:
        publication = publication.lower()
    feed = feedparser.parse(RSS_FEEDS[publication])
    articles = feed['entries']
    return render_template('get_headlines.html',articles=articles)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)
