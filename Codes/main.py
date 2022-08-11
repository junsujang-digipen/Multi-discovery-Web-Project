from flask import Flask, render_template, request
 
app = Flask(__name__)

@app.route("/",  methods=['GET', 'POST'])
def index(): 
    if request.method == 'GET':
        name = request.args.get("keyword")
        print(request.form)
        
    return render_template('index.html', name = name)

@app.route('/result/')
def search():
    if request.method == 'GET':
        name = request.args.get("keyword")
    return name

if __name__ == "__main__":
    app.run()
