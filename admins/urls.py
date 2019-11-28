from django.urls import path
from. import views

urlpatterns = [
    path('', views.index, name='index'),
    path('adm', views.admin, name='adm'),
    path('admi', views.adhm, name='admi'),
    path('apt', views.appointment, name='apt'),
    path('admhome', views.home, name='admhome'),
    path('np', views.newpatient, name='np'),
    path('nt', views.newtechnician, name='nt'),
    path('rnp', views.registeredPatientdetails, name='rnp'),
    path('rnt', views.registeredTechniciandetails, name='rnt'),
    path('patreg', views.patientprocess, name='patreg'),
    path('techreg', views.technicianprocess, name='techreg'),
    path('log', views.login, name='log'),
    path('loginprocess', views.loggedin, name='loginprocess'),
    # path('patie', views.patienthome, name='patie'),
    path('adm', views.adminhome, name='adm'),
    # path('techn', views.technicianhome, name='techn'),
    path('#home', views.hom, name='homepage'),
    path('lgout', views.logout, name='lgout'),
    path('login', views.loginpage, name='login'),
    path('test', views.testin, name='test'),
    path('tech', views.techlogin, name='tech'),
    path('pat', views.patlogin, name='pat'),
    path('vr', views.patrep, name='vr'),
    # path('back', views.backup, name='back'),





















]
