import urllib.request
import json
url="https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH,LTC&tsyms=EUR&e=CCCAGG"
r=urllib.request.urlopen(url)
html=r.read()
html=html.decode()
d=json.loads(html)
file = input("Ονομα αρχείου: ")
f = open(file, 'r')
f = f.read()
f = json.loads(f)
dict = {
  "BTC": "39577.49",
  "ETH": "1247.56",
  "LTC":"144.56"
}
print('Τα αποτελέσματα είναι:')
print(f)
print('Σε ευρώ είναι: ')
print(dict)








