from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("edit/add_entry",views.add, name = "add"),
    path("edit/edit_entry",views.edit,name="edit"),
    path("display/random",views.random_page,name="random"),
    path("<str:name>",views.display,name="display")
]
