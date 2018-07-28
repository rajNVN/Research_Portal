from django.urls import path

from students import views

urlpatterns = [
    path('register/', views.register),
    path('add/', views.add),
    path('rate/', views.rate)
]