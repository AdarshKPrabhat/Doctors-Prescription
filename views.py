from django.shortcuts import render

from django.http import HttpResponse
#from .models import
from . import final

# Create your views here.
def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,"signup.html")

def showRecords(request):
    pass

def logout(request):
    pass

def showPrescription(request):
    pass

def record(request):
    e = final.final()
    #e.startrecord()
    e.convert_to_text()
    #e.text_filtration()
    """e.text_separation()
    e.merged_file()
    e.google_translate()
    e.pdfgene()"""
    return render(request,'home.html')