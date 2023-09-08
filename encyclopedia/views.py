from django.shortcuts import render

from . import util
from . import convert

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def display(request,name):
    entries = util.list_entries()
    for entry in entries:
        if name == entry:
            contents = util.get_entry(name)
            input_file = open(r"C:\Users\bento\django\django_app\encyclopedia\input.txt","w+")                       
            input_file.write(contents)                                                                  #Writing markdown content into input.txt
            input_file.close()
            convert.main()                                                   #Function converts markdown file into html and outputs it into an output.txt file
            return render(request,"encyclopedia/display.html")
    
    return render(request,"encyclopedia/error.html")