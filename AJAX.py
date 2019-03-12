import requests
import json
from jsonpath import jsonpath as jp
base_url = 'https://movie.douban.com/j/chart/top_list?type=13&interval_id=100%3A90&action=&start={}&limit=20'

headers = {
    "User-Agent":
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
}
i = 0
while True:
    url = base_url.format(i*20)
    response = requests.get(url, headers=headers)
    data = response.json()
    if data == [] or data is None:
        break
    Watch_titles = jp(data, '$..[title]')
    Watch_stars = jp(data, '$..[actors]')
    d = json.dumps(Watch_titles, ensure_ascii=False)
    s = json.dumps(Watch_stars, ensure_ascii=False)
    print(d)
    print(s)
    i += 1
# print(response.text)
