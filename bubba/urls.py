from django.urls import path
from django.urls import path
from .views import LoginView,LogoutView, dashboard,profile_list,profile, SignupView

urlpatterns=[
    path("",dashboard,name="dashboard"),
    path("profile_list/",profile_list,name="profile_list"),
    path("profile/<int:pk>",profile,name="profile"),
    path("signup/",SignupView.as_view(),name="signup"),
    path("login/",LoginView,name="login"),
    path('logout/',LogoutView,name="logout")
    ]