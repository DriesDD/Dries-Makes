from flask_frozen import Freezer
from build import app, ARTICLES, OVERVIEWS

freezer = Freezer(app)

app.config['FREEZER_DESTINATION'] = 'DriesDD.github.io'

@freezer.register_generator
def page_url_generator():
    for article in ARTICLES:
        yield '/'+article[0]+'.html'
    for overview in OVERVIEWS:
        yield '/'+overview[0]+'.html'

if __name__ == '__main__':
    freezer.freeze()
    freezer.run(debug=True)