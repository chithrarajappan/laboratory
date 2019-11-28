from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from admins.models import PatientRegistartion, TechnicianRegistration, Logins
from django.template import loader
from django.core.mail import send_mail
from django.conf import settings
# from django.core.mail import EmailMessage
from patient.models import Appointment


# Create your views here.
def index(request):
    # return HttpResponse('ok')
    return render(request, 'adminstemp/index.html')

def hom(request):
    return render(request, 'adminstemp/index.html')

def appointment(request):
    patient = Appointment.objects.all()
    context = {'patient': patient}
    return render(request, 'adminstemp/appointment.html', context)


def admin(request):
    return render(request, 'logins/login.html')

def home(request):
    return render(request, 'adminstemp/index.html')

def adhm(request):
    return render(request, 'adminstemp/adminhome.html')

def newpatient(request):
    return render(request, 'patienttemp/patientreg.html')

def newtechnician(request):
    return render(request, 'techtemp/techreg.html')

def registeredPatientdetails(request):
    patient = PatientRegistartion.objects.all()
    context = {'patient': patient}
    return render(request, 'adminstemp/registeredpatient.html', context)


def registeredTechniciandetails(request):
    tech = TechnicianRegistration.objects.all()
    context = {'tech': tech}
    return render(request, 'adminstemp/registeredtechnician.html', context)

def patientprocess(request):
    log1 = Logins()
    loguname = request.POST.get("uname")
    paswd = request.POST.get("password")
    mail = request.POST.get("email")
    ctgry = request.POST.get("category")

    log1.Username = loguname
    log1.Password = paswd
    log1.Email = mail
    log1.Category = ctgry
    log1.save()

    pr = PatientRegistartion()
    patname = request.POST.get("pname")
    username = request.POST.get("uname")
    pswd = request.POST.get("password")
    ag = request.POST.get("age")
    addr = request.POST.get("address")
    mob = request.POST.get("mobile")
    gnd = request.POST.get("gender")
    birth = request.POST.get("birth_date")
    blood = request.POST.get("BloodGroup")
    hist = request.POST.get("history")
    eml = request.POST.get("email")

    pr.Patient_Name = patname
    pr.Username = username
    pr.Password = pswd
    pr.Gender = gnd
    pr.Age = ag
    pr.DateofBirth = birth
    pr.BloodGroup = blood
    pr.Mobile = mob
    pr.Email = eml
    pr.ResidencyAddress = addr
    pr.MedicalHistory = hist
    pr.save()
    subject = "Accept Lab portal login"
    msg = "Request has been accepted.please go to this  http://127.0.0.1:8000/  for login our website"
    to = mail
    res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
    return HttpResponse("<script>alert('Inserted successfully');window.location='./';</script>")


# def backup(request):
#     return HttpResponse("<script>window.location='../';</script>")


def technicianprocess(request):
    log2 = Logins()
    tuser = request.POST.get("uname")
    tpaswd = request.POST.get("password")
    tmail = request.POST.get("email")
    tcategory = request.POST.get("category")

    log2.Username = tuser
    log2.Password = tpaswd
    log2.Category = tcategory
    log2.Email = tmail
    log2.save()

    tr = TechnicianRegistration()
    techname = request.POST.get("tname")
    techuname = request.POST.get("uname")
    techpswd = request.POST.get("password")
    techaddr = request.POST.get("address")
    techmobile = request.POST.get("mobile")
    techgnd = request.POST.get("gender")
    techage = request.POST.get("age")
    techbirth = request.POST.get("birth_date")
    techblood = request.POST.get("BloodGroup")
    techmail = request.POST.get("email")

    tr.Technician_Name = techname
    tr.Username = techuname
    tr.Password = techpswd
    tr.DateofBirth = techbirth
    tr.Age = techage
    tr.BloodGroup = techblood
    tr.Gender = techgnd
    tr.Address = techaddr
    tr.Mobile = techmobile
    tr.Email = techmail

    tr.save()
    return HttpResponse("<script>alert('Inserted successfully');window.location='./';</script>")

def login(request):
    return render(request, 'logins/login.html')

def loggedin(request):
    if request.method == 'POST':
        email1 = request.POST.get("email")
        password = request.POST.get("password")
        if (Logins.objects.filter(Email=email1, Password=password).exists()):
            logins = Logins.objects.filter(Email=email1, Password=password)
            for login in logins:
                usertype = login.Category
                request.session["usertype"] = usertype

                if usertype == "patient":
                    request.session["email"] = login.Email
                    request.session["password"] = login.Password
                    request.session["usertype"] = login.Category
                    request.session["userid"] = login.pk
                    return HttpResponse("<script>window.location='../patient';</script>")

                elif usertype == 'admin':
                    request.session["email"] = login.Email
                    request.session["password"] = login.Password
                    request.session["usertype"] = login.Category
                    request.session["userid"] = login.pk
                    return HttpResponse("<script>window.location='./admi';</script>")

                elif usertype == 'technician':
                    request.session["email"] = login.Email
                    request.session["password"] = login.Password
                    request.session["usertype"] = login.Category
                    request.session["userid"] = login.pk
                    return HttpResponse("<script>window.location='../technician';</script>")


                else:
                    template = loader.get_template("logins/login.html")
                    context = {"error": "Incorrect username or password"}
                    return HttpResponse(template.render(context, request))
            else:
                template = loader.get_template("logins/login.html")
                context = {"error": "Incorrect Information"}
                return HttpResponse(template.render(context, request))
        else:
            template = loader.get_template("logins/login.html")
            context = {}
            return HttpResponse(template.render(context, request))

# def patienthome(request):
#     return render(request, 'patienttemp/index.html')

def adminhome(request):
    return render(request, 'adminstemp/index.html')

# def technicianhome(request):
#     return render(request, 'techtemp/home.html')

def testin(request):
    return HttpResponse("<script>window.location='../technician/test';</script>")

def logout(request):
    try:
        del request.session['email']
    except:
        pass
    return HttpResponse("<script>alert('you are successfully logged out');window.location='login';</script>")

def loginpage(request):
    return render(request, 'logins/login.html')


def techlogin(request):
    return render(request, 'logins/login.html')

def patlogin(request):
    return render(request, 'logins/login.html')

def patrep(request):
    return HttpResponse("<script>window.location='../patient/vr';</script>")















