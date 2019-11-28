from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from patient.models import Appointment
from admins.models import PatientRegistartion, TechnicianRegistration, Logins
from technician.models import AddTestResult, BloodTest, UricAcidTest, DiabetesTest, CholestrolTest
from django.template import loader
# Create your views here.

def index(request):
    # return HttpResponse('patient')
     return render(request, 'patienttemp/index.html')

def viewingreport(request):
    pname = request.session.get("email")
    pid = PatientRegistartion.objects.filter(Email=pname)
    context = {'pid': pid}
    return render(request, 'viewreportpatient/index.html', context)

def checkhem(request):
    patid = request.POST.get("pid")
    tstn = request.POST.get("testcheck")

    if(AddTestResult.objects.filter(Patient_ID=patid, Test_Name=tstn).exists()):
        if (tstn == "Hematology"):
            blood = BloodTest.objects.filter(Patient_ID=patid)
            context = {'blood': blood}
            return render(request, 'viewreportpatient/extendedindex.html', context)

        if(tstn =="Diabetes"):
            blood = DiabetesTest.objects.filter(Patient_ID=patid)
            context = {'blood': blood}
            return render(request, 'viewreportpatient/extendedindex.html', context)

        if(tstn =="UricAcid"):
            blood = UricAcidTest.objects.filter(Patient_ID=patid)
            context = {'blood': blood}
            return render(request, 'viewreportpatient/extendedindex.html', context)

        if(tstn =="Cholesterol"):
            blood = CholestrolTest.objects.filter(Patient_ID=patid)
            context = {'blood': blood}
            return render(request, 'viewreportpatient/extendedindex.html', context)

def submit(request):
    return HttpResponse("<script>window.location='../patient/vr';</script>")

def download(request):
    pname = request.session.get("email")
    pid = PatientRegistartion.objects.filter(Email=pname)
    context = {'pid': pid}
    return render(request, 'downloadtemp/downloadreport.html', context)

def repdownload(request):
    pname = request.session.get("email")
    pid = PatientRegistartion.objects.filter(Email=pname)
    patid = request.POST.get("pid")
    #context = {'patid': patid,'pid':pid}
    tstn = request.POST.get("testcheck")

    if (AddTestResult.objects.filter(Patient_ID=patid, Test_Name=tstn).exists()):
        if (tstn == "Hematology"):
            blood = BloodTest.objects.filter(Patient_ID=patid)
            context = {'blood': blood,'pid':pid}
            return render(request, 'downloadtemp/extendeddownload.html', context)

        if (tstn == "Diabetes"):
            blood = DiabetesTest.objects.filter(Patient_ID=patid)
            context = {'blood': blood, 'pid':pid}
            return render(request, 'downloadtemp/extendeddownload.html', context)

        if (tstn == "UricAcid"):
            blood = UricAcidTest.objects.filter(Patient_ID=patid)
            context = {'blood': blood, 'pid':pid}
            return render(request, 'downloadtemp/extendeddownload.html', context)

        if (tstn == "Cholesterol"):
            blood = CholestrolTest.objects.filter(Patient_ID=patid)
            context = {'blood': blood, 'pid':pid}
            return render(request, 'downloadtemp/extendeddownload.html', context)
def back(request):
    return HttpResponse("<script>window.location='../patient/dw';</script>")

def logout(request):
    try:
        del request.session['email']
    except:
        pass
    return HttpResponse("<script>alert('you are successfully logged out');window.location='login';</script>")

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
                    return HttpResponse("<script>window.location='../admins/adm';</script>")

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

def message(request):
    # return HttpResponse("ok")
    ap = Appointment()
    nm = request.POST.get("name")
    em = request.POST.get("email")
    sub = request.POST.get("subject")
    msg = request.POST.get("message")
    ap.Name = nm
    ap.Email = em
    ap.Subject = sub
    ap.Message = msg
    ap.save()
    return HttpResponse("<script>alert('Message sent successfully');window.location='./';</script>")


 










