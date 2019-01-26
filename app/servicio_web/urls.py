from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('listaCantones/',views.listaCantones.as_view()),
]
