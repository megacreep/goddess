from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.template import RequestContext


def index(request):
    return render(request, 'portfolio/index.html')

def signup(request):
    context = RequestContext(request)
    if request.method == 'POST':
        user_form = UserCreationForm(data=request.POST)
        if user_form.is_valid():
            user_form.save()
            user = authenticate(username=user_form.cleaned_data.get('username'),
                                password=user_form.cleaned_data.get('password1'))
            user.email = request.POST['email']
            user.save()
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            print user_form.error_messages
    else:
        user_form = UserCreationForm()
    return render_to_response('registration/login.html', {'form': user_form}, context)


