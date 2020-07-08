from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.



def signIn(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            
            auth.login(request,user)
            messages.success(request,"Welcome "+username+" ")
            return render(request,"index.html")
        else:
            messages.warning(request,"Invalid Credential")
            return render(request,"signIn.html")
            
    else:
        return render(request,"signIn.html")
        

def signUp(request):
    if request.method =="POST":
        print(request.POST)
        first_name = request.POST['firstname']
        last_name =  request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.warning(request,"Username Already Taken")
                return render(request,"signUp.html")
            
            elif User.objects.filter(email=email).exists():
                messages.warning(request,"Email Already Taken")
                return render(request,"signUp.html")
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                print(user)
                messages.success(request,"User Created")
                return render(request,"signIn.html")
        else:
            messages.warning(request,"Password Not Match")
    return render(request,"signUp.html")
        
        
        