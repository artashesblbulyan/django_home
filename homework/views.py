from django.shortcuts import render, HttpResponse
# from models import Homework
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from homework.forms import TaskForm
from homework.models import Homework


def homework(request):
    user = TaskForm()
    if request.method == "POST":
        user = TaskForm(request.POST)
        if user.is_valid():
            Homework.objects.create(**user.cleaned_data)
    context = {'user': user}
    return render(request, 'homework/index.html', context)
