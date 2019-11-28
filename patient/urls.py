from django.urls import path
from. import views

urlpatterns = [
    path('', views.index, name=''),
    path('vr', views.viewingreport, name='vr'),
    path('checkin', views.checkhem, name='checkin'),
    path('done', views.submit, name='done'),
    path('dw', views.download, name='dw'),
    path('dwn', views.repdownload, name='dwn'),
    path('do', views.back, name='do'),
    path('lgout', views.logout, name='lgout'),
    path('login', views.login, name='login'),
    path('loginprocess', views.loggedin, name='loginprocess'),
    path('book', views.message, name='book'),











]