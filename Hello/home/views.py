from datetime import datetime

from django.contrib import messages
from django.shortcuts import HttpResponse, render

from home.models import Contact


# Create your views here.
def index(request):
    context = {
        "variable1":"shubham is great",
        "variable2":"Rohan is great"
    } 
    return render(request, 'index.html', context)
    # return HttpResponse("this is homepage")

def about(request):
    return render(request, 'about.html') 

def menu(request):
    return render(request, 'menu.html')
 

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Yay.. meal Booked!')
    return render(request, 'contact.html')
 