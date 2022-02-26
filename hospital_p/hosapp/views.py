from django.shortcuts import render
from .models import Patient
from django.contrib import messages


# Create your views here.

def doctor(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')

        if mobile.isdigit():
            v = Patient(name=name, age=age, gender=gender, mobile=mobile, address=address)
            v.save()

            messages.success(request, 'Appointment Successfully')
        else:
            messages.error(request,'Your Mobile No Is Wrong')
    return render(request, 'index.html')
