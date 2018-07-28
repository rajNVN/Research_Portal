from django.urls import path

from scholars import views

urlpatterns = [
    path("counsel/", views.counsel),
    path("home/", views.home),
    path("paper/", views.paper),
    path("student/", views.student),
    path("login/", views.login),
    path("admit/", views.admissions),
    path("results/", views.results),
    path('final/', views.finalize),
    path('register/', views.register),
    path('addPaper/', views.add_paper),
    path('assignStudent/', views.assign_student)
]
