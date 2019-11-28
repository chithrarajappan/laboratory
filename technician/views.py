from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from admins.models import PatientRegistartion, TechnicianRegistration, Logins
from technician.models import AddTestResult, BloodTest, UricAcidTest, DiabetesTest, CholestrolTest
from django.template import loader


# Create your views here.
def index(request):
    # return HttpResponse('technician')
     return render(request, 'techtemp/home.html')

def showpatientdetails(request):
    patient = PatientRegistartion.objects.all()
    context = {'patient': patient}
    return render(request, 'adminstemp/registeredpatient.html', context)

def addtest(request):
    # return HttpResponse('ok')
    return render(request, 'extendedtemp/index.html')


def patientdata(request):
    return render(request, 'pdtemp/index.html')


# def testprocess(request):
#
#     tp = AddTestResult()
#     dt = request.POST.get("datetime")
#     ptname = request.POST.get("patient")
#     testn = request.POST.get("test")
#     res = request.POST.get("result")
#     unit = request.POST.get("units")
#     ref = request.POST.get("range")
#     doct = request.POST.get("doc")
#     techn = request.POST.get("tech")
#     tp.DateTime = dt
#     tp.Patient_Name = ptname
#     tp.Test_Name = testn
#     tp.Result = res
#     tp.Units = unit
#     tp.Reference_range = ref
#     tp.Doctor_Consulted = doct
#     tp.Technician_Name = techn
#     tp.save()
#     return HttpResponse("<script>alert('Inserted successfully');window.location='./';</script>")

def hematology(request):

    adt = AddTestResult()
    dt = request.POST.get("date")
    patid = request.POST.get("pid")
    tn = request.POST.get("hemato")
    rs = request.POST.get("result")
    un = request.POST.get("units")
    rng = request.POST.get("range")
    dc = request.POST.get("doc")
    tecn = request.POST.get("tech")

    adt.DateTime = dt
    adt.Patient_ID = patid
    if (PatientRegistartion.objects.filter(id=patid).exists()):

        pat1 = PatientRegistartion.objects.filter(id=patid)
        for pat in pat1:
            patname = pat.Patient_Name
            adt.Test_Name = tn
            adt.Result = rs
            adt.Units = un
            adt.Reference_range = rng
            adt.Doctor_Consulted = dc
            adt.Patient_Name = patname
            adt.Technician_id = tecn
            adt.save()

    bld = BloodTest()
    patient = request.POST.get("pid")
    tst = request.POST.get("testname")
    res = request.POST.get("result")
    unt = request.POST.get("units")
    ran = request.POST.get("range")
    bld.Patient_ID = patient
    bld.Test = tst
    bld.Result = res
    bld.Units = unt
    bld.Reference_range = ran
    bld.save()
    return HttpResponse("<script>alert('Inserted successfully');window.location='./';</script>")

def diabetes(request):

    adt = AddTestResult()
    dt = request.POST.get("date")
    patid = request.POST.get("pid")
    tn = request.POST.get("diab")
    rs = request.POST.get("result")
    un = request.POST.get("units")
    rng = request.POST.get("range")
    dc = request.POST.get("doc")
    tecn = request.POST.get("tech")

    adt.DateTime = dt
    adt.Patient_ID = patid
    if (PatientRegistartion.objects.filter(id=patid).exists()):

        pat1 = PatientRegistartion.objects.filter(id=patid)
        for pat in pat1:
            patname = pat.Patient_Name
            adt.Test_Name = tn
            adt.Result = rs
            adt.Units = un
            adt.Reference_range = rng
            adt.Doctor_Consulted = dc
            adt.Patient_Name = patname
            adt.Technician_id = tecn
            adt.save()

    dia = DiabetesTest()
    tst = request.POST.get("testname")
    res = request.POST.get("result")
    unt = request.POST.get("units")
    ran = request.POST.get("range")
    dia.Patient_ID = patid
    dia.Test = tst
    dia.Result = res
    dia.Units = unt
    dia.Reference_range = ran
    dia.save()
    return HttpResponse("<script>alert('Inserted successfully');window.location='./';</script>")


def uricacid(request):
    adt = AddTestResult()
    dt = request.POST.get("date")
    patid = request.POST.get("pid")
    tn = request.POST.get("uric")
    rs = request.POST.get("result")
    un = request.POST.get("units")
    rng = request.POST.get("range")
    dc = request.POST.get("doc")
    tecn = request.POST.get("tech")

    adt.DateTime = dt
    adt.Patient_ID = patid
    if (PatientRegistartion.objects.filter(id=patid).exists()):

        pat1 = PatientRegistartion.objects.filter(id=patid)
        for pat in pat1:
            patname = pat.Patient_Name
            adt.Test_Name = tn
            adt.Result = rs
            adt.Units = un
            adt.Reference_range = rng
            adt.Doctor_Consulted = dc
            adt.Patient_Name = patname
            adt.Technician_id = tecn
            adt.save()

    uric = UricAcidTest()
    tst = request.POST.get("testname")
    res = request.POST.get("result")
    unt = request.POST.get("units")
    ran = request.POST.get("range")
    uric.Patient_ID = patid
    uric.Test = tst
    uric.Result = res
    uric.Units = unt
    uric.Reference_range = ran
    uric.save()
    return HttpResponse("<script>alert('Inserted successfully');window.location='./';</script>")

def cholestrol(request):
    adt = AddTestResult()
    dt = request.POST.get("date")
    patid = request.POST.get("pid")
    tn = request.POST.get("choles")
    rs = request.POST.get("result")
    un = request.POST.get("units")
    rng = request.POST.get("range")
    dc = request.POST.get("doc")
    tecn = request.POST.get("tech")

    adt.DateTime = dt
    adt.Patient_ID = patid
    if (PatientRegistartion.objects.filter(id=patid).exists()):

        pat1 = PatientRegistartion.objects.filter(id=patid)
        for pat in pat1:
            patname = pat.Patient_Name
            adt.Test_Name = tn
            adt.Result = rs
            adt.Units = un
            adt.Reference_range = rng
            adt.Doctor_Consulted = dc
            adt.Patient_Name = patname
            adt.Technician_id = tecn
            adt.save()

    cho = CholestrolTest()
    tst = request.POST.get("testname")
    res = request.POST.get("result")
    unt = request.POST.get("units")
    ran = request.POST.get("range")
    cho.Patient_ID = patid
    cho .Test = tst
    cho.Result = res
    cho .Units = unt
    cho .Reference_range = ran
    cho .save()
    return HttpResponse("<script>alert('Inserted successfully');window.location='./';</script>")

def patientreport(request):
    return render(request, 'patientreporttemp/index.html')

def reporthematology(request):
    stud = BloodTest.objects.all()
    context = {'stud': stud}
    return render(request, 'patientreporttemp/reporthem.html', context)

def reportdiabetes(request):
    stud = DiabetesTest.objects.all()
    context = {'stud': stud}
    return render(request, 'patientreporttemp/reportdiab.html', context)

def reporturic(request):
    stud = UricAcidTest.objects.all()
    context = {'stud': stud}
    return render(request, 'patientreporttemp/reporturic.html', context)

def reportcholestrol(request):
    stud = CholestrolTest.objects.all()
    context = {'stud': stud}
    return render(request, 'patientreporttemp/reportchol.html', context)

def reporthome(request):
    return render(request, 'patientreporttemp/index.html')

def checkin(request):
    patid = request.POST.get("pid")
    stud = BloodTest.objects.filter(Patient_ID=patid)
    context = {'stud': stud}
    return render(request, 'patientreporttemp/reporthem.html', context)

def cholcheck(request):
    patid = request.POST.get("pid")
    stud = CholestrolTest.objects.filter(Patient_ID=patid)
    context = {'stud': stud}
    return render(request, 'patientreporttemp/reportchol.html', context)

def uriccheck(request):
    patid = request.POST.get("pid")
    stud = UricAcidTest.objects.filter(Patient_ID=patid)
    context = {'stud': stud}
    return render(request, 'patientreporttemp/reporturic.html', context)

def diabcheck(request):
    patid = request.POST.get("pid")
    stud = DiabetesTest.objects.filter(Patient_ID=patid)
    context = {'stud': stud}
    return render(request, 'patientreporttemp/reportdiab.html', context)

def finalreport(request):
    patid = request.POST.get("pid")
    stud = AddTestResult.objects.filter(Patient_ID=patid)
    context = {'stud': stud}
    return render(request, 'patientreporttemp/finalreport.html', context)

def logout(request):
    try:
        del request.session['email']
    except:
        pass
    return HttpResponse("<script>alert('you are successfully logged out');window.location='login';</script>")


def login(request):
    return render(request, 'logins/login.html')

def techome(request):
    return render(request, 'techtemp/home.html')
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



































