import bs4 as bs
import urllib.request
import openpyxl as exl
import os
#To get the current working directory
print(os.getcwd())
#'http://www.pythonforbeginners.com'
weburl = 'http://www.reddit.com' 
sauce =urllib.request.urlopen(weburl).read()

##Unstructure source will be displayed
#print(sauce)

soup = bs.BeautifulSoup(sauce,'lxml')
##Unstructure source will be displayed
#print(soup)
#print(soup.prettify())

##To print page title
print(soup.title)

##To print page title without tags
page_title = soup.title.string
print(page_title)

##To print a first paragh in a page
print('---print a first paragh in a page---')
print(soup.p)

##To print all paragh in a page
print('---print all paragh in a page---')
#print(soup.find_all('p'))


print('---print all paragh in a page without tags---')
for paragraph in soup.find_all('p'):
    print(paragraph.text)

print('---print all links in a page---')
for alink in soup.find_all('a'):
    print(alink.get('href'))

print('---print all texts in a page---')
print(soup.get_text())

