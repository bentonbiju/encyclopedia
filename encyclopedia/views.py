from django.shortcuts import render,redirect
from . import util
from . import convert
import random
def index(request):
    print(request.POST)
    entries = util.list_entries()
    if request.method == "POST":                                    #First we check if Post data is sent through request. If this is the case, a new encyclopedia entry has been created which means that we have to add it to the encyclopedia list and then render the index page.
        check = request.POST["check"]
        if check == "1":                                            #Checks if the request has come from the add page.
            entry_title = request.POST["title"]
            entry_contents = request.POST["markdown"]
            if entry_title in entries:
                return render(request,"encyclopedia/duplicate.html")
            util.save_entry(entry_title,entry_contents)
            return redirect(display,entry_title)
        else:
            entry_title = request.POST["title"]
            entry_contents = request.POST["markdown"]
            util.save_entry(entry_title,entry_contents)
            return redirect(display,entry_title)
    list=[]
    query_dict = request.GET      #Gets the get data that has been passed after searching through the searchbar
    query = query_dict.get("query")
    
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
                return render(request,"encyclopedia/display.html",{
                    "entry_title":query
                })   
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
            return render(request,"encyclopedia/display.html",{
                "title":name,
                "entry_title":name
            })   
    return render(request,"encyclopedia/error.html")

def add(request):
    return render(request,"encyclopedia/add.html")

def edit(request):
    if request.method == "POST":   
        print(request.POST)           
        name = request.POST["name"]                 #Receives the title of the page
        print(name)
    content = util.get_entry(name)
    return render(request,"encyclopedia/edit.html",{
        "contents":content,
        "name":name
    }
    )

def random_page(request):
    entries = util.list_entries()
    ele = random.choice(entries)
    return redirect(display,ele)
