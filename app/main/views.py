from flask import render_template, request, redirect, url_for
from  ..request import get_sources,get_articles
from ..models import Source, Articles
from . import main

@main.route('/')
def index():
    business_news = get_sources('business')
    general = get_sources('general')
    entertainment = get_sources('entertainment')
    sports = get_sources('sports')

    return render_template('index.html', business_news=business_news, 
    entertainment=entertainment,general=general,sports=sports)

@main.route('/sources/<id>')
def articles(id):
    '''
    route page for articles and the content availabe
    '''
    article = get_articles(id)

    return render_template('articles.html', article= article)