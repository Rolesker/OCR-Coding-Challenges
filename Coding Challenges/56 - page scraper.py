import httplib2
from bs4 import BeautifulSoup, SoupStrainer

site=input("Enter full url of website: ")
print()
seen={}

http = httplib2.Http()
status, response=http.request(site)

print("Hyperlinks:")
for link in BeautifulSoup(response, 'html.parser', parse_only=SoupStrainer('a')):
    if link.has_attr("href"):
        if not seen.get(link["href"]):
            print(link["href"])
            seen[link["href"]]=1
print()
print("Image links:")
for img in BeautifulSoup(response, 'html.parser', parse_only=SoupStrainer('img')):
    if img.has_attr("src"):
        if not seen.get(img["src"]):
            print(img["src"])
            seen[img["src"]]=1