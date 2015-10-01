import urllib2
from BeautifulSoup import BeautifulSoup

opener = urllib2.build_opener()
opener.addheaders=[('User-agent','Mozilla/5.0')]

url = "http://www.imdb.com/search/title?release_date=2010,2015&title_type=feature"
ourUrl = opener.open(url).read()
soup = BeautifulSoup(ourUrl)

# Fetching the value present within tag table with class=results
movie = soup.findChildren('table','results')

# Changing the movie into an iterator
iterMovie = iter(movie[0].findChildren('tr'))

# Finding tr in itermovie. Every tr tag contains information of a movie.
for tr in iterMovie:
	#try doing some stuff here