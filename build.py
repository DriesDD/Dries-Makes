from flask import Flask, redirect, render_template, request
import json
import traceback
import os
from waitress import serve

app = Flask(__name__)

@app.route('/')
def home():
    return redirect('/home')

@app.route('/<page>')
def article(page):
    pagedetails = next(i for i in PAGES if i[0] == page)
    nextdetails = PAGES[(PAGES.index(pagedetails) -1) % pagecount]
    prevdetails = PAGES[(PAGES.index(pagedetails) +1) % pagecount]
    return render_template(pagedetails[1],
    article = pagedetails[1], title=pagedetails[2], color=pagedetails[3], date=pagedetails[4],
    nexttitle=nextdetails[2], nexturl=nextdetails[0],nextcolor=nextdetails[3],
    prevtitle=prevdetails[2], prevurl=prevdetails[0],prevcolor=prevdetails[3])

#every page is listed here as [URL resource name, HTML file path, title]
PAGES = [
    ['website','/articles/website.html','Making this website using flask and Heroku','blue','Dec 8, 2020'],
    ['reads','/articles/reads.html','Overview of reads','green','Dec 2, 2020'],
    ['art','/articles/art.html','Art overview','pink','Dec 2, 2020'],
    ['webdev','/articles/webdev.html','Web dev overview','blue','Dec 2, 2020'],
    ['home','/articles/home.html','Welcome','green','Dec 2, 2020'],
    ['about','/articles/about.html','Dries De Decker','gray','Dec 1, 2020'],
    ]

pagecount = len(PAGES)

if __name__ == "__main__":
    app.debug = False
    port = int(os.environ.get('PORT', 33507))
    waitress.serve(app, port=port)

    