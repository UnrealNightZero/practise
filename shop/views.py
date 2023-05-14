from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

def shop(request):
    if request.method == "GET":
        return render(request,"shop.html")