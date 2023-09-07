import re


def convert_line_headers(line):
    pat1=re.compile('###')
    pat2=re.compile('##')
    pat3=re.compile('#')
    line1 = line
    if((pat1.match(line)) != None ):
        line1 = re.sub(pat1,"<h3>",line,1)
        count = 3
    elif((pat2.match(line)) != None):
        line1 = re.sub(pat2,"<h2>",line,1)
        count = 2
    elif((pat3.match(line)) != None):
        line1 = re.sub(pat3,"<h1>",line,1)
        count = 1
    
    if(line1 != line):
        endtag = "</h"+str(count)+">"
        line1 = line1.replace("\n",endtag)
        line1 = line1+"\n"
    return line1
    


# Check to replace only first occurence
def convert_line_bold(line):
    line1 = line
    line = line.replace("**","<b>",1)
    while True:
        if line != line1:
            line= line.replace("**","</b>",1)
            line1 = line
        line = line.replace("**","<b>",1)
        if line1 == line:
            break
    return line

# Check to include all three symbols at once
def convert_line_list(line):
    pat = re.compile("\*|-|\+")
    if(pat.match(line) != None):
        line = pat.sub("<li>",line,1)
        line = line.replace("\n","</li>")
        line = line+"\n"
    return line

# Check to include all three symbols at once
def convert_line_link(line):
    pat = re.compile("\[(.*?)\]\((.*?)\)")
    mat = re.search(pat,line)
    if mat:
        content = mat.group(1)
        link = mat.group(2)
        replacement = '<a href="'+link+'">'+content+'</a>'
        line = re.sub(pat,replacement,line)
    return line

    
# Check to include all three symbols at once
def convert_line_paragraph(line):
    pat = re.compile("\n")
    if pat.match(line):
        line = line.replace("\n","<p>")
    return line



def main():
    input_file = open(r"C:\Users\bento\django\django_app\encyclopedia\input.txt","r")    
    out = open(r"C:\Users\bento\django\django_app\encyclopedia\templates\encyclopedia\converted.html","w")
    lines=input_file.readlines()
    l = []
    num = 0
    for x,line in enumerate(lines):
        line=convert_line_headers(line)
        line=convert_line_bold(line)
        line1 = line
        line=convert_line_list(line)
        if line1 != line:                               #Checking whether the line was changed after the convert_line_list function. If this happened then we need to process all the list items before moving to the next function.
            line = "<ul>"+line
            for altline in range(x+1,len(lines)):            #Here we use another for loop to loop through all the list items.
                line1 = lines[altline]
                lines[altline] = convert_line_list(lines[altline])
                if(line1 == lines[altline]):
                    lines[altline] = lines[altline] + "</ul>"
                    break
        
        line =convert_line_link(line)
        line1 = line
        line = convert_line_paragraph(line)
        if(line1 != line):
            for s,altline in enumerate(range(x+1,len(lines))):
                pat = re.compile("\n")
                if pat.match(lines[altline]):
                    lines[altline] = lines[altline].replace("\n","</p>")
                    break
                
                if  altline == len(lines)-1:
                    lines[altline] = lines[altline]+"</p>"
        l.append(line) 
        num +=1
        
        print(line)
    out.writelines(l)    
    out.close()
    input_file.close()
