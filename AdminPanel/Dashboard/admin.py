from django.contrib import admin

from Dashboard.models import Login, UserInfo

# Register your models here.
admin.site.register(UserInfo)
admin.site.register(Login)
