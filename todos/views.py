from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Todo
# Create your views here.


def index(request):
    return render(request, "index.html", {
        "todos": Todo.objects.all()
    })


def view_todo(request, todo_id):
    return render(request, "view.html", {
        "todo": Todo.objects.get(pk=todo_id)
    })


def add(request):
    if request.method == "POST":
        todo = request.POST["todo"]
        description = request.POST["description"]
        status = request.POST.get("status", False)
        t = Todo(todo=todo, description=description, status=status)
        t.save()
        return HttpResponseRedirect(reverse("index"))
    return render(request, "add.html")


def delete(request, todo_id):
    t = Todo.objects.get(pk=todo_id)
    t.delete()
    return HttpResponseRedirect(reverse("index"))
