from django.shortcuts import render

def home(request):
    context = {}
    return render(request, 'bend/home.html', context)

def about(request):
    pass

def contact(request):
    pass

