from webbrowser import get
from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
import htmlFunc
app = Flask(__name__)

@app.route("/",  methods=['GET', 'POST'])
def index(): 
    if request.method == 'GET':
        name = request.args.get("keyword")
        #print(request.form)
        
    return render_template('index.html', name = name)

@app.route('/result/')
def search():
    print("ssssssssssssssssssssssssssssssssssssssssssssssss")
    if request.method == 'GET':
        name = request.args.get("keyword")
        GoogleWebpage = requests.get("https://www.google.com/search?q={}".format(name))
        soup = BeautifulSoup(GoogleWebpage.text,"html.parser")
        div = soup.find("div",id = "main")
        a = [d.find("a") for d in div]

        GoogleHrefs = []
        GoogleSearchRes = []
        for t in a:
            # print(t)
            # print("\n")
            if t == None:
                continue
            if t.get("href")[:4] == "/url":
                temp = str(t).replace("/url?q=","")
                first = temp.find("&")
                second = temp.find(">")
                temp = temp.replace(temp[first:second],'"')
                GoogleHrefs.append(t.get("href"))
                GoogleSearchRes.append(temp)
        # print("G  hrefs")
        # print(GoogleHrefs)
        # print("G searchRes")
        # print(GoogleSearchRes)

        NaverWebpage = requests.get("https://search.naver.com/search.naver?query={}".format(name))
        soup = BeautifulSoup(NaverWebpage.text,"html.parser")
        div = soup.find("div",id = "main_pack")
        a = div.select("a")
        NaverHrefs = []
        NaverSearchRes = []
        for t in a:
            if t == None or t == -1 or t.get("href") == None:
                continue
            if str(t).find(name) == -1:
                continue
            if t.get("href")[:4] == "http":
                NaverHrefs.append(t.get("href"))
                NaverSearchRes.append(str(t))
        # print("N  hrefs")
        # print(NaverHrefs)
        # print("N searchRes")
        #print(NaverSearchRes)
        
        print("ssssssssssssssssssssssssssssssssssssssssssssssss")
        Res = []
        Res.append("<div style=\"position:absolute;left:0%; height:100%;width:40%;color:white;border:1px solid;background-color:009900;margin:2%;\">")
        for r in GoogleSearchRes:
            Res.append(r)
        Res.append("</div>")
        Res.append("<div style=\" position:absolute;left:50%;top:0%;height:100%;width:40%;color:white;border:1px solid;background-color:009900;margin:2%; \">")
        for r in NaverSearchRes:
            Res.append(r)
        Res.append("</div>")

    return htmlFunc.basicHtmlSearch(Res)

#,{"class":"BNeawe vvjwJb AP7Wnd"}
#GyAeWb , rso , search , id="res" , role="main"
#https://www.google.com/search?q=%EA%B3%84%EB%AA%85%EB%8C%80%ED%95%99%EA%B5%90&start=60
if __name__ == "__main__":
    app.run()
