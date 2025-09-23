from django.urls import path
from . import views

urlpatterns = [
    path('',views.home ,name='movies-home'),
    path('about/',views.about ,name='movies-about'),
]


