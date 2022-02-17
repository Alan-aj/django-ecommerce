from django.urls.conf import include
from django.urls import path
from . import views

urlpatterns = [
    path('home',views.index),
    path('main',views.main),

]
