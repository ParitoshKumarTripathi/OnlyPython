from flask import Flask
import feedparser
from newsplease import NewsPlease
app = Flask(__name__)

@app.route('/')
def news():
    feed = feedparser.parse('https://rss.nytimes.com/services/xml/rss/nyt/World.xml')
    titles = []

    for entry in feed.entries:
        article = NewsPlease.from_url(entry.link)
        if article is not None:
            titles.append(article.title)

    all_titles = '\n'.join(titles)
    return all_titles
