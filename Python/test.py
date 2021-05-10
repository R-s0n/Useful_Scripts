import requests, json
from bs4 import BeautifulSoup

r = requests.post('http://webscantest.com/crosstraining/aboutyou.php', data={'fname':'<img src=https://webhook.site/d4949c2c-ed32-427a-830f-b81a8ad5f0ae?test=1>'})
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.find_all('img'))
f = open('/tmp/test.html', 'w')
f.write(str(soup.img))
f.close

# 1. Pull URL from DB
# 2. Send request for each endpoint and parameter (get, post, put)
# 3. Add all img tags returned to list
# 4. Build html report with img tags, numbers to identify which payloads worked