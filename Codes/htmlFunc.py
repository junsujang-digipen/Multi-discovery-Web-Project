def basicHtml(head = "Title", body = "Description"):
    return """
<!doctype html>
<html>
    <head>
        {}
    </head>
    <body>
        {}
    </body>
</html>
""".format(head,body)

def searchBarHtml():
    return """
    <h2>Search</h2>
        <form action="/result/" method="get">
            <input type="text" name="keyword" id="keyword"/>
        </form>
    """

def basicHtmlSearch(Addition):
    results = searchBarHtml()
    for link in Addition:
        #print(link)
        #results += "<br>"
        results += link
        

    return basicHtml(head = "",body = results[:])