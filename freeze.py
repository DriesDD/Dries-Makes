from flask_frozen import Freezer
from build import app, ARTICLES, OVERVIEWS
import os

freezer = Freezer(app)

app.config['FREEZER_DESTINATION'] = 'DriesDD.github.io'

@freezer.register_generator
def page_url_generator():
    for article in ARTICLES:
        yield '/'+article[0]
    for overview in OVERVIEWS:
        yield '/'+overview[0]

if __name__ == '__main__':
    freezer.freeze()
    freezer.run(debug=True)

for article in ARTICLES:        
    os.rename('DriesDD.github.io/'+article[0],'DriesDD.github.io/'+article[0]+'.html')
for overview in OVERVIEWS:        
    os.rename('DriesDD.github.io/'+overview[0],'DriesDD.github.io/'+overview[0]+'.html')