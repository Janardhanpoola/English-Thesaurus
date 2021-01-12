from django.shortcuts import render

import json

from difflib import get_close_matches
# Create your views here.

def word(request):
    word=request.POST['word']

    f=open(r"C:\Users\jpoola\3D Objects\py_real_world_app\APP1\data.json")

    data=json.load(f)
    
    #word=request.POST.get('word',get_close_matches(word,data.keys())[0])
    word=word.lower()
    
    if word in data:
        return render(request,"meaning.html",{'data':data[word],'word':word})

    
    elif word.title() in data:    
        return render(request,"meaning.html",{"data":data[word.title()],'word':word})

    elif word.upper() in data:
        return render(request,"meaning.html",{'data':data[word.upper()],'word':word})    
    
    elif len(get_close_matches(word,data.keys())) >0:
    
        
        s=True
        word=get_close_matches(word,data.keys())[0]

        return render(request,"home.html",{'s':False,'data':data[get_close_matches(word,data.keys())[0]],'word':word})

    else:
        e=True
        return render(request,"home.html",{'e':False})
                     
            

    return render(request,"meaning.html",{'data':data})


