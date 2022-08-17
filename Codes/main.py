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
        
    return htmlFunc.basicHtmlSearch(siteLists = ['Google'])

@app.route('/result/')
def search():
    print("ssssssssssssssssssssssssssssssssssssssssssssssss")
    if request.method == 'GET':
        name = request.args.get("keyword")
        CheckedSiteLists = request.args.getlist("selected")
        CheckedSiteListsNum = len(CheckedSiteLists)
        width = 0
        left = 9
        leftInterval = 0
        margin = 4
        if CheckedSiteListsNum == 1:
            width = 80
        elif CheckedSiteListsNum == 2:
            width = 39
            leftInterval = width + margin
        elif CheckedSiteListsNum == 3 or CheckedSiteListsNum == 4:
            width = 25
            leftInterval = width + margin

        print(CheckedSiteLists)
        if name !="":
            Res = []

            if 'Google' in CheckedSiteLists:
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
                Res.append("<div class = searchResult  style=\"width:{}%;left:{}%;\">".format(width,left))
                left += leftInterval
                Res.append("<h2 text-align=center style=\"color:black;\">Google search results</h2>")
                for r in GoogleSearchRes:
                    Res.append(r)
                Res.append("</div>")

            if 'Naver' in CheckedSiteLists:
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
                        if str(t).find("svg") == -1: 
                            NaverHrefs.append(t.get("href"))
                            NaverSearchRes.append(str(t))
                Res.append("<div class = searchResult style=\"width:{}%; left:{}%;\">".format(width,left))
                left += leftInterval
                Res.append("<h2 text-align=center style=\"color:black;\">Naver search results</h2>")

                for r in NaverSearchRes:
                    Res.append(r)
                Res.append("</div>")

            if 'YaHoo' in CheckedSiteLists:
                Webpage = requests.get("https://search.yahoo.com/search?p={}".format(name))
                soup = BeautifulSoup(Webpage.text,"html.parser")
                div = soup.find("div",id = "main")
                a = div.select("a")
                Hrefs = []
                SearchRes = []
                for t in a:
                    if t == None or t == -1 or t.get("href") == None:
                        continue
                    if str(t).find(name) == -1:
                        continue
                    if t.get("href")[:4] == "http":
                        #if str(t).find("svg") == -1: 
                        Hrefs.append(t.get("href"))
                        SearchRes.append(str(t))
                Res.append("<div class = searchResult style=\"width:{}%; left:{}%;\">".format(width,left))
                left += leftInterval
                Res.append("<h2 text-align=center style=\"color:black;\">YaHoo search results</h2>")

                for r in SearchRes:
                    Res.append(r)
                Res.append("</div>")

            if 'YouTube' in CheckedSiteLists:
                Webpage = requests.get("https://www.youtube.com/results?search_query={}".format(name))
                soup = BeautifulSoup(Webpage.text,"html.parser")
                a = soup.findAll("a",id="video-title")
                
                #print(div)
                #return Webpage.text
                #a = div.select("a")
                Hrefs = []
                SearchRes = []
                for t in a:
                    if t == None or t == -1 or t.get("href") == None:
                        continue
                    if str(t).find(name) == -1:
                        continue
                    if t.get("href")[:4] == "/wat":
                        #if str(t).find("svg") == -1: 
                        Hrefs.append(t.get("href"))
                        SearchRes.append(str(t))
                Res.append("<div class = searchResult style=\"width:{}%; left:{}%;\">".format(width,left))
                left += leftInterval
                Res.append("<h2 text-align=center style=\"color:black;\">YouTube search results</h2>")

                for r in SearchRes:
                    Res.append(r)
                Res.append("</div>")
            print("ssssssssssssssssssssssssssssssssssssssssssssssss")
            
            return htmlFunc.basicHtmlSearch(Addition = Res,siteLists = CheckedSiteLists,searchVal=name)
        return htmlFunc.basicHtmlSearch(siteLists = CheckedSiteLists)
    return htmlFunc.basicHtmlSearch()

#,{"class":"BNeawe vvjwJb AP7Wnd"}
#GyAeWb , rso , search , id="res" , role="main"
#https://www.google.com/search?q=%EA%B3%84%EB%AA%85%EB%8C%80%ED%95%99%EA%B5%90&start=60
#<style>body{border:1px solid black;}</style>
#display:inline;
# and str(t).find("thumb_area") == -1
if __name__ == "__main__":
    app.run()
