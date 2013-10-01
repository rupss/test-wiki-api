import mwclient, json
import MWApi

username = 'rupss'
password = 'creekview'

def test_get_wikipedia_page_data(): 
	site = mwclient.Site('en.wikipedia.org')
	page = site.Pages['Wakka_Wakka']
	text = page.edit()
	print text.encode('utf-8')
	print 'hello world'

def test_get_wikidata_page_data(): 
	site = mwclient.Site('test.wikidata.org')
	site.login(username, password)
	page = site.Pages['Q80']
	text = page.edit()
	print text.encode('utf-8')
	print '--------'
	obj = json.loads(text.encode('utf-8'))
	obj['description']['en'] = 'Successful change'
	print '---------'
	print type(json.dumps(obj))
	page.save(json.dumps(obj), 'Test change')

def sample(): 
	site = mwclient.Site('commons.wikimedia.org')
	site.login(username, password)  # Optional

	# Edit page
	page = site.Pages['Commons:Sandbox']
	text = page.edit()
	print 'Text in sandbox:', text.encode('utf-8')
	page.save(text + u'\nExtra data TEST', summary = 'Test edit')

def test_mwapi(): 
	obj = MWAPI('https://en.wikipedia.org')

if __name__ == "__main__": 
	#test_get_wikidata_page_data()
	#sample()
	test_mwapi()
