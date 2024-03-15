from django.shortcuts import render

def index(request):
    return render(request, 'core/index.html')
def shop(request):
    return render(request, 'core/shop.html')
