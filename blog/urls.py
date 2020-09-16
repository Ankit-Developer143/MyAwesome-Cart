from django.urls import path
from . import views


#forward to views => index
urlpatterns = [
    path("", views.index, name ="blogHome"),
]