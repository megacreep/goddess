from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.template import RequestContext
from django.core.mail import send_mail
from django.conf import settings


def index(request):
    return render(request, 'portfolio/index.html')

def about(request):
    return render(request, 'portfolio/about.html')


def projects(request):
    return render(request, 'portfolio/projects.html')


def research(request):
    return render(request, 'portfolio/research.html')


def interests(request):
    return render(request, 'portfolio/interests.html')


def cv(request):
    return render(request, 'portfolio/cv.html')


def contact(request):
    return render(request, 'portfolio/contact.html')


def demo(request):
    return render(request, 'portfolio/index_backup.html')


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
            print(user_form.error_messages)
    else:
        user_form = UserCreationForm()
    return render_to_response('portfolio/login.html', {'form': user_form}, context)


def project_ethu(request):
    return render(request, 'portfolio/project_ethu.html')


def project_learnpar(request):
    return render(request, 'portfolio/project_learnpar.html')


def project_treeme(request):
    return render(request, 'portfolio/project_treeme.html')


def project_cmf(request):
    return render(request, 'portfolio/project_cmf.html')


def project_ureveal(request):
    return render(request, 'portfolio/project_ureveal.html')


def project_climate(request):
    return render(request, 'portfolio/project_climate.html')


def project_tune(request):
    return render(request, 'portfolio/project_tune.html')



def project_dataviz(request):
    return render(request, 'portfolio/project_dataviz.html')


def project_renaissance(request):
    return render(request, 'portfolio/project_renaissance.html')


def footprint(request):
    return render(request, 'portfolio/footprint.html')


def research1(request):
    return render(request, 'portfolio/research1.html')


def research2(request):
    return render(request, 'portfolio/research2.html')


def research3(request):
    return render(request, 'portfolio/research3.html')


def research4(request):
    return render(request, 'portfolio/research4.html')




def send_email(request):
    context = RequestContext(request)

    sender = settings.EMAIL_HOST_USER
    name = request.POST.get('sender_name', '')
    email = request.POST.get('email', '')
    message = request.POST.get('message', '')

    try:
        send_mail(
            'Message from yutianxin.me',
            """\
Hi Tianxin,

 you have a message from {}, email address is {}. Following the message:

 {}
""".format(name, email, message),
            sender,
            ['limuyang08@163.com'],
            fail_silently=False
        )
    except ():
        return render(
            request,
            'portfolio/contact.html',
            {'error_message': "Sorry, we could not send your message."},
        )
    return render(request, 'portfolio/contact.html', {
        'success_message': "Your message has been sent."
    },
                  context)

