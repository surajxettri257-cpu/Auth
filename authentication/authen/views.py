from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def forgotpassword(request):
    return render(request, 'forgotpassword.html')

def dashboard(request):
    return render(request, 'dashboard.html')