from flask import Flask, redirect, Markup, render_template, request
import waitress as waitress
from waitress import serve
import os

app = Flask(__name__)

@app.route('/')
def home():
    return redirect('/home')

@app.route('/<page>')
def article(page):
    if any(page in a for a in ARTICLES):
        pagedetails = next(i for i in ARTICLES if i[0] == page)
        prevdetails = ARTICLES[(ARTICLES.index(pagedetails) -1) % articlecount]
        nextdetails = ARTICLES[(ARTICLES.index(pagedetails) +1) % articlecount]
        return render_template(pagedetails[1],
        article = pagedetails[1], title=pagedetails[2], color=pagedetails[3], date=pagedetails[4],
        nexttitle=nextdetails[2], nexturl=nextdetails[0],nextcolor=nextdetails[3],
        prevtitle=prevdetails[2], prevurl=prevdetails[0],prevcolor=prevdetails[3])
    else:
        if not any(page in a for a in OVERVIEWS):
            page = '404'
        pagedetails = next(i for i in OVERVIEWS if i[0] == page)
        html = "<div class='flex flex-row flex-wrap -mx-4'>"
        for i in pagedetails[4]:
            carddetails = next(j for j in ARTICLES if j[0] == i)
            html += "<div class='flex-none shadow-sm text-left font-display py-2 px-4 text-"+carddetails[3]+"-200 bg-"+carddetails[3]+"-800 hover:bg-"+carddetails[3]+"-600 focus:bg-"+carddetails[3]+"-100 h-48 w-48 mx-2 my-2 sm:mx-4 sm:my-4'><a href=/"+carddetails[0]+"><span class='block text-right font-bold'>"+carddetails[4]+"</span><h3 class='font-display overflow-hidden h-full text-2xl'>"+carddetails[2]+"</h3></a></div>"
        html += "</div>"
        html = Markup(html)
        return render_template(pagedetails[1],
        article = pagedetails[1], title=pagedetails[2], color=pagedetails[3],cards=html)

#every article is listed here as [URL resource name, HTML file path, title, color,date]
ARTICLES = [
    ['spacesnake','/articles/spacesnake.html','Space Snake: Unleashed','blue','Dec 11, 2020'],
    ['website','/articles/website.html','Making this website using Flask and Heroku','blue','Dec 8, 2020'],
    ['about','/articles/about.html','About me','gray','Dec 1, 2020']
    ]

articlecount = len(ARTICLES)

#every overview is listed here as [URL resource name, HTML file path, title, color, [articles]]
OVERVIEWS = [
    ['404','/overviews/404.html','Page not found!','red',[]],
    ['reads','/overviews/reads.html','Overview of reads','green',[]],
    ['art','/overviews/art.html','Art overview','pink',[]],
    ['webdev','/overviews/webdev.html','Web dev overview','blue',['spacesnake','website']],
    ['home','/overviews/home.html','All articles','red',['spacesnake','website','about']]
    ]

#serve the file. This works on heroku after you CLI 'heroku config:set ON_HEROKU=1'
if 'ON_HEROKU' in os.environ:
    if __name__ == "__main__":
        app.debug = False
        port = int(os.environ.get('PORT', 33507))
        waitress.serve(app, port=port)
else:
    app.run(debug=True)
