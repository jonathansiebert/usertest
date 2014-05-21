from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from usertest.forms import UserForm
from usertest.forms import LoginForm
from usertest.forms import UpdateForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.template import RequestContext

@csrf_protect
def index(request):
    return render_to_response('usertest/index.html',
                               None,
                               context_instance=RequestContext(request))

@csrf_protect
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user != None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
                else:
                    return HttpResponse('Account disabled.')
            else:
                return HttpResponse('Invalid username/password.')
    else:
        form = LoginForm()

    return render_to_response('usertest/login.html',
                               { 'form': form },
                               context_instance=RequestContext(request))

@csrf_protect
def logout_view(request):
    logout(request)
    return redirect('/')
 
@csrf_protect
def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                form.cleaned_data.get('username'),
                form.cleaned_data.get('email'),
                form.cleaned_data.get('password')
            )
            user.first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            if last_name != None:
                user.last_name = last_name
            user.save()
            return redirect('login')
    else:
        form = UserForm()

    return render_to_response('usertest/register.html',
                               { 'form': form },
                               context_instance=RequestContext(request))


@csrf_protect
def update_view(request):
    if request.method == 'POST':
        form = UpdateForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email');
            email = email.strip('()\'.')
            request.user.email = email
            request.user.first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            if last_name != None:
                request.user.last_name = last_name
            request.user.save()
            return redirect('/')
    else:
        form = UpdateForm()

    return render_to_response('usertest/update.html',
                               { 'form': form },
                               context_instance=RequestContext(request))
