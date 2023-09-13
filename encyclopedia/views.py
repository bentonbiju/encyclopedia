from django.shortcuts import render

from . import util
from . import convert

def index(request):
    list=[]
    query_dict = request.GET      #Gets the get data that has been passed after searching through the searchbar
    query = query_dict.get("query")
    entries = util.list_entries()
    if query != None:                                   #Here we check if a query was given by the user as a get request. If it was given then we check whether the page exists and then render it. If it doesn't exist then we display an error message.
        for entry in entries:
            if query == entry:
                contents = util.get_entry(query)
                input_file = open(r"C:\Users\bento\django\django_app\encyclopedia\input.txt","w+")                       
                input_file.write(contents)                                                                  #Writing markdown content into input.txt
                input_file.close()
                convert.main()                                                   #Function converts markdown file into html and outputs it into an output.txt file
                return render(request,"encyclopedia/display.html") 
        for entry in entries:
            if query in entry:
                list.append(entry)
        if len(list) == 0:
            return render(request,"encyclopedia/error.html")
        else:
            return render(request,"encyclopedia/results.html",{
                "results":list
            }
            )    
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def display(request,name):
    list=[]
    query_dict = request.GET      #Gets the get data that has been passed after searching through the searchbar
    query = query_dict.get("query")
    entries = util.list_entries()
    if query != None:                                   #Here we check if a query was given by the user as a get request. If it was given then we check whether the page exists and then render it. If it doesn't exist then we display an error message.
        for entry in entries:
            if query == entry:
                contents = util.get_entry(query)
                input_file = open(r"C:\Users\bento\django\django_app\encyclopedia\input.txt","w+")                       
                input_file.write(contents)                                                                  #Writing markdown content into input.txt
                input_file.close()
                convert.main()                                                   #Function converts markdown file into html and outputs it into an output.txt file
                return render(request,"encyclopedia/display.html")   
        for entry in entries:
            if query in entry:
                list.append(entry)
        if len(list) == 0:
            return render(request,"encyclopedia/error.html")
        else:
            return render(request,"encyclopedia/results.html",{
                "results":list
            }
            )    
    

    for entry in entries:                               #If a get request wasn't made throught a url then the page on the url is rendered.
        if name == entry:
            contents = util.get_entry(name)
            input_file = open(r"C:\Users\bento\django\django_app\encyclopedia\input.txt","w+")                       
            input_file.write(contents)                                                                  #Writing markdown content into input.txt
            input_file.close()
            convert.main()                                                   #Function converts markdown file into html and outputs it into an output.txt file
            return render(request,"encyclopedia/display.html")   
    return render(request,"encyclopedia/error.html")

        

