import urllib.request
import random

data = urllib.request.urlopen("https://www.jd.com/").read().decode("utf-8","ignore")
#print(data)

uapools=[
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363",
]
def UA():
    opener = urllib.request.build_opener()
    thisua = random.choice(uapools)
    ua = ("User-Agent",thisua)
    opener.addheaders = [ua]
    urllib.request.install_opener(opener)
    print("当前使用的UA："+str(thisua))

for i in range(0,10):
    print(i)
    UA()
    data = urllib.request.urlopen("https://www.jd.com/").read().decode("utf-8","ignore")