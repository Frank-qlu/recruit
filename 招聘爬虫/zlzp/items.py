#author Frank_Lee
# email=lizhipengqilu@gmail.com
#2019/3/21
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZlzpItem(scrapy.Item):

    #公司名字
    cname = scrapy.Field()
    #职位名字
    pname = scrapy.Field()
    # 工作地点
    workplace = scrapy.Field()
    # 公司福利
    welfare = scrapy.Field()
    # 最低薪水
    salary = scrapy.Field()
    # 学历
    education = scrapy.Field()
    # 工作经验
    experience = scrapy.Field()
    #任职要求
    requirement = scrapy.Field()
    #公司类型
    ctype = scrapy.Field()
    #公司规模
    scale = scrapy.Field()
    #公司性质
    nature = scrapy.Field()
    #发布时间
    publictime = scrapy.Field()
    # 详情链接
    dlink = scrapy.Field()