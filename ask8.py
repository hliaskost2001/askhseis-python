import urllib.request
import json
url="https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH,LTC&tsyms=EUR&e=CCCAGG"
r=urllib.request.urlopen(url)
html=r.read()
html=html.decode()
d=json.loads(html)
file = input("File name: ")
f = open(file, 'r')
f = f.read()
f = json.loads(f)
thisdict = {
  "BTC": "54267.673556",
  "ETH": "10797,677999999998",
  "LTC":"182.01"
}

print('Your portofolio is:')
print(f)
print('Which in Euros is: ')
print(thisdict)






