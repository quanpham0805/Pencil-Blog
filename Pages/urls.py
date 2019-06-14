from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('logout', views.logout_request, name='logout'),
    path('login', views.login_request, name='login'),
    path("<single_slug>", views.single_slug, name="single_slug"),
    path("<single_slug>/comment", views.add_comment, name="add_comment")
]