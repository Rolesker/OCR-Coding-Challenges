import httplib2
from bs4 import BeautifulSoup, SoupStrainer

http = httplib2.Http()
status, response=http.request("https://www.bbc.co.uk/news")

for title in BeautifulSoup(response, 'html.parser', parse_only=SoupStrainer('h3')):
    if title.string:
        print(title.string)