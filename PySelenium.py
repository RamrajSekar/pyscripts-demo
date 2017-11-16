from selenium import webdriver
##from selenium.webdriver.common.keys import keys

fbrw = webdriver.Firefox()
fbrw.get("http://www.gmail.com")
assert "Google" in fbrw.title

