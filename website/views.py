from django.shortcuts import render

def home(request):
    return render(request,"index.html")

def company(request):
    return render(request,"company.html")

def solutions(request):
    return render(request,"solutions.html")

def order(request):
    return render(request,"order.html")

def contact(request):
    return render(request,"contact_us.html")

def efds(request):
    return render(request,"efds.html")

def attendance(request):
    return render(request,"attendance.html")

def plant_disease(request):
    return render(request,"plant_disease.html")
def jrs(request):
    return render(request,"jrs.html")
