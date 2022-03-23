from django.urls.conf import include
from django.urls import path
from . import views

urlpatterns = [
    path('',views.fb),
    path('main',views.main),
    path('jquery',views.jquery),
    path('form',views.form),
    path('fb',views.fb),
    path('update/<int:id>',views.update)
]
