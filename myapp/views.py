from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
from django.contrib.auth.models import User
from .models import *

# Create your views here.
def about(request):
    return render(request,'about.html')

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *


# helper to require login via session

def _require_login(request):
    return request.session.get('member_id')


# Create your views here.
def about(request):
    return render(request,'about.html')


def login(request):
    # simple login using Member model and session
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            member = Member.objects.get(email=email, password=password)
            request.session['member_id'] = member.id
            messages.success(request, 'Successfully logged in.')
            return redirect('dashboard')
        except Member.DoesNotExist:
            messages.error(request, 'Invalid credentials')
    return render(request,'login.html')


def logout(request):
    request.session.flush()
    messages.info(request, 'Logged out.')
    return redirect('login')


def register(request):
    # registration form handler
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # basic validation
        if Member.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered')
        else:
            member = Member.objects.create(
                name=name,
                email=email,
                password=password,
                gender=request.POST.get('gender',''),
                age=request.POST.get('age',0) or 0,
                city=request.POST.get('city',''),
                state=request.POST.get('state',''),
                country=request.POST.get('country',''),
                interests=request.POST.get('interests','')
            )
            request.session['member_id'] = member.id
            messages.success(request, 'Registration successful.')
            return redirect('dashboard')
    return render(request,'register.html')


def dashboard(request):
    if not _require_login(request):
        return redirect('login')
    member = Member.objects.get(id=request.session['member_id'])
    return render(request,'dashboard.html', {'member': member})


def browse(request):
    if not _require_login(request):
        return redirect('login')
    return render(request,'browse.html')


def view_messages(request):
    # view for message list/chat
    if not _require_login(request):
        return redirect('login')
    return render(request,'messages.html')


def call(request):
    if not _require_login(request):
        return redirect('login')
    return render(request,'call.html')