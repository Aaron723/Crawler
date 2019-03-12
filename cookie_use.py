import requests
from fake_useragent import UserAgent

login_url = 'https://www.sxt.cn/index/login/login'
form_data = {
    'user': '17703181473',
    'password': '123456'
}
headers = {
    "User-Agent": UserAgent().chrome
}

response = requests.post(login_url, headers=headers, data=form_data)
base_url = 'https://www.sxt.cn/index/user.html'
# print(response.cookies)
res = requests.get(base_url, headers=headers, cookies=response.cookies)
print(res.text)
# print(response.text)
