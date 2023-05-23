from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from Core.models import Post,Course,Department,Faculty

# Create your views here.

def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request,'incorrect username or password')
            return redirect('.')
    return render(request,'admin/login.html')


@login_required
def dashboard(request):
    posts = Post.objects.filter(Status=1).count()
    course = Course.objects.filter(Status=1).count()
    department = Department.objects.filter(Status=1).count()
    faculty = Faculty.objects.filter(Status=1).count()
    context = {
        'posts':posts,
        'course':course,
        'department':department,
        'faculty':faculty
    }
    return render(request,'admin/dashboard.html',context)

@login_required
def changepassword(request):
    user = request.user
    if request.method == 'POST':
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            messages.warning(request,'password does not matching')
            return redirect('/change-password/')
        else:
            user.set_password(password1)
            user.save()
            return redirect('dashboard')
    return render(request,'admin/change-password.html')

@login_required
def signout(request):
    logout(request)
    return redirect('sign-in')