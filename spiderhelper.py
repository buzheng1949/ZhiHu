#coding=utf-8
import requests
from bs4 import BeautifulSoup
import re
import json
class SpiderHelper:
    def __init__(self):
        self.datas = []

    def downloaderNetHTML(self,url,type):
        ret = requests.get(url,headers = { 'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20' })
        if ret.status_code == 200:
            if type =='json':
                return ret.json()
            else:
                return ret.text 
    def parseHTML(self,ret):
        if ret is None:
            return 
        else:
            soup = BeautifulSoup(ret,'html.parser',from_encoding='utf-8')
            nodes = soup.find_all('a',class_='link-button')
            for node in nodes:
                data = {}
                href = 'https://daily.zhihu.com'+node['href']
                image = node.find('img',class_='preview-image')['src']
                title = node.find('span',class_='title').get_text()
                data['href'] = href
                data['image'] = image
                data['title'] = title
                self.datas.append(data)
        return self.datas
    def get_datas(self):
        ret = self.downloaderNetHTML("https://daily.zhihu.com",type='html')
        return self.parseHTML(ret)
        
        
# 测试代码
def main():
    # 解决字典打印问题
    spider = SpiderHelper()
    print json.dumps(spider.get_datas(), encoding="UTF-8", ensure_ascii=False)

if __name__ == '__main__':
    main()