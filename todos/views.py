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
    s = request.GET.get("stat", False)
    if s is True:
        status = True
    else:
        status = s
    return render(request, "view.html", {
        "todo": Todo.objects.get(pk=todo_id),
        "status": status
    })


def add(request):
    if request.method == "POST":
        todo = request.POST["todo"]
        description = request.POST["description"]
        Todo(todo=todo, description=description, status=False).save()
        return HttpResponseRedirect(reverse("index"))
    return render(request, "add.html")


def delete(request, todo_id):
    t = Todo.objects.get(pk=todo_id)
    t.delete()
    return HttpResponseRedirect(reverse("index"))
