from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Comment
from .models import User
from .forms import CommentForm


def index(request):
    name = Comment.objects.order_by('-date')
    context = {'nombres': name}
    return render(request, 'polls/index.html', context)


def pollsHome(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            new_usuario = User(email=request.POST['email'], password=request.POST['password'])
            new_usuario.save()
            return redirect('index')

    form = CommentForm()
    context = {'form': form}
    return render(request, 'polls/home.html', context)


def home(request):
    return HttpResponse("Entrando al index de la wea re ctm!!!")
