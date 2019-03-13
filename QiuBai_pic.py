import requests
from lxml import etree
from fake_useragent import UserAgent

# the basic format of the url

url = 'https://www.qiushibaike.com/pic/page/{}/?s=5174841'
headers = {
    "User-Agent": UserAgent().chrome
}
proxies = {'http': '183.148.152.153:31923'}
# The whole page number is 35, and 0, 1 page will be redirected to the same page
for i in range(35):
    if i == 0:
        continue
    rp = requests.get(url.format(i), headers=headers, proxies=proxies)
    # Use xpath to get the picture's href
    e = etree.HTML(rp.text)
    pic_urls = e.xpath('//div[@class="thumb"]//img/@src')
    # Download the pictures
    for j in range(len(pic_urls)):
        pic_urls[j] = 'https:' + pic_urls[j]
        with open('QiuBai/pic' + str(i) + str(j) + '.jpg', 'wb') as file:
            pic = requests.get(pic_urls[j], headers=headers)
            file.write(pic.content)
