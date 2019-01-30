from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'main_site\home.html')

def about(request):
    return render(request, 'main_site\about.html')