from django.urls import path
from . import views

urlpatterns = [
    path('get/',views.fundList),
    path('add/',views.fundCreate),
]