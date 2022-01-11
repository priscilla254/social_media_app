from django.shortcuts import render
from .models import Profile

def dashboard(request):

    return render(request,"base.html")

def profile_list(request):
    profiles=Profile.objects.exclude(user=request.user)
    context={'profiles':profiles}
    return render(request,"bubba/profile_list.html",context)

def profile(request,pk):
    profile=Profile.objects.get(pk=pk)
    context={'profile':profile}
    return render(request,"bubba/profile.html",context)