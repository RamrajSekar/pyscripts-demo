from urllib.request import urlopen,URLError

request = 'http://placekitten.com/'

response = urlopen(request)
kittens = response.read()
a = kittens[559:1000]
print(a)


# Another way to Make a GET request here and assign the result to kittens:
##kittens = request.get("http://placekitten.com/")
##print (kittens.text[559:1000])

