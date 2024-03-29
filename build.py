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
            html += "<div class='flex-none sm:shadow-sm text-left font-display py-2 px-4 text-"+carddetails[3]+"-200 bg-"+carddetails[3]+"-800 hover:bg-"+carddetails[3]+"-600 focus:bg-"+carddetails[3]+"-100 h-48 w-48 m-2 sm:m-4'><a href=/"+carddetails[0]+"><span class='block text-right font-bold'>"+carddetails[4]+"</span><h2 class='font-display overflow-hidden h-full text-2xl'>"+carddetails[2]+"</h2></a></div>"
        html += "</div>"
        html = Markup(html)
        return render_template(pagedetails[1],
        article = pagedetails[1], title=pagedetails[2], color=pagedetails[3],cards=html)

"""
@app.route('/votestar/<path:dynamicPath>')
def show_subpath(dynamicPath):
   if dynamicPath == 'poll':
      poll = .get(dynamicPath) #get your orders from db or files
      return render_template('poll.html', poll=poll)
   elif dynamicPath == 'otherStuff':
      return "page not found"
"""

#every article is listed here as [URL resource name, HTML file path, title, color,date]
ARTICLES = [
    ['life2','/articles/life2.html','Optimized Life Simulation','blue','Jun 26, 2022'],
    ['words','/articles/words.html','Words on things are overpowered','pink','Jul 27, 2021'],
    ['unweaving','/articles/unweaving.html','Aztec Metaphysics Boardgame Box Art','green','Feb 19, 2021'],
    ['soap','/articles/soap.html','Honeycomb Soap','green','Jan 22, 2021'],
    ['jupiter','/articles/jupiter.html','Jupiter whirls','pink','Jan 3, 2021'],
    ['economy','/articles/economy.html','What is the economy?','pink','Dec 23, 2020'],
    ['life','/articles/life.html','Python and the Meaning of Life','blue','Dec 22, 2020'],
    ['spacesnake','/articles/spacesnake.html','Space Snake: Unleashed','blue','Dec 11, 2020'],
    ['website','/articles/website.html','Making this website using Flask and Heroku','blue','Dec 8, 2020'],
    ['who','/articles/about.html','Who?','red','Dec 1, 2020']
    ]

articlecount = len(ARTICLES)

#every overview is listed here as [URL resource name, HTML file path, title, color, [articles]]
OVERVIEWS = [
    ['404','/overviews/404.html','Page not found!','red',[]],
    ['DIY','/overviews/DIY.html','DIY overview','green',['unweaving','soap']],
    ['art','/overviews/art.html','Art overview','pink',['words','unweaving','jupiter','economy']],
    ['dev','/overviews/dev.html','Development overview','blue',['life2','life','spacesnake','website']],
    ['home','/overviews/home.html','All articles','red',['life2','words','unweaving','soap','jupiter','economy','life','spacesnake','website','who']]
    ]

#serve the file. This works on heroku after you CLI 'heroku config:set ON_HEROKU=1'
if 'ON_HEROKU' in os.environ:
    if __name__ == "__main__":
        app.debug = False
        port = int(os.environ.get('PORT', 33507))
        waitress.serve(app, port=port)
else:
    app.run(debug=True)
