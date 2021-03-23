import pdfplumber
import pandas as pd
import csv
import urllib3
urllib3.disable_warnings()
import re
import time

class paper_struct:
    def __init__(self):
        self.title = ""  # 标题
        self.authors = ()  # 作者
        self.pdf = ""  # pdf 地址
        self.subject = ()  # 分类
        self.arxiv = 0  # arxiv 编号

class paper_crwaler:
    def __init__(self, count):
        self.header = \
            {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1 Safari/605.1.15',
                'Host': 'arxiv.org',
                'Connection': 'keep-alive',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Encoding': 'br, gzip, deflate',
                'Cookie': '_pk_id.538.1db2=ccba8d546a606c4b.1528718980.1.1528719368.1528718980.; browser=202.200.81.4.1528718962819043; '
                          'BIGipServer~SVCCENTER~arxiv-web.arxiv.org_http_pool=rd822o00000000000000000000ffff8054040do80',
                'Accept-Language': 'zh-cn',
            }
        self.count=count
        self.http = urllib3.PoolManager()
        self.response = self.http.request("GET", self.create_url(count), headers=self.header)
        self.page = self.response.data
        self.page = self.page.decode()

        self.papers = []
        #self.titles = []
        self.authors = []
        self.arxives = []
        self.pdfs = []
        #self.subject = []

    def create_url(self, count=20):
        url = 'https://arxiv.org/list/cs/pastweek?'
        # count 最小是 5, 最大 854
        skip = 0
        if count < 5:
            count = 5
        if count > 854:
            count %= 854
            count -= 1
            skip = count / 854
        tmp = url+'skip='+ str(skip)+'&show='+str(count)
        # skip 指定开始位置， show 指定本页显示数量
        return tmp

    def test(self):
        if self.response.status != 200:
            print(self.response.status)

    def get_title(self):
        pattern = re.compile('<span class="descriptor">Title:</span>(.*?)</div>', re.S)
        #self.titles = pattern.findall(self.page)
        return pattern.findall(self.page)

    def get_authors(self):
        # 先获取div，然后对 div 内容分组
        #
        #
        pattern_dd = re.compile('<dd>(.*?)</dd>', re.S)
        pattern_f = re.compile('<div class="list-authors">(.*?)</div>', re.S)
        pattern_s = re.compile('<a href="/search\?searchtype=author&query=.*?">(.*?)</a>', re.S)

        dd = pattern_dd.findall(self.page)
        dd = str(dd)
        print("dd is"+ dd)

        tmp = pattern_f.findall(dd)
        tmp = str(tmp)
        print("tmp is"+ tmp)

        self.authors = pattern_s.findall(tmp)
        print(self.authors)

    def get_subject(self):
        pattern = re.compile('<span class="primary-subject">(.*?)</span>', re.S)
        #self.subject = pattern.findall(self.page)
        return pattern.findall(self.page)

    def get_arxiv(self):
        pattern = re.compile('<a href="/abs/(.*?)" title="Abstract">arXiv:.*?</a>', re.S)
        self.arxives = pattern.findall(self.page)

    def get_pdf(self):
        for i in range(len(self.arxives)):
            self.pdfs.append('https://arxiv.org/pdf/' + self.arxives[i])

    def create_paper(self):
        for i in range(self.count):
            self.papers.append(paper_struct())
            #self.papers[i].title = self.titles[i]
            self.papers[i].title = self.get_title()[i]
            self.papers[i].arxiv = self.arxives[i]
            self.papers[i].pdf = self.pdfs[i]
            #self.papers[i].subject = self.subject[i]
            self.papers[i].subject = self.get_subject()[i]
            self.papers[i].authors = self.authors
            #print(self.papers[0].authors)

    def download_pdf(self):
        http = urllib3.PoolManager()
        li = []
        for i in range(self.count):
            response = http.request('GET', self.papers[i].pdf, headers=self.header)
            self.test()
            filename=self.papers[i].title
            with open(filename.strip("\n") + '.pdf', 'wb') as file:
                file.write(response.data)
                file.close()
                response.release_conn()
            with pdfplumber.open(filename.strip("\n") + '.pdf') as pdf:
                for page in pdf.pages:
                    content=page.extract_text()
                    regular = re.compile(r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}\b")
                    if len(re.findall(regular, content)):
                        # print(re.findall(regular, content))
                        li.append(re.findall(regular, content))
                        # Open File
                        # csvFile2 = open('csvFile2.csv', 'w', newline='')  # 设置newline，否则两行之间会空一行
                        # writer = csv.writer(csvFile2)
                        # for i in li:
                        #     writer.writerow(i)
                        # csvFile2.close()
        print(li)
        output = open('email.csv', 'w', newline='')
        writer = csv.writer(output)
        for row in li:
            for r in row:
                if row:  # 去除空行
                    writer.writerow([r])
        print("保存文件成功，处理结束")


def main(count):
    t_start = time.time()
    pc = paper_crwaler(count)
    pc.test()
    pc.get_title()
    #pc.get_authors()
    pc.get_arxiv()
    pc.get_pdf()
    pc.get_subject()
    pc.create_paper()
    pc.download_pdf()
    print(time.time() - t_start)

if __name__ == '__main__':
    main(10)
