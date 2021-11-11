from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.index,name = "homepage"),
    path('',views.chooselogin,name = "selectlogintype"),
    path('stugriev/',views.stugrievpage,name = "stugrievpage"),
    path('facgriev/',views.facgrievpage,name = "facgrievpage"),
    path('contactus/',views.contactuspage,name = "contactuspage"),
    path('aboutus/',views.aboutus, name = "aboutuspage"),
    path('stusignup/',views.stusignup,name="studentsignup"),
    path('stulogin/',views.stuloginpage,name ="studentloginpage"),
    path('stulogout/',views.stulogout,name="studentlogout"),
    path('facsignup/',views.facsignup,name="facultysignup"),
    path('faclogin/',views.facloginpage,name ="facultyloginpage"),
    path('faclogout/',views.stulogout,name="facultylogout"),
    #path('register/',views.registerpage,name = "registerpage"),
    #path('testlogin',views.testlogin,name="testlogin")
     
]

