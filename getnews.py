import urllib.request, json, datetime
from bs4 import BeautifulSoup
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

sid = SIA()

def get_day_article_urls(query, date):
	url = 'https://api.nytimes.com/svc/search/v2/articlesearch.json?q=%22' + query + '%22&fq=pub_date:("' + date + '")&fl=web_url&api-key=Ndg99yFAJsBjIa4oclBK98F5eZfL361C'
	request = urllib.request.urlopen(url)
	data = json.load(request)
	article_urls=[]

	for article in data['response']['docs']:
		article_urls.append(article['web_url'])
	return(article_urls)

def get_article_text(article_url):
	html = urllib.request.urlopen(article_url)
	soup = BeautifulSoup(html.read(), "lxml")
	story = soup.find(id='story')
	paragraphs = story.find_all(class_='css-1ygdjhk evys1bk0')
	text = ''
	for p in paragraphs:
		text = text + ' ' + p.get_text()
	return(text)

def determine_applicable(article_text, query):
	if query in article_text:
		return True
	return False	

def convert_date(date):
	date_format = '%m/%d/%Y'
	datetime_obj = datetime.datetime.strptime(date, date_format)
	return(datetime_obj.date())


#query is word in article wanted
#date is date like YYYY-MM-DD
def get_useful_articles(query, date):
	converted_date = convert_date(date)
	articles = get_day_article_urls(query, converted_date)
	useful = []
	for article in articles:
		text = get_article_text(article)
		if determine_applicable(text, query):
			sentiment = sid.polarity_scores(text)['compound']
			useful.append([sentiment, article, text])
	return(useful)







	

