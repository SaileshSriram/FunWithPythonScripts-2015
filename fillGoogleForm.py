import mechanize

def select_form(form):
	return form.attrs.get('id', None) == 'ss-form'

br = mechanize.Browser()

br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Firefox')]

url = ('http://goo.gl/forms/')

response = br.open(url)

for form in br.forms():
	print form.name

br.select_form(predicate = select_form)
br.form['entry.1347418895'] = 'foo'
br.form['entry.1940205853'] = 'bar' 
br.form['entry.5923354_month'] = ['11']
br.form['entry.5923354_day'] = ['19']
br.form['entry.5923354_year'] = ['2015']
br.form['entry.1410404341'] = ['2']
br.form['entry.1947739601'] = ['A', 'B']
br.submit()

