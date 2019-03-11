import requests
# import ssl
from urllib.parse import urlencode
# ssl._create_default_https_context = ssl._create_unverified_context
url = 'https://www.sxt.cn/index/login/login.html'
headers = {
    "User-Agent":
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
}

form_data = {
   'user': '17703181473',
    'password': '123456'
}
# f_data = urlencode(form_data)
response = requests.post(url, data=form_data, headers=headers)
print(response.text)
