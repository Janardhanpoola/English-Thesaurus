from django.shortcuts import render
########hello
##########welcome

def home(request):
    
    return render(request,"home.html")