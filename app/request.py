import urllib.request,json
from .models import Source, Articles


api_key = None
base_url = None
article_url = None

def configure_request(app):
    global api_key, base_url,article_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_SOURCE_URL']
    article_url = app.config["ARTICLES_URL"]