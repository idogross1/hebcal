import requests

response = requests.get("https://www.hebcal.com/converter?cfg=json&hy=5749&hm=Kislev&hd=25&h2g=1")
date = response.json()
