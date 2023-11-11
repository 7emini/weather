import requests

url = 'https://restapi.amap.com/v3/weather/weatherInfo?parameters'
parems = {
    'key':'5266bd0984d65332aff49bd1774706e6',
    'city':'370500',
    'extensions':'all',
    'output':'JSON'
}

r = requests.get('https://restapi.amap.com/v3/weather/weatherInfo?parameters', params=parems)

# print(r.json())
print(r.text)