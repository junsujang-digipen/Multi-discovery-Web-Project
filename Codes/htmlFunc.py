def basicHtml(head = "Title", body = "Description"):
    return """
<!doctype html>
<html>
    <head>
        {cont}
    </head>
    <body>
        {bodyCont}
    </body>
</html>
""".format(cont = head,bodyCont = body)
def selectSectionHtml():
    return """
        <div class="wrapper">
            <form action="/result/" method="get">
                <input type="checkbox" nameid="switch">
            <label for="switch" class="switch_label">
                <span class="onf_btn"></span>
            </label>
        </div>
    """
def searchBarHtml():
    return """
    <div class=SearchBar>
        <h1>Search</h1>
            <form action="/result/" method="get">
                <input size=50 type="text" name="keyword" id="keyword"/>
            </form>
    </div>
    """
def styles():
    return """
        <style>
            .searchResult{
                color:black; 
                border:3px solid black;
                background-color:009900;
                
                position: absolute;
                top: 20%;
                padding-right: 1%;
                padding-left: 1%;
            }
            .SearchBar{
                position: absolute;
                border:3px solid black;
                top: 5%;
                width:99%;
                text-align: center;
            }
            
        </style>
    """

def basicHtmlSearch(Addition):
    results = searchBarHtml() + selectSectionHtml()
    for link in Addition:
        #print(link)
        #results += "<br>"
        results += link
    
    return basicHtml(head = styles(),body = results[:])