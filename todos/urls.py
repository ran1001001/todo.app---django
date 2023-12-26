from django.urls import path

from . import views

urlpatterns = [
        path('', views.index, name="index"),
        path('view/<int:todo_id>', views.view_todo, name="view_todo"),
        path('add/', views.add, name="add"),
        path('delete/<int:todo_id>', views.delete, name="delete"),
    ]
