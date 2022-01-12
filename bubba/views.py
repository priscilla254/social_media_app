
from django.shortcuts import render,redirect
from .models import *
from .forms import BubbasForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

def dashboard(request):
    if request.method=='POST':
        form=BubbasForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user=request.user
            form.save()
            return redirect('/')
    form=BubbasForm
    form_model=Bubbas.objects.all
    context={"form":form,"form_model":form_model
    }
    return render(request,"bubba/dashboard.html",context)

def profile_list(request):
    profiles=Profile.objects.exclude(user=request.user)
    context={'profiles':profiles}
    return render(request,"bubba/profile_list.html",context)

def profile(request,pk):
    profile=Profile.objects.get(pk=pk)
    if request.method=='POST':
        current_user_profile=request.user.profile
        data=request.POST
        action=data.get("follow") #name
        if action=="follow": #value
            current_user_profile.follows.add(profile)
        elif action=="unfollow": #value
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    context={'profile':profile}
    return render(request,"bubba/profile.html",context)

class SignupView(generic.CreateView):
    form_class=UserCreationForm
    success_url=reverse_lazy('dashboard')
    template_name='bubba/signup.html'

def LoginView(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Username OR Password is incorrect")
        
    context={}
    return render(request,'bubba/login.html',context)

def LogoutView(request):
    logout(request)
    messages.info(request,"you have successfully logged out.")
    return redirect('/')