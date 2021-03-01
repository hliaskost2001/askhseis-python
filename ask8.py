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
  "BTC": "54267.673556",
  "ETH": "10797,677999999998",
  "LTC":"182.01"
}

print('Τα αποτελέσματα είναι:')
print(f)
print('Σε ευρώ είναι: ')
print(dict)






