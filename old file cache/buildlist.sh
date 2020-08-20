echo -n "" > articlelist.txt 
for D in */; do
if [ -f "${D}"article.html ]
then
    v=$(grep -oP '(?<=// ).*?(?=</h1>)' "${D}"article.html)
    echo -n "title:" >> articlelist.txt 
    echo -n "$v" >> articlelist.txt
    echo -n "|link:" >> articlelist.txt 
    v="${v}.html"
    v=${v// /_}
    echo -n "$v" >> articlelist.txt
    echo -n "|tag:" >> articlelist.txt
    v=$(grep -oP '(?<=tag">).*?(?=</span>)' "${D}"article.html | head -1 )
    echo -n "$v" >> articlelist.txt
    echo -n "|" >> articlelist.txt
fi ; done
