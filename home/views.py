from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth import authenticate,login

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.html')
    # return HttpResponse('Hey this is me')

def loginUser(request):
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            return render(request,'login.html')
        
    return render(request,'login.html')




def logoutuser(request):
    logoutuser(request)
    return redirect("/login")
