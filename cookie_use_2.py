import requests
from fake_useragent import UserAgent
import json
import cookielib
login_url = 'https://www.sxt.cn/index/login/login'
form_data = {
    'user': '17703181473',
    'password': '123456'
}
headers = {
    "User-Agent": UserAgent().chrome
}
se = requests.session()

response = se.post(login_url, headers=headers, data=form_data) # put all the requests in one session to save the cookie

base_url = 'https://www.sxt.cn/index/user.html'
res = se.get(base_url, headers=headers)
# print(res.text)



