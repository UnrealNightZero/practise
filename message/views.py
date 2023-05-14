from django.shortcuts import render, redirect
from .models import Message

def message_list(request):
    messages = Message.objects.all()
    return render(request, 'message_list.html', {'messages': messages})

def subit(request):
    if request.method == 'POST':
        author = request.user
        content = request.POST.get('content')
        message = Message(author=author, content=content)
        message.save()
        messages = Message.objects.all()
        return render(request, 'message_list.html',{'messages': messages})