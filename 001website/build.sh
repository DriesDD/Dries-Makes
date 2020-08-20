#!/bin/bash
#create page variable which will have the page title name after the // + .html
page=$(grep -oP '(?<=// ).*?(?=</h1>)' article.html)
page="${page}.html"
page=${page// /_}
#combine head, nav, article and foot files to a single page file
cat ../head.html ../nav.html article.html ../foot.html > $page
#grab the content of the h1 element from the article...
v=$(grep -oP '(?<=<h1> ).*?(?=</h1>)' article.html)
#...and put it inside of the placeholder 'titletarget' in the header element
sed -i 's|titletarget|'"$v"'|g' $page
#now grab all tags...
v=$(grep -oP '(?<="tag">#).*?(?=</span>)' article.html | tr '\n' ',')
#and put them in the 'tagtarget' placeholder
sed -i 's|tagtarget|'"$v"'|g' $page
