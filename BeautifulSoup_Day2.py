import requests
from bs4 import BeautifulSoup as bs

page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
#With tag
print(page)
#Withot tag
print(page.status_code)

#print out the HTML content of the page, formatted nicely
soup = bs(page.content,'html.parser')
print(soup.prettify())

print(list(soup.children))

print([type(item) for item in list(soup.children)])

html = list(soup.children)[2]
print(html)
print(list(html.children))
