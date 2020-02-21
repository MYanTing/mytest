import requests
from pyquery import PyQuery as pq

novel_classify = list()
all_novel_classify = list()
all_novel_link = set()
headers = {'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
           'Accept - Encoding': 'gzip, deflate',
           'Accept-Language': 'zh-Hans-CN, zh-Hans; q=0.5',
           'Connection': 'Keep-Alive',
           'Host': 'www.heiyan.org',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36 Edg/80.0.361.54'}


def download_by_requests(link, headers, timeout=500):
    response = requests.get(link, headers=headers, timeout=timeout)
    print(response.status_code)
    return response


url = "http://www.heiyan.org/"
home_page = requests.get(url, headers)
home_page_text = pq(home_page.text)

# 获取网站小说类别链接
doc = home_page_text.find('.menu')
its = doc("a").items()  # 结果是生成迭代器
for it in its:
    classify_link = 'http://www.heiyan.org' + it.attr('href')
    novel_classify.append(classify_link)
all_novel_classify = novel_classify[1:]
print(all_novel_classify)

# 获取每个类别下小说名称链接
for link_classify in all_novel_classify:
    print(link_classify)
    try:
        response_classify = download_by_requests(link_classify, headers)
        text_classify = pq(response_classify.text)
        doc_classify = text_classify.find('.news.section-cols')
        its_classify = doc_classify.find("a").items()
        for item in its_classify:
            name_novel = 'http://www.heiyan.org' + item.attr('href')
            all_novel_link.add(name_novel)
            print(len(all_novel_link))

    except Exception as e:
        print(link_classify)
        print(e)


# 获取每个小说的章节链接













