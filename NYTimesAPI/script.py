from urllib2 import urlopen
from json import loads
import codecs, sys
import os 

sys.stdout = codecs.getwriter('UTF-8')(sys.stdout)

try:
    os.remove("output.txt")
except OSError:
    pass

def call_the_articles():
    url = "http://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/30.json?&offset=%s&api-key=a1f2de9c74a24d2cf3f72d910ff68018:14:61296924"
    # url = "http://api.nytimes.com/svc/movies/v2/reviews/search.xml?&query=Potter&opening-date=2001-11-01;2011-07-31&api-key=ecaf47b08580b6c079f40da2d96a107a:2:67632807"
    return loads(urlopen(url).read())

articles = call_the_articles()
g = "a"

f = codecs.open('output.txt', 'w', encoding='utf-8')
for story in articles["results"]:
    f.write(story["title"] + "\n")
    try:
        g = g + story["title"] + "\n"
    except:
        g = g + " \n"
f.close()
print g



	# try:
	# 	p = Page.objects.get(pk=page_id)
	# except:
	# 	raise Http404