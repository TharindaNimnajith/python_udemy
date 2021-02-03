import requests

url1 = 'https://api.pwnedpasswords.com/range/' + 'password123'
res1 = requests.get(url1)
print(res1)
# <Response [400]>

url2 = 'https://api.pwnedpasswords.com/range/' + 'CBFDAC6008F9CAB4083784CBD1874F76618D2A97'
res2 = requests.get(url2)
print(res2)
# <Response [400]>

url = 'https://api.pwnedpasswords.com/range/' + 'CBFDA'
res = requests.get(url)
print(res)
# <Response [200]>
