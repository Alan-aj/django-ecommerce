from django.urls.conf import include
from django.urls import path
from . import views

urlpatterns = [
    path('',views.fb),
    path('main',views.main),
    path('jquery',views.jquery),
    path('form',views.form),
    path('fb',views.fb),
    path('update/<int:id>',views.update),
    path('log',views.login,name="log_user"),
    path('home',views.home,name="home"),
    path('logout',views.logout,name="logout_user"),
    path('profile',views.profile,name="profile"),
    path('chpwd',views.chpwd,name="chpwd")
]
