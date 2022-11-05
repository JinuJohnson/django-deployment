from django.urls import path
from ProjectApp import views

urlpatterns = [
    path('',views.home,name='name'),
    path('predict/',views.prediction,name='prediction'),
]
