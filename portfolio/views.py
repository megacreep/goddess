from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request, 'portfolio/index.html')

def signup(request):
    return HttpResponse("Hello world")
