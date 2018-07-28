from django.urls import path, include

from guides import views

urlpatterns = [
    path('login/', views.login),
    path('home/', views.home),
    path('scholar/', views.scholar),
    path('student/', views.student),
    path('logout/', views.logout),
]
