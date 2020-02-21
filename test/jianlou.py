import requests
import re

con = list()

url = "http://www.heiyan.org/jianlou1/"
response = requests.get(url)
novel_text = response.text
# print(novel_text)

# 获取小说章节链接

ss = r'<li><a href="(\d+.html)">'
chapter = re.findall(ss, novel_text, re.S)
# print(chapter)
for each_chapter in chapter:
    chapter_con = 'http://www.heiyan.org/jianlou1/' + each_chapter
    con.append(chapter_con)
    # 判断是否重复
print(len(con))
print(len(set(con)))
# print(con)

#  获取小说的章节内容并写入文件中
with open("C:\Me\python_about\捡漏.txt", 'w', encoding='utf-8') as file:
    for each_content in con:
        content = requests.get(each_content)
        novel_content = content.text
        title = re.findall(r'<h1>(.+)</h1>', novel_content, re.S)
        title_new = title[0].replace('捡漏|', '')
        file.write('\n\n\n' + title_new)
        C_content = re.findall(r'<div class="contentbox">(.+)<strong>捡漏最新章节', novel_content, re.S)
        if "&nbsp;&nbsp;&nbsp;&nbsp;" in C_content[0]:
            fin_content = C_content[0].replace("&nbsp;&nbsp;&nbsp;&nbsp;", '\n')
            if '<br />' in fin_content:
                fin_content = fin_content.replace('<br />', '')
                if '&mdash;' in fin_content:
                    fin_content = fin_content.replace('&mdash;', '')
                    if '请记住本书首发域名：。手机版阅读网址：<br/>' in fin_content:
                        fin_content = fin_content.replace('请记住本书首发域名：。手机版阅读网址：<br/>', '')
                        if '<br/>' in fin_content:
                            fin_content = fin_content.replace('<br/>', '')
                            if '<br/>' in fin_content:
                                fin_content = fin_content.replace('<br/>', '')
        file.write('\n' + fin_content)
        print('downloading...' + title_new + '\n' + fin_content)