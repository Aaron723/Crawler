import requests
from fake_useragent import UserAgent

url = 'https://www.douban1231231.com/'
headers = {
    "User-Agent": UserAgent().chrome
}
# proxies = {'http': '47.88.193.14', 'http': '36.226.115.250'}
proxies = {'http': '183.148.152.153:31923'}
try:
    rp = requests.get(url, headers=headers, proxies=proxies)
    print(rp.text)
except requests.exceptions.ConnectionError as e:
    print("error!")

