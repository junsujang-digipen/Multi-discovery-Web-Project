from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
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
        webpage = requests.get("https://www.google.com/search?q={}".format(name))
        soup = BeautifulSoup(webpage.content,"html.parser")
        div = soup.find_all("div",{"id":"search"})
        a = [d.findAll("a") for d in div]
        print(div)
        print("ssssssssssssssssssssssssssssssssssssssssssssssss")
    return webpage.content

#,{"class":"BNeawe vvjwJb AP7Wnd"}
#GyAeWb , rso , search , id="res" , role="main"
if __name__ == "__main__":
    app.run()
