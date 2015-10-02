import re
from BeautifulSoup import BeautifulSoup
import mechanize

br = mechanize.Browser()

br.addheaders = [('User-agent', 'Mozilla/5.0')]

url = ('https://en.wikipedia.org/wiki/List_of_American_comedy_films')
br.open(url) 
res = br.response().read()
soup = BeautifulSoup(res)
k = 0

for link in soup.findAll('a', attrs = {'href' : re.compile("^/wiki/")}):

	k+=1
	if k==200:
		break
	elif k<60:
		continue
		
	find = re.compile('/wiki/(.*?)"')
	searchMovie = re.search(find, str(link))
	movie = searchMovie.group(1)
	url = ('https://en.wikipedia.org/wiki/' + movie)
	br.open(url)
	soup = BeautifulSoup(br.response().read())
	body = soup.find('span', attrs = {'id' : 'Plot'})
	i = ''
	if body != None:
		print soup.title.text
		nextE = body.findNext('p')
		while nextE.name != "h2":
			if nextE.name == "p":
				i = i + nextE.text + '\n\n'
			nextE = nextE.findNext()
		i = i.encode('ascii', 'ignore')
		outFile = open('your folder destination' + movie + '.txt', 'w')
		outFile.write(str(i))
outFile.close()
