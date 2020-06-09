import requests
# r = requests.get("http://www.baidu.com")
# r.encoding = "utf-8"

r = requests.post( 'https://service-trunk.xiaoyuncai.com/api/login',data = {"key":"value"})
print(r.text)


