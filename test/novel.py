import requests
from pyquery import PyQuery as pq

novel_classify = list()
all_novel_classify = list()
all_novel_link = set()

url = "http://www.heiyan.org/"
response = requests.get(url)
novel_text = pq(response.text)
# print(novel_text)
doc = novel_text.find('#cols-2')
print(doc)
its = doc("h3").items()   # 结果是生成迭代器
for it in its:
    classify_link = 'http://www.heiyan.org' + it.attr('href')
    novel_classify.append(classify_link)
print(novel_classify)

