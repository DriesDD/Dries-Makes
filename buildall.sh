#this is a bash script. To execute, use bash build.sh.

#build fullnav.html

echo -n "<body>
    <header>
      <div id='navtarget'>
        <nav id='navsource' class='navcontainer'>
            <div class='navarrow'> >> </div>
            " > fullnav.html
            
for D in */; do
if [ -f "${D}"article.html ]
then
    v=$(grep -oP '(?<=<a class=").*?(?= tag)' "${D}"article.html | head -1 )
    echo -n "<a class='" >> fullnav.html 
    echo -n "$v" >> fullnav.html
    echo -n " navitem' href=../" >> fullnav.html
    v=$(grep -oP '(?<=// ).*?(?=</h1>)' "${D}"article.html)
    v="${v}.html"
    v=${v// /_}
    echo -n $v >> fullnav.html
    echo -n ">" >> fullnav.html
    v=$(grep -oP '(?<=// ).*?(?=</h1>)' "${D}"article.html)
    echo -n "$v" >> fullnav.html
    echo -n "</a>" >> fullnav.html
fi ; done

echo -n "
</nav>
      </div>
   </header>" >> fullnav.html
   
#now copy this to individual pages, appropriately replace one with the 'selected' tag and cull if too long (culling not implemented yet)

for D in */; do
if [ -f "${D}"article.html ]
then
    cat fullnav.html > "${D}"nav.html
    v=$(grep -oP '(?<=// ).*?(?=</h1>)' "${D}"article.html)
    v="${v}.html"
    v=${v// /_}
    sed -i "s/navitem' href=..\/$v/selected'/" "${D}"nav.html
    #now build the actual page
  	  #create page variable which will have the page title name after the // + .html
	page=$(grep -oP '(?<=// ).*?(?=</h1>)' "${D}"article.html)
	page="${page}.html"
	page=${page// /_}
	#combine head, nav, article and foot files to a single page file
	cat head.html "${D}"nav.html "${D}"article.html foot.html > "${D}"$page
	#grab the content of the h1 element from the article...
	v=$(grep -oP '(?<=<h1> ).*?(?=</h1>)' "${D}"article.html)
	#...and put it inside of the placeholder 'titletarget' in the header element
	sed -i 's|titletarget|'"$v"'|g' "${D}"$page
	#now grab all tags...
	v=$(grep -oP '(?<="tag">#).*?(?=</span>)' "${D}"article.html | tr '\n' ',')
	#and put them in the 'tagtarget' placeholder
	sed -i 's|tagtarget|'"$v"'|g' "${D}"$page

fi ; done


