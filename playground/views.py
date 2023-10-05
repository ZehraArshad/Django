from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# a view func takes req and return response also called action
def say_hello(request):
    #return HttpResponse('Hello, this is Zehra!')
    x=20
    y=30
    return render(request, 'hello.html', {'name':'Zehra Arshad'})
