from django.shortcuts import render

# Create your views here.

def command(request):
    return render(request, 'command/overview.html')
