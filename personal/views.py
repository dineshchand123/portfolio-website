from django.shortcuts import render,HttpResponse
from datetime import datetime
from personal.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    current_year=datetime.now().year #get the current year
    return render(request, 'index.html',{'current_year':current_year})
    
    
def about(request):
     return render(request, 'about.html')


def resume(request):
     return render(request, 'resume.html')


def portfolio(request):
    return render(request, 'portfolio.html')


def services(request):
     return render(request, 'services.html')
    

def contact(request):
     if request.method== "POST":
          name= request.POST.get('name')
          email= request.POST.get('email')
          phone= request.POST.get('phone')
          desc= request.POST.get('desc')
          name= request.POST.get('name')
          contact= Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
          contact.save()
          messages.success(request, "Your message has been sent!")
     return render(request, 'contact.html')
     