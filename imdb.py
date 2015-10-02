import urllib2
import sys
from BeautifulSoup import BeautifulSoup
sys.stdout = open('imdb.txt','w')
opener = urllib2.build_opener()
opener.addheaders=[('User-agent','Mozilla/5.0')]

url = "http://www.imdb.com/search/title?release_date=2005,2015&title_type=feature"
ourUrl = opener.open(url).read()
soup = BeautifulSoup(ourUrl)
count = 0
# Fetching the value present within tag table with class=results
movie = soup.findChildren('table','results')

# Changing the movie into an iterator
iterMovie = iter(movie[0].findChildren('tr'))
#print type (iterMovie)
next(iterMovie)
# Finding tr in itermovie. Every tr tag contains information of a movie.
for tr in iterMovie:
	imgSource = tr.findChildren('td','image')[0].find('img')['src'].split('._V1.')[0]+'._V1_SX214_AL_.jpg'
	movie = tr.findChildren('td','title')
	title = movie[0].find('a').contents[0]
	year = movie[0].find('span','year_type').contents[0]
	#fetch genres
	genres = movie[0].find('span','genre').findAll('a')
	genres = [g.contents[0] for g in genres]
	try:
		runtime = movie[0].find('span','runtime').contents[0]
	except:
		runtime = "Not given"
	try:
		rating  = movie[0].find('span','value').contents[0]
	except:
		rating = "Not given"

	print '***************IMDB MOVIE LIST******************'
	print "S.No of the movie --> ",
	count += 1
	print count
	print 'Title -->' + title
	print 'Genres -->',
	for item in genres:
		if genres.index(item) == len(genres)-1:
			print(item.decode('UTF-8','strict'))
		else:
			print(item.decode('UTF-8','strict')+','),

	print "Runtime --> " + runtime
	print 'Rating -->' + rating
	print "Image source -->"+imgSource

