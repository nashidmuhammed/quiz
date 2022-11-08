from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import CreateUserForm
from .models import *

# Create your views here.


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                return redirect('add_qst')
            return redirect('index')
        else:
            messages.info(request, 'Username or Password is incorrect')
    context = {}
    return render(request, 'login.html', context)


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        print('post')
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            first = request.POST['first']
            phone = request.POST['phone']
            last = request.POST['second']
            user.first_name = first
            user.last_name = last
            user.save()
            Client.objects.create(user=user, phone=phone)
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    context = {'form': form}
    return render(request, 'register.html', context)


def add_qst(request):
    if request.user.is_superuser:
        n = Questions.objects.all().count()
        if request.method == 'POST':
            Questions.objects.create(
                qst=request.POST['qst'],
                no=n+1,
                a=request.POST['a'],
                b=request.POST['b'],
                c=request.POST['c'],
                d=request.POST['d'],
                ans=request.POST['ans'],
                time=request.POST['time']
            )
            messages.info(request, 'Question added successfully')
        return render(request, 'add_qst.html', {'count': n})
    else:
        return redirect('login')


def index(request):
    if request.user.is_authenticated:
        count = Questions.objects.all().count()
        user = Client.objects.get(user=request.user)
        no = user.no
        if count < no:
            score = user.score
            return render(request, 'score.html', {'count': count, 'score': score})
        qst = Questions.objects.get(no=no)
        if request.GET.get('data') is not None:
            data = request.GET.get('data')
            print('ans =',qst.ans.lower())
            if qst.ans.lower() == data:
                print('COREECT')
                user.score += 1
                user.no += 1
                user.save()
                return redirect('index')
            else:
                print('In COREECT')
                user.no += 1
                user.save()
                return redirect('index')
        if request.method == 'POST':
            print('Time is up')
            user.no += 1
            user.save()
            return redirect('index')
        context = {'count': count, 'qst': qst}
        return render(request, 'index.html', context)
    else:
        return redirect('login')


def logoutUser(request):
    logout(request)
    return redirect('login')


def send_email(request):
    count = Questions.objects.all().count()
    user = Client.objects.get(user=request.user)
    subject = 'Grammar Score'
    message = 'Your Grammar Score is ' + str(user.score) + ' out of ' + str(count) + '\nThankyou!'
    recipient = str(user.user.email)
    print('msg =', message)
    send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
    messages.success(request, 'Score sended successfully to your email')
    return redirect('index')