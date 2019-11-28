from django.urls import path
from. import views

urlpatterns = [
    path('', views.index, name=''),
    path('pat', views.showpatientdetails, name='pat'),
    path('test', views.addtest, name='test'),
    path('pd', views.patientdata, name='pd'),
    # path('tp', views.testprocess, name='tp'),
    path('testhem', views.hematology, name='testhem'),
    path('testdiab', views.diabetes, name='testdiab'),
    path('testuric', views.uricacid, name='testuric'),
    path('testchol', views.cholestrol, name='testchol'),
    path('pr', views.patientreport, name='pr'),
    path('rpb', views.reporthematology, name='rpb'),
    path('rpd', views.reportdiabetes, name='rpd'),
    path('rpu', views.reporturic, name='rpu'),
    path('rpc', views.reportcholestrol, name='rpc'),
    path('rph', views.reporthome, name='rph'),
    path('check', views.checkin, name='check'),
    path('checkchol', views.cholcheck, name='checkchol'),
    path('checkuric', views.uriccheck, name='checkuric'),
    path('checkdiab', views.diabcheck, name='checkdiab'),
    path('report', views.finalreport, name='report'),
    path('lgout', views.logout, name='lgout'),
    path('login', views.login, name='login'),
    path('loginprocess', views.loggedin, name='loginprocess'),
    path('hom', views.techome, name='hom'),






























]
