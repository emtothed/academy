from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("schedule", views.schedule, name="schedule"),
    path("scheduleget", views.scheduleget, name="scheduleget"),
    path("exam/<str:title>", views.exam, name="exam"),
    path("questsget/<str:title>", views.questsget, name="questsget"),
    path("scores", views.scores, name="scores"),



    
]
