from django.contrib import admin
from django.contrib.auth.models import Group,User
from .models import Profile,Bubbas
admin.site.unregister(Group)
admin.site.unregister(User)

class ProfileInLine(admin.StackedInline):
    model=Profile
    
class UserAdmin(admin.ModelAdmin):
    model=User
    #to only display the username field
    fields=["username"]
    inlines=[ProfileInLine]

admin.site.register(User,UserAdmin)
admin.site.register(Bubbas)
