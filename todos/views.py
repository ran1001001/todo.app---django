from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Todo
# Create your views here.


def initialize_session(request):
    if "todos" not in request.session:
        request.session["todos"] = []


def index(request):
    initialize_session(request)
    user_todos = Todo.objects.filter(id__in=request.session["todos"])
    print(request.session["todos"])
    return render(request, "index.html", {
        "todos": user_todos
    })


def view_todo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    if request.GET.get("stat"):
        todo.status = True
        todo.save()
    return render(request, "view.html", {
        "todo": todo,
        "status": todo.status
    })


def add(request):
    initialize_session(request)
    if request.method == "POST":
        todo = request.POST["todo"]
        description = request.POST["description"]
        todo_object = Todo.objects.create(todo=todo, description=description,
                                          status=False)
        request.session['todos'].append(todo_object.pk)
        request.session.modified = True
        return HttpResponseRedirect(reverse("index"))
    return render(request, "add.html")


def delete(request, todo_id):
    t = Todo.objects.get(pk=todo_id)
    t.delete()
    return HttpResponseRedirect(reverse("index"))
