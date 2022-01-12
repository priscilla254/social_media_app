from types import BuiltinMethodType
from django.shortcuts import render,redirect
from .models import *
from .forms import BubbasForm

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

