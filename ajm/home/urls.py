from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = "Learn Admin"
admin.site.site_title = "Learn Admin Portal"
admin.site.index_title = "Welcome to Learning Researcher Portal"

urlpatterns = [
    path("index", views.index, name='index'),
    path("home", views.home, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact')
]
