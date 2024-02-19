from typing import Self
from django.shortcuts import render

from Dashboard.models import Login, UserInfo

# Create your views here.


def login(request):
    if request.method == "POST":
        usrname = request.POST.get("usrname", "")
        passd = request.POST.get("password", '')
        try:
            user = Login.objects.get(usrname=usrname)
            if user.password == passd:
                usrinfo=UserInfo.objects.all()
                return render(request,'dashboard/userInfo.html',{'usrinfo':usrinfo})
            else:
                return render(request,'dashboard/login.html') 
        except Login.DoesNotExist:
            return render(request,'dashboard/login.html') 
        
    else:
        return render(request,'dashboard/login.html') 
