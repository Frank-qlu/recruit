#author Frank_Lee
# email=lizhipengqilu@gmail.com
#2019/3/21
import pymongo
import pandas as pd
client = pymongo.MongoClient('localhost', 27017)
db = client['51job']
collection = db['zhiwei']
# 读取数据
data = pd.DataFrame(list(collection.find()))
# 选择需要显示的字段
data = data[['pname',"workplace","education","salary","experience"]]
# 打印输出
data1=list(data['education'])
data2=list(data['experience'])
count_undergraduate=0
master=0
doctor=0
others=0
college=0
unlimited=0
unrestricted=0
graduate=0
one_year=0
almost_year=0
three_year=0
five_year=0
for data1 in data1:
    if data1=="本科":
        count_undergraduate=count_undergraduate+1
    elif data1=="硕士":
        master=master+1
    elif data1=="博士":
        doctor=doctor+1
    elif data1=="大专":
          college=college+1
    elif data1=="不限":
        unlimited=unlimited+1
    else:
        pass
for data2 in data2:
    if data2=="应届毕业生" or data2=="应届"or data2=="应届生":
        graduate=graduate+1
    elif data2=="不限":
        unrestricted=unrestricted+1
    elif data2=="1年"or data2=="2年"or data2=="1-2年":
        one_year=one_year+1
    elif data2=="3年"or data2=="4年"or data2=="3-4年":
        three_year=three_year+1
    elif data2=="5年"or data2=="6年"or data2=="5-7年":
        five_year=five_year+1
    elif data2=="一年以下":
        almost_year=almost_year+1
    else:
        pass
# print(count_undergraduate,master,doctor,college,unlimited)
# print(graduate,unrestricted,one_year,three_year,five_year,almost_year)