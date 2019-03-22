#author Frank_Lee
# email=lizhipengqilu@gmail.com
#2019/3/21
from flask import Flask,render_template,request,g
from datetime import datetime
app = Flask(__name__)
import read_data
import pandas as pd


@app.route('/',methods=["POST","GET"])
def hello_world():
    if request.method == 'POST':
        zhiweis = request.form.get("zhiwei")
        zw = read_data.collection.find({"pname": {'$regex': zhiweis}})
        g.zw = zw
        return render_template("search.html")
    else:
        return render_template("index.html")
@app.route('/ciyun/',methods=["POST","GET"])
def ciyun():
    if request.method == 'POST':
        zhiweis = request.form.get("zhiwei")
        zw = read_data.collection.find({"pname": {'$regex': zhiweis}})
        g.zw = zw
        return render_template("search.html")
    else:
        return render_template("ciyun.html")
@app.route('/educate/',methods=["POST","GET"])
def education():
    if request.method=='POST':
       zhiweis=request.form.get("zhiwei")
       zw=read_data.collection.find({"pname":{'$regex': zhiweis}})
       g.zw=zw
       return render_template("search.html")
    else:
        g.master=read_data.master
        g.doctor=read_data.doctor
        g.undergraduate=read_data.count_undergraduate
        g.others=read_data.others
        g.unlimited=read_data.unlimited
        g.college=read_data.college
        g.time=datetime.now()
        return render_template("education.html")
@app.route("/experience/",methods=["POST","GET"])
def work_experience():
    if request.method=='POST':
       zhiweis=request.form.get("zhiwei")
       zw=read_data.collection.find({"pname":{'$regex': zhiweis}})
       g.zw=zw
       # print(zw)
       # cname=[]
       # pname=[]
       # workplace=[]
       # welfare=[]
       # education=[]
       # experience=[]
       # requirement=[]
       # ctype=[]
       # scale=[]
       # nature=[]
       # dlink=[]
       # for item in zw:
       #     print(item)
           # # print(item)
           # # print(item["pname"],item["scale"])
           # cname.append(item["cname"])
           # workplace.append(item["workplace"])
           # pname.append(item["pname"])
           # welfare.append(item["welfare"])
           # experience.append(item["experience"])
           # education.append(item["education"])
           # requirement.append(item["requirement"])
           # ctype.append(item["ctype"])
           # scale.append(item["scale"])
           # nature.append(item["nature"])
           # dlink.append(item["dlink"])
       # print(cname)
       # # print(zw["pname"])
       # # for zhiwei in zw:
       # #     print(zhiwei["pname"])
       # #     zhiwei1=zhiwei["pname"]
       # #     result = read_data.collection.find_one({'pname': zhiwei1})
       # g.cname=cname
       # g.workplace=workplace
       # g.pname=pname
       # g.welfare=welfare
       # g.experience= experience
       # g.education=education
       # g.requirement=requirement
       # g.ctype=ctype
       # g.scale=scale
       # g.dlink=dlink
       # g.nature=nature
       return render_template("search.html")
    else:
        g.unrestricted=read_data.unrestricted
        g.one_year=read_data.one_year
        g.three_year=read_data.three_year
        g.five_year=read_data.five_year
        return render_template("experience.html")
if __name__ == '__main__':
    app.run(debug=True)
