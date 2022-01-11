from django.shortcuts import render
from .models import Profile

def dashboard(request):

    return render(request,"bubba/dashboard.html")

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

