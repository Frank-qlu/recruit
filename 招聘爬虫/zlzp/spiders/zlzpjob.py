#author Frank_Lee
# email=lizhipengqilu@gmail.com
#2019/3/21
# -*- coding: utf-8 -*-
import scrapy
# from scrapy.linkextractors import LinkExtractor
# from scrapy.spiders import CrawlSpider, Rule
from zlzp.items import ZlzpItem


class ZlzpjobSpider(scrapy.Spider):
    name = 'zlzp'
    allowed_domains = ['51job.com']

    url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,%25E5%25A4%25A7%25E6%2595%25B0%25E6%258D%25AE,2,'
    offset = 1
    start_urls = [url + str(offset) + ".html?"]
    # rules = (
    #     Rule(LinkExtractor(allow=r'%25E5%25A4%25A7%25E6%2595%25B0%25E6%258D%25AE,2,\d+.html?')),
    #     Rule(LinkExtractor(allow=r'\d+.html?s=01&t=0'),callback='parse_item',follow=False),
    # )
    #处理请求的方法
    def parse(self, response):
        # item = ZlzpItem()
        # item['publictime'] = response.xpath('')
        # yield item
        links = response.xpath('//div[@class="el"]/p/span/a/@href').extract()
        #迭代取出每个集合里的链接
        for link in links:
            #print(link)
            #提取列表里每个链接，发送请求并调用callback处理
            yield scrapy.Request(link,callback=self.parse_item)

        if self.offset <= 1073:
            self.offset += 1
            yield scrapy.Request(self.url + str(self.offset) + ".html?",callback=self.parse)
    #处理详情页信息的方法
    def parse_item(self, response):

        item = ZlzpItem()

        #公司名字
        item['cname'] = response.xpath('//div[@class="in"]/div/p/a/@title').extract()[0]
        # 职位名字
        item['pname'] = response.xpath('//div[@class="in"]/div/h1/@title').extract()[0]
        # 工作地点
        workplace = response.xpath('//div[@class="cn"]/p[2]/text()').extract()[0]
        item['workplace'] = workplace.strip().split("-")[0]
        # 公司福利
        welfare = response.xpath('//div[@class="jtag"]/div/span/text()').extract()
        if welfare == []:
            item['welfare'] = "五险一金,绩效奖金,年终奖金"
        else:
            item['welfare'] = ",".join(welfare)
        # 薪水
        salarys = response.xpath('//div[@class="in"]/div/strong/text()').extract()
        if salarys == []:
            item['salary'] = ""

        else:
            item['salary'] = salarys[0].split("-")[0]

            # for salary in salarys:
            #      = salarys*10000

        # 学历
        education = response.xpath('//div[@class="cn"]/p[2]/text()').extract()[2]
        item['education'] = education.strip()
        # 工作经验
        experience = response.xpath('//div[@class="cn"]/p[2]/text()').extract()[1]
        item['experience'] = experience.strip().replace("经验","").replace("无工作","不限")
        #renzhi
        list = response.xpath('//div[@class="tCompany_main"]//div[@class="bmsg job_msg inbox"]/ol/li/text() | //div[@class="tCompany_main"]//div[@class="bmsg job_msg inbox"]/p/span/text() | //div[@class="tCompany_main"]//div[@class="bmsg job_msg inbox"]/p/b/text() | //div[@class="tCompany_main"]//div[@class="bmsg job_msg inbox"]/p/text() | //div[@class="tCompany_main"]//div[@class="bmsg job_msg inbox"]/div/text() | //div[@class="tCompany_main"]//div[@class="bmsg job_msg inbox"]/text() | //div[@class="tCompany_main"]//div[@class="bmsg job_msg inbox"]/ol/li/p/span/text()').extract()
        item['requirement'] = "".join(list).strip().replace("岗位职责:","").replace("职位描述:","").replace(" ","")
        # 公司类型
        item['ctype'] = response.xpath('//div[@class="com_tag"]/p[1]/text()').extract()[0]
        # 公司规模
        scale = response.xpath('//div[@class="com_tag"]/p[2]/text()').extract()
        if scale == []:
            item['scale'] = "50-150人"
        else:
            item['scale'] = scale[0]
        # 公司性质
        nature = response.xpath('//div[@class="com_tag"]/p[3]/@title').extract()
        if nature == []:
            item['nature'] = "上市公司"
        else:
            item['nature'] = nature[0]
        # 详情链接
        item['dlink'] = response.url

        #交给管道文件处理数据
        yield item

