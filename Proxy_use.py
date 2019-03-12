import requests

from fake_useragent import UserAgent

url = 'http://httpbin.org/get'
headers = {
    "User-Agent": UserAgent().chrome
}
# proxies = {'http': '47.88.193.14', 'http': '36.226.115.250'}
proxies = {'http': '183.148.152.153:31923'}
rp = requests.get(url, headers=headers, proxies=proxies)

print(rp.text)
