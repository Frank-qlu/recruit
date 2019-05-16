# recruit
招聘爬虫+数据分析
1.爬虫：
    采用Scrapy 分布式爬虫技术，使用mongodb作为数据存储，爬取的网站Demo为51job，数据我目前爬了有几千条
2.数据处理：
     采用pandas对爬取的数据进行清晰和处理
2.数据分析：
    采用flask后端获取mongodb数据，前端使用bootstrap3.echarts以及D3的词云图

###注意：1. pymongo安装版本 <=3.0 建议 pip install pymongo==2.8###
        2. 如果scrapy安装不上，在这上面查找https://www.lfd.uci.edu/~gohlke/pythonlibs/ 先安装对应版本 twisted ，再安装scrapy就没问题。
        3.mongodb启动，进入安装mongodb的文件夹的bin目录下面，输入 mongod --dbpath= data文件夹路径
#####

###
关于项目启动
1. 爬虫：
    
   1.cd 目录
   2. pip install pymongo==2.8
   3. scrapy crawl zlzp
2. 数据可视化
   1. 激活虚拟环境 cd venv/Scripts
                  activate
   2. python zlzpView.py
###
       
###
该项目适合新手学习和交流，如果有任何问题请联系我Email: lizhipengqilu@gmail.com
同时希望大家提出宝贵意见，欢迎学习交流，如果你喜欢该项目，请收藏或者fork一下，你的主动将是我前行的动力
</br></br>由于服务器运行需要成本，如果你想贡献，欢迎捐赠，非常感谢。
<img src="https://github.com/Frank-qlu/recruit/blob/master/%E6%8B%9B%E8%81%98%E7%88%AC%E8%99%AB/images/wei.jpg"  align="middle" height="400" width="400" />
###
<h4>version 1.0:</h4></br>
&nbsp; &nbsp;         首次更新项目</br>
<h4>version 2.0(2019-05-16更新):</h4></br>
 &nbsp;&nbsp;         1.优化界面，采用blueprint设计模，代码稍后更新</br>
   &nbsp;&nbsp;        2.添加高级搜索(聚合查找)</br>
    &nbsp;&nbsp;       3.添加前后台，增添redis数据库</br>
   &nbsp;&nbsp;        3. 后台设置招聘信息过期时间</br>
    &nbsp;&nbsp;       4.后台用户管理</br>
<h4>version 3.0(未来):</h4></br>
   &nbsp;&nbsp;        1.采用flask-restful</br>
    &nbsp;&nbsp;       2.优化数据分析模块</br>
    &nbsp;&nbsp;       3. 设置兴趣标签,添加推荐系统，相似职位推荐</br>
<h4>项目预览</h4>
###</br>
<img src="https://github.com/Frank-qlu/recruit/blob/master/%E6%8B%9B%E8%81%98%E7%88%AC%E8%99%AB/images/1.png" />
<img src="https://github.com/Frank-qlu/recruit/blob/master/%E6%8B%9B%E8%81%98%E7%88%AC%E8%99%AB/images/2.png" />
<img src="https://github.com/Frank-qlu/recruit/blob/master/%E6%8B%9B%E8%81%98%E7%88%AC%E8%99%AB/images/wordcount.png" />
<img src="https://github.com/Frank-qlu/recruit/blob/master/%E6%8B%9B%E8%81%98%E7%88%AC%E8%99%AB/images/education.png" />
<img src="https://github.com/Frank-qlu/recruit/blob/master/%E6%8B%9B%E8%81%98%E7%88%AC%E8%99%AB/images/experience.png" />
<img src="https://github.com/Frank-qlu/recruit/blob/master/%E6%8B%9B%E8%81%98%E7%88%AC%E8%99%AB/images/search.png" />
<img src="https://github.com/Frank-qlu/recruit/blob/master/%E6%8B%9B%E8%81%98%E7%88%AC%E8%99%AB/images/back.png" />