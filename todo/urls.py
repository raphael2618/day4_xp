from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_view),
    path('form/', views.form_views)

]
