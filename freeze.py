from flask_frozen import Freezer
from build import app, ARTICLES, OVERVIEWS

freezer = Freezer(app)

app.config['FREEZER_DESTINATION'] = 'frozen'

@freezer.register_generator
def page_url_generator():
    for article in ARTICLES:
        yield '/'+article[0]
    for overview in OVERVIEWS:
        yield '/'+overview[0]

if __name__ == '__main__':
    freezer.freeze()
    freezer.run(debug=True)