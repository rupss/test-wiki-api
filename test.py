import mwclient

def test(): 
	site = mwclient.Site('en.wikipedia.org')
	page = site.Pages['Wakka_Wakka']
	text = page.edit()
	print text.encode('utf-8')


if __name__ == "__main__": 
	test()