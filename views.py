from django.contrib.auth.signals import user_logged_in
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import studentgriev , contactus
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages
from django.contrib import auth


def index(request):
    return render(request,'index.html')
    #return HttpResponse("Homepage!")

def stusignup(request):
    if request.method == "POST":
        myusername = request.POST['name']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']

        if not pass1 == pass2:
            messages.error(request,"Please enter same password!")
        else:
            myuser = User.objects.create_user(username=myusername,password=pass1,email=email)
        
            myuser.name = myusername
            myuser.email = email
            myuser.password = pass1
            myuser.save()

            return redirect('studentloginpage')

    return render(request,'stusignup.html')

def stuloginpage(request):
    if request.method == 'POST':
        user_email = request.POST['email']
        pass1 = request.POST['password']

        user = User.objects.get(email=user_email,password=pass1) 

        if user is not None:
            login(request,user)
            return redirect('homepage')
            #messages.success(request,'Login Succcessful')

        else:
            messages.info(request, "Username OR Password is INCORRECT")

    return render(request,'stulogin.html')

def stulogout(request):
    logout(request)
    return redirect('selectlogintype')

def facsignup(request):
    if request.method == "POST":
        myusername = request.POST['name']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']

        if not pass1 == pass2:
            messages.warning(request,"Please enter same password!")
            return render(request,'facsignup.html')
        else:
            myuser = User.objects.create_user(username=myusername,password=pass1,email=email)
        
        myuser.name = myusername
        myuser.email = email
        myuser.password = pass1
        myuser.save()

        return redirect('facultyloginpage')

    return render(request,'facsignup.html')

def facloginpage(request):
    if request.method == 'POST':
        user_email = request.POST['email']
        pass1 = request.POST['password']

        myuser = User.objects.get(email=user_email,password=pass1) 

        if myuser is not None:
            login(request,myuser)
            return redirect('facgrievpage')
            #messages.success(request,'Login Succcessful')

        else:
            return redirect('facultyloginpage')
            #raise ValidationError
            #messages.error(request, "Invalid Login")

    return render(request,'faclogin.html')



def stugrievpage(request):
    if request.method == 'POST':
        name = request.POST['name']
        contactnum = request.POST['contactnum']
        email = request.POST['email']
        grievance = request.POST['message']
       # print(name,contactnum,email,grievance)

        griv = studentgriev()
        griv.name = name
        griv.contactnum = contactnum
        griv.email = email
        griv.grievance = grievance
        griv.save()
    return render(request,'stugrievances.html')
    


def facgrievpage(request):
    grievance_data =  studentgriev.objects.all()
    return render(request,'facgrievances.html',{"data":grievance_data})    

def chooselogin(request):
    return render(request,'Welcome.html')
    

def contactuspage(request):
    if request.method == 'POST':
        ctname = request.POST['name']
        ctemail = request.POST['email']
        ctsubject = request.POST['subject']
        ctmessage = request.POST['message']

       # print(ctname,ctemail,ctsubject,ctmessage)

        ctus = contactus()
        ctus.ctname = ctname
        ctus.ctemail = ctemail
        ctus.ctsubject = ctsubject
        ctus.ctmessage = ctmessage
        ctus.save()

    return render(request,'contactus.html')
    

def aboutus(request):
    return render(request,'about.html')

