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
   
#now copy this to individual pages, appropriately replace one with the 'selected' tag and cull if too long

for D in */; do
if [ -f "${D}"article.html ]
then
    cat fullnav.html > "${D}"nav.html
    v=$(grep -oP '(?<=// ).*?(?=</h1>)' "${D}"article.html)
    v="${v}.html"
    v=${v// /_}
    sed -i "s/navitem' href=..\/$v/selected'/" "${D}"nav.html
fi ; done

