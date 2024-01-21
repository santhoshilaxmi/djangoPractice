from django.shortcuts import render
from django.http import  HttpResponse

# Create your views here.

def home(request):
    #return HttpResponse("Hello World")
# if we want to call the html pages

    return render(request, 'home.html', {'name':'Santhoshi'})

def add(request):
    val1=int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    res=val1+val2
    return render(request, 'home.html', {'result': res , 'name':'Santhoshi'})
    # return render(request, 'result.html', {'result':res})

