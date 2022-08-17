from pickle import TRUE


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

def selectSectionHtml(siteCheckLists = []):
    selectBars = """ 
    <div class=\"siteSelectBar\" style=\"position:fixed;top:{pos}%;\">
    <label> 
    {label} 
    </label> 
    </div> 
    """
    #{ischecked}
    inputBox = """
    <input type=\"checkbox\" name=\"selected\" value= \"{value}\" {ischecked}> 
    {value}
    """
    
    sites = ['Google','Naver','YaHoo','YouTube']
    returnValues = ""
    positionVal = 20
    
    for s in sites:
        checked = ""

        if siteCheckLists.count(s) != 0:
            checked = "checked"   

        returnValues += selectBars.format(pos=positionVal,label = 
        inputBox.format(value=s, ischecked = checked))
        positionVal += 10

    # returnValues += selectBars.format(pos=20,label = inputBox.format(value="Google"))
    # returnValues += selectBars.format(pos=30,label = inputBox.format(value="Naver"))
    # returnValues+= selectBars.format(pos=40,label = inputBox.format(value="YaHoo"))
    # returnValues+= selectBars.format(pos=50,label = inputBox.format(value="YouTube"))

    returnValues+= selectBars.format(pos=60,label = "<input type=\"submit\">")

    return returnValues
def searchBarHtml( val):
    return """
    <div class=SearchBar>
        <h1>Search</h1>
                <input size=50 type="text" name="keyword" value = "{}" id="keyword"/>
    </div>
    """.format(val)
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
                position: fixed;
                border:3px solid black;
                top: 5%;
                width:99%;
                text-align: center;
            }
            .siteSelectBar{
                position: fixed;
                border:3px solid black;
                left: 2%;

            }
            
        </style>
    """
def siteSearchInputs(siteLists, searchVal):
    results = "<form action='/result/' method='get'>" + searchBarHtml(searchVal) + selectSectionHtml(siteLists) + "</form>"
    return results

def basicHtmlSearch(Addition = [], siteLists=[], searchVal = ""):
    results = siteSearchInputs(siteLists,searchVal)
    for link in Addition:
        #print(link)
        #results += "<br>"
        results += link
    
    return basicHtml(head = styles(),body = results[:])